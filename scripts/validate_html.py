#!/usr/bin/env python3
"""Dependency-free structural validator for standalone HTML presentations."""

from __future__ import annotations

import argparse
import os
import re
import statistics
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Results:
    def __init__(self) -> None:
        self.messages: list[tuple[str, str]] = []

    def add(self, level: str, message: str) -> None:
        self.messages.append((level, message))

    def passed(self, message: str) -> None:
        self.add("PASS", message)

    def warn(self, message: str) -> None:
        self.add("WARN", message)

    def fail(self, message: str) -> None:
        self.add("FAIL", message)

    @property
    def has_failures(self) -> bool:
        return any(level == "FAIL" for level, _ in self.messages)

    def print_report(self) -> None:
        for level, message in self.messages:
            print(f"{level}: {message}")
        print(f"\nValidation result: {'FAIL' if self.has_failures else 'PASS'}")


class Inspector(HTMLParser):
    """Collect facts that can be checked reliably without a browser."""

    IDREF_ATTRIBUTES = {"aria-controls", "aria-describedby", "aria-labelledby", "aria-owns"}
    ASSET_TAGS = {"audio", "img", "input", "link", "source", "track", "video"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.doctype = False
        self.tags: dict[str, int] = {}
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.fragments: list[tuple[str, int]] = []
        self.idrefs: list[tuple[str, str, int]] = []
        self.local_files: list[tuple[str, str, int]] = []
        self.remote_assets: list[tuple[str, str, int]] = []
        self.empty_refs: list[tuple[str, str, int]] = []
        self.stylesheets: list[tuple[str, int]] = []
        self.external_scripts: list[tuple[str, int]] = []
        self.iframes: list[int] = []
        self.has_viewport = False
        self.title_text: list[str] = []
        self.styles: list[str] = []
        self.scripts: list[str] = []
        self.slides: list[dict[str, object]] = []
        self.buttons: list[dict[str, object]] = []
        self.tables: list[dict[str, object]] = []
        self.interactive_elements: list[dict[str, object]] = []
        self._stack: list[str] = []
        self._slide_stack: list[dict[str, object]] = []
        self._button_stack: list[dict[str, object]] = []
        self._heading_stack: list[dict[str, object]] = []
        self._table_stack: list[dict[str, object]] = []
        self._interactive_stack: list[dict[str, object]] = []
        self._capture: str | None = None
        self._captured: list[str] = []

    def handle_decl(self, decl: str) -> None:
        self.doctype = decl.strip().lower() == "doctype html" or self.doctype

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attrs = {key.lower(): (value or "") for key, value in attrs_list}
        line = self.getpos()[0]
        self._stack.append(tag)
        self.tags[tag] = self.tags.get(tag, 0) + 1

        element_id = attrs.get("id", "").strip()
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)

        for attribute in self.IDREF_ATTRIBUTES:
            for target in attrs.get(attribute, "").split():
                self.idrefs.append((attribute, target, line))

        if tag == "meta" and attrs.get("name", "").lower() == "viewport" and attrs.get("content", "").strip():
            self.has_viewport = True
        if tag == "link" and "stylesheet" in attrs.get("rel", "").lower().split():
            self.stylesheets.append((attrs.get("href", ""), line))
        if tag == "script" and "src" in attrs:
            self.external_scripts.append((attrs["src"], line))
        if tag == "iframe":
            self.iframes.append(line)

        for attribute in ("href", "src"):
            if attribute in attrs and not attrs[attribute].strip():
                self.empty_refs.append((tag, attribute, line))

        self._record_url(tag, "href", attrs.get("href"), line)
        self._record_url(tag, "src", attrs.get("src"), line)
        self._record_url(tag, "poster", attrs.get("poster"), line)
        for candidate in attrs.get("srcset", "").split(","):
            parts = candidate.strip().split(maxsplit=1)
            url = parts[0] if parts else ""
            if url:
                self._record_url(tag, "srcset", url, line)

        classes = set(attrs.get("class", "").split())
        if tag == "section" and ("slide" in classes or "data-slide" in attrs):
            slide = {
                "line": line,
                "depth": len(self._stack),
                "heading": False,
                "headings": [],
                "text": [],
                "structure": [],
                "classes": tuple(sorted(classes - {"is-active"})),
                "label": attrs.get("aria-label", "").strip(),
                "labelledby": attrs.get("aria-labelledby", "").strip(),
            }
            self.slides.append(slide)
            self._slide_stack.append(slide)
        elif self._slide_stack:
            slide = self._slide_stack[-1]
            depth = len(self._stack) - int(slide["depth"])
            if depth <= 2:
                signature = tag
                if classes:
                    signature += "." + ".".join(sorted(classes - {"is-active"}))
                slide["structure"].append(signature)  # type: ignore[union-attr]
        if self._slide_stack and tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._slide_stack[-1]["heading"] = True
            heading = {"line": line, "text": []}
            self._slide_stack[-1]["headings"].append(heading)  # type: ignore[union-attr]
            self._heading_stack.append(heading)

        if tag == "button":
            button = {"line": line, "attrs": attrs, "text": []}
            self.buttons.append(button)
            self._button_stack.append(button)

        if tag == "table":
            table = {"line": line, "rows": 0, "columns": 0, "current_columns": 0}
            self.tables.append(table)
            self._table_stack.append(table)
        elif self._table_stack and tag == "tr":
            self._table_stack[-1]["rows"] = int(self._table_stack[-1]["rows"]) + 1
            self._table_stack[-1]["current_columns"] = 0
        elif self._table_stack and tag in {"th", "td"}:
            table = self._table_stack[-1]
            table["current_columns"] = int(table["current_columns"]) + 1
            table["columns"] = max(int(table["columns"]), int(table["current_columns"]))

        is_interactive = (
            tag in {"details", "input", "select", "textarea", "canvas"}
            or attrs.get("role", "").lower() in {"button", "tab", "tablist", "switch", "slider"}
            or "onclick" in attrs
        )
        if is_interactive:
            element = {"tag": tag, "line": line, "attrs": attrs, "text": [], "has_summary": False}
            self.interactive_elements.append(element)
            self._interactive_stack.append(element)
        if tag == "summary" and self._interactive_stack and self._interactive_stack[-1]["tag"] == "details":
            self._interactive_stack[-1]["has_summary"] = True

        if tag in {"style", "title"} or (tag == "script" and "src" not in attrs):
            self._capture = tag
            self._captured = []

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self._capture == tag:
            text = "".join(self._captured)
            {"style": self.styles, "script": self.scripts, "title": self.title_text}[tag].append(text)
            self._capture = None
            self._captured = []
        if tag == "button" and self._button_stack:
            self._button_stack.pop()
        if self._heading_stack and tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._heading_stack.pop()
        if tag == "table" and self._table_stack:
            self._table_stack.pop()
        if self._interactive_stack and tag == self._interactive_stack[-1]["tag"]:
            self._interactive_stack.pop()
        if tag == "section" and self._slide_stack:
            if len(self._stack) == self._slide_stack[-1]["depth"]:
                self._slide_stack.pop()
        if self._stack:
            if self._stack[-1] == tag:
                self._stack.pop()
            elif tag in self._stack:
                del self._stack[len(self._stack) - self._stack[::-1].index(tag) - 1 :]

    def handle_data(self, data: str) -> None:
        if self._capture:
            self._captured.append(data)
        for button in self._button_stack:
            button["text"].append(data)  # type: ignore[union-attr]
        for slide in self._slide_stack:
            slide["text"].append(data)  # type: ignore[union-attr]
        for heading in self._heading_stack:
            heading["text"].append(data)  # type: ignore[union-attr]
        for element in self._interactive_stack:
            element["text"].append(data)  # type: ignore[union-attr]

    def _record_url(self, tag: str, attribute: str, value: str | None, line: int) -> None:
        if not value:
            return
        value = value.strip()
        if attribute == "href" and value.startswith("#"):
            if value[1:]:
                self.fragments.append((unquote(value[1:]), line))
            return
        kind = classify_url(value)
        if kind == "local" and (tag in self.ASSET_TAGS or tag == "a"):
            self.local_files.append((value, f"{tag}[{attribute}]", line))
        elif kind == "remote" and tag in self.ASSET_TAGS:
            self.remote_assets.append((value, tag, line))


