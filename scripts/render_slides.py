#!/usr/bin/env python3
"""Capture presentation screenshots with an installed Chromium-family browser.

This helper creates review artifacts. A successful capture does not mean that
the presentation has passed visual review; a person must inspect the images.
"""

from __future__ import annotations

import argparse
import os
import shutil
import signal
import struct
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Viewport:
    name: str
    width: int
    height: int


VIEWPORTS = (
    Viewport("desktop", 1440, 900),
    Viewport("tablet", 1024, 768),
    Viewport("mobile", 390, 844),
)

MAC_BROWSER_PATHS = (
    Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
    Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
    Path("/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"),
)

COMMAND_NAMES = (
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "microsoft-edge",
    "brave-browser",
)


def find_browser(explicit: Path | None = None) -> Path | None:
    """Return an executable Chromium-family browser already on the system."""
    if explicit is not None:
        candidate = explicit.expanduser().resolve()
        return candidate if candidate.is_file() and candidate.stat().st_mode & 0o111 else None

    for command in COMMAND_NAMES:
        resolved = shutil.which(command)
        if resolved:
            return Path(resolved)

    for candidate in MAC_BROWSER_PATHS:
        if candidate.is_file() and candidate.stat().st_mode & 0o111:
            return candidate
    return None


def png_dimensions(path: Path) -> tuple[int, int] | None:
    """Read PNG dimensions using the standard IHDR header."""
    try:
        with path.open("rb") as image:
            header = image.read(24)
    except OSError:
        return None
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", header[16:24])


def stop_browser_process(process: subprocess.Popen[str], grace_period: float = 2.0) -> bool:
    """Stop only the browser process tree started for this capture."""
    if process.poll() is not None:
        return True

    try:
        if os.name == "posix":
            os.killpg(process.pid, signal.SIGTERM)
        else:
            process.terminate()
    except ProcessLookupError:
        return True
    except OSError:
        pass

    try:
        process.wait(timeout=grace_period)
        return True
    except subprocess.TimeoutExpired:
        pass

    try:
        if os.name == "posix":
            os.killpg(process.pid, signal.SIGKILL)
        else:
            process.kill()
    except ProcessLookupError:
        return True
    except OSError:
        return process.poll() is not None

    try:
        process.wait(timeout=grace_period)
    except subprocess.TimeoutExpired:
        return False
    return True


def capture(
    browser: Path,
    html_file: Path,
    output_file: Path,
    viewport: Viewport,
    profile_directory: Path,
    timeout: float,
) -> tuple[bool, str]:
    """Run one headless browser capture and return success plus a message."""
    command = [
        str(browser),
        "--headless=new",
        "--disable-gpu",
        "--disable-extensions",
        "--hide-scrollbars",
        "--no-default-browser-check",
        "--no-first-run",
        "--allow-file-access-from-files",
        f"--user-data-dir={profile_directory}",
        f"--window-size={viewport.width},{viewport.height}",
        "--virtual-time-budget=1200",
        f"--screenshot={output_file}",
        html_file.as_uri(),
    ]

    try:
        output_file.unlink(missing_ok=True)
    except OSError as error:
        return False, f"could not replace existing screenshot: {error}"

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            start_new_session=(os.name == "posix"),
        )
    except OSError as error:
        return False, f"browser could not start: {error}"

    timed_out = False
    cleaned_up = True
    stdout = ""
    stderr = ""
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        cleaned_up = stop_browser_process(process)
        stdout, stderr = process.communicate()
    finally:
        if process.poll() is None:
            cleaned_up = stop_browser_process(process) and cleaned_up

    if not output_file.is_file() or output_file.stat().st_size == 0:
        if timed_out:
            return False, f"browser timed out after {timeout:g} seconds without creating a usable PNG"
        detail = (stderr or stdout).strip().splitlines()
        summary = detail[-1] if detail else f"browser exited with code {process.returncode}"
        return False, summary

    dimensions = png_dimensions(output_file)
    if dimensions is None:
        return False, "created file is not a readable PNG"
    if not cleaned_up:
        return False, "screenshot was created, but the spawned browser process could not be stopped safely"

    cleanup_note = "; browser cleaned up after capture" if timed_out else ""
    if dimensions != (viewport.width, viewport.height):
        return True, (
            f"created at {dimensions[0]}×{dimensions[1]} "
            f"(requested {viewport.width}×{viewport.height}){cleanup_note}"
        )
    return True, f"created at {dimensions[0]}×{dimensions[1]}{cleanup_note}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Capture desktop, tablet, and mobile screenshots of a standalone HTML "
            "presentation using an already-installed Chromium-family browser."
        ),
        epilog=(
            "Screenshots support visual review but do not prove that the presentation "
            "passes accessibility, interaction, or layout quality checks."
        ),
    )
    parser.add_argument("html_file", type=Path, help="Path to the standalone HTML presentation.")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("rendered"),
        help="Directory for desktop.png, tablet.png, and mobile.png (default: rendered).",
    )
    parser.add_argument(
        "--browser",
        type=Path,
        help="Optional path to an installed Chrome, Chromium, Edge, or Brave executable.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Maximum seconds allowed for each screenshot (default: 30).",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    html_file = args.html_file.expanduser().resolve()
    output_directory = args.output_dir.expanduser().resolve()

    if not html_file.exists():
        print(f"FAIL: HTML file does not exist: {html_file}")
        return 1
    if not html_file.is_file():
        print(f"FAIL: HTML path is not a regular file: {html_file}")
        return 1
    if args.timeout <= 0:
        print("FAIL: --timeout must be greater than zero.")
        return 1

    browser = find_browser(args.browser)
    if browser is None:
        if args.browser:
            print(f"WARN: The requested browser is missing or not executable: {args.browser}")
        else:
            print("WARN: No supported Chromium-family browser automation runtime was found.")
        print("WARN: No screenshots were created. Open the HTML file manually and review desktop and mobile layouts.")
        print("Visual capture result: UNAVAILABLE")
        return 2

    try:
        output_directory.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        print(f"FAIL: Could not create output directory {output_directory}: {error}")
        return 1

    print(f"PASS: HTML file found: {html_file}")
    print(f"PASS: Browser automation available: {browser}")
    print(f"PASS: Screenshot directory: {output_directory}")

    successes: list[Path] = []
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="presentation-browser-profile-") as profile:
        profile_root = Path(profile)
        for viewport in VIEWPORTS:
            output_file = output_directory / f"{viewport.name}.png"
            success, detail = capture(
                browser,
                html_file,
                output_file,
                viewport,
                profile_root / viewport.name,
                args.timeout,
            )
            if success:
                successes.append(output_file)
                print(f"PASS: {viewport.name.capitalize()} screenshot {detail}: {output_file}")
            else:
                failures.append(viewport.name)
                print(f"FAIL: {viewport.name.capitalize()} screenshot was not created: {detail}")

    print()
    if successes:
        print("Created screenshots:")
        for screenshot in successes:
            print(f"- {screenshot}")
    else:
        print("No screenshots were created.")

    print("WARN: Screenshot creation is not a visual-quality pass. Inspect every image manually.")
    if failures:
        print("WARN: Manual review is required for failed viewport(s): " + ", ".join(failures) + ".")
        print("Visual capture result: PARTIAL" if successes else "Visual capture result: FAIL")
        return 1

    print("Visual capture result: COMPLETE (manual review still required)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
