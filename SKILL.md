---
name: interactive-html-presentation
description: Create or improve interactive, responsive, highly readable standalone HTML presentations. Use when converting documents, reports, research, notes, or data into slides or pitch decks; creating web-native presentations; or editing existing HTML presentations to improve narrative, readability, UI/UX, responsiveness, visuals, or interactions.
---

# Interactive HTML Presentation

Create or edit presentation-focused HTML with an editorial visual language, meaningful interaction, and faithful use of source material. Use the reference files as the detailed source of truth; do not duplicate their guidance in the working context unless it is relevant to the request.

## Choose the workflow

### Create from source

Use for documents, reports, research, notes, and other narrative source material. Read [references/create-from-source.md](references/create-from-source.md).

### Create from data

Use for structured data, tables, spreadsheet content, research findings, metrics, or other quantitative information. Read [references/create-from-data.md](references/create-from-data.md).

### Improve existing HTML

Use when editing, restyling, repairing, or improving an existing HTML presentation. Read [references/improve-existing-html.md](references/improve-existing-html.md) and preserve unaffected content and working behavior.

If a request combines workflows, use each relevant reference and preserve one coherent narrative and design system.

## Route to shared references

- Read [references/editorial-design-system.md](references/editorial-design-system.md) for visual design, typography, layout, hierarchy, whitespace, composition, responsiveness, and visual anti-patterns.
- Read [references/interactions-and-accessibility.md](references/interactions-and-accessibility.md) when adding or changing Level 2 interactions or accessibility behavior.
- Read [references/source-integrity.md](references/source-integrity.md) whenever factual claims, source material, financial information, quotations, citations, charts, data, or derived metrics are involved.
- Read [references/quality-checklist.md](references/quality-checklist.md) before every final delivery.

## Shared creation process

1. Understand the request, audience, purpose, and source material.
2. Determine the appropriate workflow.
3. Read the required workflow and shared reference files.
4. Build or revise the narrative.
5. Assign visual compositions and meaningful Level 2 interactions based on communication needs.
6. Preserve citations, provenance, and factual distinctions.
7. Complete the final stages in order: generate/edit HTML → validate HTML → render desktop/tablet/mobile → inspect → repair → validate again → render again → final quality gate → deliver.

## Final validation workflow

Use the existing scripts rather than recreating their checks with ad hoc instructions.

1. Run `scripts/validate_html.py <presentation.html>` and review every result.
2. Treat each `FAIL` as a delivery blocker and repair it. Treat each `WARN` as a review target, not an automatic failure; determine whether it represents a real problem.
3. When browser rendering is available, run `scripts/render_slides.py <presentation.html>` and inspect its desktop, tablet, and mobile screenshots. Static validation alone does not prove visual quality.
4. Inspect clipping, overlap, horizontal overflow, typography readability, visual hierarchy, repeated layouts, interactive controls, and responsive behavior.
5. Repair discovered problems, then rerun both validation and browser rendering.
6. Apply [references/quality-checklist.md](references/quality-checklist.md) and deliver only after the final quality gate passes.

If browser rendering is unavailable, clearly state that manual visual inspection is still required.

## Global requirements

Every result must:

- be a standalone HTML file that opens directly in a browser;
- prioritize exceptional readability and editorial presentation design;
- behave responsively without clipping, overlap, or page-level horizontal overflow;
- use accessible semantic structure, controls, focus states, and reduced-motion behavior;
- use Level 2 interaction only when it improves understanding or navigation;
- preserve source facts, definitions, qualifications, and important distinctions;
- include traceable citations where appropriate;
- avoid invented information, data, sources, quotations, and citations;
- avoid unnecessary dependencies; and
- pass the final quality-control and repair process before delivery.

## Decision rules

Prefer:

- understanding over literal source formatting;
- restructuring or additional slides over shrinking content;
- visual forms chosen from the information relationship;
- factual precision over visual simplicity;
- meaningful compositional variety over repetitive layouts;
- restrained, purposeful visuals over decorative complexity; and
- interaction as a communication tool rather than an effect.

Do not:

- reproduce source pages blindly;
- turn every paragraph into bullets;
- invent data or citations;
- use tiny text to force content into a slide;
- default to cards or repeated card grids;
- add interaction without a communication purpose; or
- introduce a dependency without a strong, task-specific reason.

Always inspect and repair the actual result before delivery.