def classify_url(value: str) -> str:
    lowered = value.lower()
    if lowered.startswith(("#", "data:", "mailto:", "tel:", "javascript:", "about:")):
        return "ignored"
    parsed = urlsplit(value)
    if parsed.scheme in {"http", "https"} or value.startswith("//"):
        return "remote"
    return "ignored" if parsed.scheme else "local"


def local_target(document: Path, reference: str) -> Path:
    raw_path = Path(unquote(urlsplit(reference).path))
    return raw_path if raw_path.is_absolute() else document.parent / raw_path


def button_is_named(button: dict[str, object], ids: set[str]) -> bool:
    attrs = button["attrs"]
    text = button["text"]
    assert isinstance(attrs, dict) and isinstance(text, list)
    if " ".join("".join(text).split()):
        return True
    if str(attrs.get("aria-label", "")).strip() or str(attrs.get("title", "")).strip():
        return True
    labelledby = str(attrs.get("aria-labelledby", "")).split()
    return bool(labelledby) and all(target in ids for target in labelledby)


def obvious_javascript_error(source: str) -> str | None:
    """Conservatively find unclosed strings, comments, or delimiters."""
    matching = {")": "(", "]": "[", "}": "{"}
    stack: list[tuple[str, int]] = []
    quote: str | None = None
    escaped = line_comment = block_comment = False
    line = 1
    index = 0
    while index < len(source):
        char = source[index]
        following = source[index + 1] if index + 1 < len(source) else ""
        if char == "\n":
            line += 1
            line_comment = False
        if line_comment:
            index += 1
            continue
        if block_comment:
            if char == "*" and following == "/":
                block_comment = False
                index += 2
            else:
                index += 1
            continue
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            index += 1
            continue
        if char == "/" and following == "/":
            line_comment = True
            index += 2
            continue
        if char == "/" and following == "*":
            block_comment = True
            index += 2
            continue
        if char in {'"', "'", "`"}:
            quote = char
        elif char in "([{":
            stack.append((char, line))
        elif char in ")]}":
            if not stack or stack[-1][0] != matching[char]:
                return f"unexpected {char!r} near script line {line}"
            stack.pop()
        index += 1
    if quote:
        return "unterminated string or template literal"
    if block_comment:
        return "unterminated block comment"
    if stack:
        return f"unclosed {stack[-1][0]!r} from script line {stack[-1][1]}"
    return None


