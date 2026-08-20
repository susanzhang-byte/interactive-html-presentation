# Interactive HTML Presentation

`interactive-html-presentation` is a ChatGPT Skill for creating and improving polished, standalone HTML presentations. It transforms source material into a presentation narrative instead of copying document pages or placing raw data directly onto slides.

The Skill is designed for exceptionally readable presentations with strong UI/UX, responsive desktop, tablet, and mobile layouts, meaningful Level 2 interaction, accessibility, and careful source and data integrity. Its final workflow includes deterministic HTML validation and browser-based visual review.

## Supported workflows

1. **Create from source material:** Turn documents, reports, research, notes, and other narrative material into an interactive HTML presentation.
2. **Create from structured data:** Analyze sources such as CSV files and present the most important trends, comparisons, and implications clearly.
3. **Improve existing HTML:** Edit, restyle, or repair an existing HTML presentation while preserving unaffected content and working behavior.

## Example requests

- “Turn this report into an interactive HTML presentation.”
- “Turn this CSV into an executive presentation.”
- “Improve the readability of this existing HTML presentation.”
- “Create an investor pitch deck from this source material.”

## How to install and use

This repository contains a ChatGPT Skill. Download or clone the repository, then install or import the Skill using the current ChatGPT Skill installation process available in your environment.

Once installed, provide the relevant document, data, notes, or existing HTML and describe the presentation outcome you want. The Skill can also be invoked explicitly as `$interactive-html-presentation` when supported.

## Project structure

- `SKILL.md` is the control plane. It defines activation, workflow routing, shared requirements, and the final validation process.
- `agents/` contains concise ChatGPT-facing metadata and invocation policy.
- `references/` contains detailed guidance for the three workflows, editorial design, interaction, accessibility, source integrity, and quality control.
- `scripts/` contains dependency-free Python tools for deterministic HTML validation and browser screenshot rendering.
- `assets/` contains the reusable standalone HTML presentation starter.
- `tests/` contains source fixtures and generated presentations used to exercise the workflows. Included example data and business content are clearly marked as fictional test material where applicable.

## Design philosophy

- Readability comes before information density or visual novelty.
- Interaction must clarify information rather than decorate it.
- Responsive layouts recompose content intentionally instead of shrinking desktop slides.
- Facts, values, definitions, distinctions, sources, and citations remain faithful to the supplied material.
- Existing HTML is edited with the smallest coherent change that satisfies the request.
- Every result follows: validate → render → inspect → repair → revalidate → rerender → final quality gate.

## Testing

The repository includes narrative, pitch-deck, and structured-data fixtures for testing presentation creation and existing-HTML editing. Generated fixture presentations can be checked with:

```bash
python scripts/validate_html.py path/to/presentation.html
python scripts/render_slides.py path/to/presentation.html
```

The validator performs deterministic structural checks. The renderer captures desktop, tablet, and mobile screenshots for manual review; a successful screenshot does not by itself prove visual quality.

## Dependencies

Generated presentation HTML is designed to be standalone. It does not require external CSS, JavaScript libraries, iframes, CDNs, or a build step. The included validation scripts use the Python standard library, while visual rendering uses an already-installed supported browser when available.