def normalized_text(parts: object) -> str:
    """Return parser-collected text with browser-like whitespace collapsing."""
    if not isinstance(parts, list):
        return ""
    return " ".join("".join(str(part) for part in parts).split())


def css_font_size_risks(css: str) -> tuple[int, int]:
    """Count clearly large or small declared sizes without resolving CSS layout."""
    oversized = 0
    undersized = 0
    for declaration in re.finditer(r"font-size\s*:\s*([^;}]+)", css, re.I):
        value = declaration.group(1)
        sizes = re.findall(r"(-?\d*\.?\d+)\s*(px|rem|em|vw)", value, re.I)
        is_large = any(
            (unit.lower() == "px" and float(number) >= 64)
            or (unit.lower() in {"rem", "em"} and float(number) >= 4)
            or (unit.lower() == "vw" and float(number) >= 8)
            for number, unit in sizes
        )
        is_small = any(
            (unit.lower() == "px" and 0 < float(number) < 11)
            or (unit.lower() == "rem" and 0 < float(number) < 0.7)
            for number, unit in sizes
        )
        oversized += int(is_large)
        undersized += int(is_small)
    return oversized, undersized


def interactive_element_is_labeled(element: dict[str, object]) -> bool:
    """Recognize obvious labels only; ambiguous cases remain review warnings."""
    tag = str(element["tag"])
    attrs = element["attrs"]
    assert isinstance(attrs, dict)
    role = str(attrs.get("role", "")).lower()
    text = normalized_text(element["text"])
    named = bool(
        text
        or str(attrs.get("aria-label", "")).strip()
        or str(attrs.get("aria-labelledby", "")).strip()
        or str(attrs.get("title", "")).strip()
    )
    if tag == "details":
        return bool(element["has_summary"])
    if tag in {"input", "select", "textarea"}:
        return named or bool(str(attrs.get("id", "")).strip())
    if tag == "canvas":
        return named
    if role == "tablist":
        return bool(str(attrs.get("aria-label", "")).strip() or str(attrs.get("aria-labelledby", "")).strip())
    if "onclick" in attrs and tag not in {"button", "a"}:
        return named and bool(role or str(attrs.get("tabindex", "")).strip())
    return named


def add_visual_risk_warnings(result: Results, inspector: Inspector, source: str, css: str) -> None:
    """Add WARN-only review prompts for patterns that require a browser to judge."""
    warnings: list[str] = []
    oversized_count, undersized_count = css_font_size_risks(css)
    nearby_supporting_text = bool(
        re.search(
            r"<(?:strong|b|h[1-6])\b[^>]*>[^<]*(?:[$€£]\s*)?\d[^<]*</(?:strong|b|h[1-6])>\s*<(?:span|small|p)\b",
            source,
            re.I,
        )
    )
    if oversized_count and nearby_supporting_text:
        warnings.append(
            "Oversized display text has nearby supporting text; visually inspect spacing to prevent overlap."
        )

    slide_word_counts = []
    for slide in inspector.slides:
        text = normalized_text(slide["text"])
        slide_word_counts.append((int(slide["line"]), len(re.findall(r"\b[\w’'-]+\b", text))))
    if len(slide_word_counts) >= 3:
        median_words = statistics.median(count for _, count in slide_word_counts)
        dense_threshold = max(180, int(median_words * 2.25))
        dense = [(line, count) for line, count in slide_word_counts if count >= dense_threshold]
        if dense:
            details = ", ".join(f"line {line} ({count} words)" for line, count in dense)
            warnings.append(
                f"Unusually dense slide text detected at {details}; visually inspect hierarchy, fit, and progressive disclosure."
            )

    long_headings: list[tuple[int, int, int]] = []
    for slide in inspector.slides:
        headings = slide["headings"]
        assert isinstance(headings, list)
        for heading in headings:
            assert isinstance(heading, dict)
            text = normalized_text(heading["text"])
            word_count = len(text.split())
            if len(text) >= 120 or word_count >= 18:
                long_headings.append((int(heading["line"]), len(text), word_count))
    if long_headings:
        details = ", ".join(
            f"line {line} ({characters} characters, {words} words)"
            for line, characters, words in long_headings
        )
        warnings.append(
            f"Very long slide heading(s) detected at {details}; visually inspect line wrapping and hierarchy."
        )

    if len(inspector.slides) >= 6:
        signatures = []
        for slide in inspector.slides:
            classes = slide["classes"]
            structure = slide["structure"]
            assert isinstance(classes, tuple) and isinstance(structure, list)
            signatures.append((classes, tuple(structure)))
        repeated = Counter(signatures).most_common(1)[0][1]
        if repeated >= 5 and repeated / len(signatures) >= 0.6:
            warnings.append(
                f"The exact same shallow slide structure appears on {repeated} of {len(signatures)} slides; visually inspect whether the repetition supports or weakens the narrative."
            )

    large_tables = [
        table
        for table in inspector.tables
        if int(table["rows"]) >= 12
        or int(table["columns"]) >= 7
        or int(table["rows"]) * int(table["columns"]) >= 60
    ]
    if large_tables:
        details = ", ".join(
            f"line {table['line']} ({table['rows']} rows × {table['columns']} columns)"
            for table in large_tables
        )
        warnings.append(
            f"Large table(s) detected at {details}; visually inspect responsive reflow, labels, and readability."
        )

    ambiguous_interactions = [
        f"{element['tag']} at line {element['line']}"
        for element in inspector.interactive_elements
        if not interactive_element_is_labeled(element)
    ]
    if ambiguous_interactions:
        warnings.append(
            "Interactive content lacks an obvious semantic label or fallback: "
            + ", ".join(ambiguous_interactions)
            + "; inspect keyboard use, labeling, and the non-interactive state."
        )

    if undersized_count:
        warnings.append(
            f"Extremely small font-size declaration(s) detected ({undersized_count}); visually inspect readability at presentation and mobile sizes."
        )

    if warnings:
        result.warn("Visual-risk heuristics identify review targets, not proven design defects.")
        for warning in warnings:
            result.warn(warning)
    else:
        result.passed("No conservative visual-risk heuristic patterns were detected.")


def validate(path: Path) -> Results:
    result = Results()
    if not path.exists():
        result.fail(f"File does not exist: {path}")
        return result
    result.passed(f"File exists: {path}")
    if not path.is_file():
        result.fail(f"Path is not a regular file: {path}")
        return result
    if not os.access(path, os.R_OK):
        result.fail(f"File is not readable: {path}")
        return result
    try:
        source = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        result.fail("File is not readable UTF-8 text.")
        return result
    except OSError as error:
        result.fail(f"Could not read file: {error}")
        return result
    result.passed("File is readable UTF-8 text.")

    inspector = Inspector()
    try:
        inspector.feed(source)
        inspector.close()
    except Exception as error:
        result.fail(f"HTML could not be inspected: {error}")
        return result

    required = {
        "doctype": inspector.doctype,
        "html element": bool(inspector.tags.get("html")),
        "head element": bool(inspector.tags.get("head")),
        "body element": bool(inspector.tags.get("body")),
        "viewport meta tag": inspector.has_viewport,
        "non-empty title": bool("".join(inspector.title_text).strip()),
    }
    missing = [name for name, present in required.items() if not present]
    if missing:
        result.fail("Missing document structure: " + ", ".join(missing) + ".")
    else:
        result.passed("Required document structure and metadata are present.")

    if inspector.slides:
        result.passed(f"Found {len(inspector.slides)} semantic slide section(s).")
    else:
        result.fail("No semantic slides found; use section.slide or section[data-slide].")

    unlabeled = [
        str(slide["line"])
        for slide in inspector.slides
        if not slide["heading"] and not slide["label"] and not slide["labelledby"]
    ]
    if unlabeled:
        result.warn("Slides without a heading or accessible label at line(s): " + ", ".join(unlabeled) + ".")
    elif inspector.slides:
        result.passed("Every slide has a heading or accessible label.")

    unnamed = [str(button["line"]) for button in inspector.buttons if not button_is_named(button, inspector.ids)]
    if unnamed:
        result.fail("Buttons without an accessible name at line(s): " + ", ".join(unnamed) + ".")
    else:
        result.passed(f"All {len(inspector.buttons)} button(s) have accessible names.")

    if inspector.duplicate_ids:
        result.fail("Duplicate IDs found: " + ", ".join(sorted(inspector.duplicate_ids)) + ".")
    else:
        result.passed("Element IDs are unique.")

    broken_fragments = [(target, line) for target, line in inspector.fragments if target not in inspector.ids]
    broken_idrefs = [(attr, target, line) for attr, target, line in inspector.idrefs if target not in inspector.ids]
    if broken_fragments:
        result.fail("Broken fragment references: " + ", ".join(f"#{target} at line {line}" for target, line in broken_fragments) + ".")
    if broken_idrefs:
        result.fail("Broken accessibility references: " + ", ".join(f"{attr}={target!r} at line {line}" for attr, target, line in broken_idrefs) + ".")
    if not broken_fragments and not broken_idrefs:
        result.passed("Internal fragment and accessibility ID references resolve.")

    missing_files = [
        (kind, reference, line)
        for reference, kind, line in inspector.local_files
        if not local_target(path, reference).exists()
    ]
    if missing_files:
        result.fail("Missing local files: " + ", ".join(f"{kind}={ref!r} at line {line}" for kind, ref, line in missing_files) + ".")
    else:
        result.passed("No obviously missing local asset references found.")
    if inspector.remote_assets:
        result.warn("Remote media reduces standalone portability: " + ", ".join(f"{tag}={url!r} at line {line}" for url, tag, line in inspector.remote_assets) + ".")

    if inspector.stylesheets:
        result.fail("External CSS dependencies found: " + ", ".join(f"{href!r} at line {line}" for href, line in inspector.stylesheets) + ".")
    else:
        result.passed("No external CSS dependencies found.")
    if inspector.external_scripts:
        result.fail("External JavaScript dependencies found: " + ", ".join(f"{src!r} at line {line}" for src, line in inspector.external_scripts) + ".")
    else:
        result.passed("No external JavaScript dependencies found.")
    if inspector.iframes:
        result.fail("Iframe dependencies found at line(s): " + ", ".join(map(str, inspector.iframes)) + ".")
    else:
        result.passed("No iframe dependencies found.")

    css = "\n".join(inspector.styles)
    unsafe_width = re.search(r"\b(?:min-)?width\s*:\s*(?:10[1-9]|[2-9]\d{2,})(?:\.\d+)?vw\b", css, re.I)
    unsafe_edges = re.search(r"\bleft\s*:\s*-\d+(?:\.\d+)?(?:px|rem|vw)\b[^}]*\bright\s*:\s*-", css, re.I | re.S)
    if unsafe_width or unsafe_edges:
        result.fail("Obviously horizontal-overflow-prone CSS was found.")
    else:
        result.passed("No obviously unsafe horizontal-overflow declarations found.")
    result.warn("Static checks cannot prove rendered clipping, overlap, or overflow; test those in a browser.")
    add_visual_risk_warnings(result, inspector, source, css)

    patterns = {
        "TODO": r"\bTODO\b",
        "Lorem ipsum": r"\blorem\s+ipsum\b",
        "Replace this": r"\breplace\s+this\b",
        "placeholder": r"\bplaceholder\b",
    }
    placeholders = [label for label, pattern in patterns.items() if re.search(pattern, source, re.I)]
    if placeholders and path.name == "presentation-starter.html":
        result.warn("Starter fixture contains intentional placeholder language: " + ", ".join(placeholders) + ".")
    elif placeholders:
        result.fail("Obvious unfinished placeholder text found: " + ", ".join(placeholders) + ".")
    else:
        result.passed("No obvious unfinished placeholder text found.")

    if inspector.empty_refs:
        result.fail("Empty href or src attributes found: " + ", ".join(f"{tag}[{attr}] at line {line}" for tag, attr, line in inspector.empty_refs) + ".")
    else:
        result.passed("No empty href or src attributes found.")

    js_errors = []
    for number, script in enumerate(inspector.scripts, start=1):
        error = obvious_javascript_error(script)
        if error:
            js_errors.append(f"inline script {number}: {error}")
    if js_errors:
        result.fail("Obvious JavaScript syntax problems: " + "; ".join(js_errors) + ".")
    elif inspector.scripts:
        result.passed(f"Basic syntax scan passed for {len(inspector.scripts)} inline script block(s).")
        result.warn("JavaScript received a conservative standard-library scan, not full browser parsing or execution.")
    else:
        result.passed("No inline JavaScript blocks require syntax scanning.")
    return result


def argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate standalone HTML presentation structure without launching a browser.",
        epilog="Example: python scripts/validate_html.py path/to/presentation.html",
    )
    parser.add_argument("html_file", type=Path, help="Path to the HTML presentation file.")
    return parser


def main() -> int:
    args = argument_parser().parse_args()
    result = validate(args.html_file.expanduser())
    result.print_report()
    return 1 if result.has_failures else 0


if __name__ == "__main__":
    sys.exit(main())
