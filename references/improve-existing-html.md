# Improve existing HTML

Use this workflow to inspect, improve, and edit an existing HTML presentation. Preserve its content, architecture, appearance, and working behavior unless the user's request requires a change.

## Core principle

Edit the existing presentation intelligently. Do not automatically rebuild it.

Treat the current file as a working system with connected structure, styles, scripts, assets, content, navigation, and interactions. Make the smallest coherent change that fulfills the request without creating regressions elsewhere.

When a request is ambiguous, prefer a conservative improvement that preserves existing intent and functionality. Do not interpret a focused request as authorization for a broad redesign.

## Editing workflow

Use this sequence:

```text
Existing HTML
  → Inspect
  → Diagnose
  → Identify affected areas
  → Plan minimal changes
  → Edit
  → Validate
  → Visually review
  → Repair
  → Final quality check
```

Do not edit before understanding how the relevant markup, styles, and behavior work together.

## 1. Inspect before changing

Inspect the presentation as both source code and a rendered experience. Review enough of the whole presentation to understand shared patterns before changing an individual slide.

### Document and slide structure

Identify:

- the document landmarks and semantic structure;
- how slides or sections are represented and ordered;
- which elements are global, shared, or slide-specific;
- whether slide size is fixed, viewport-based, or content-driven;
- repeated components, templates, and naming conventions;
- inline, embedded, and linked resources; and
- content or behavior that depends on element IDs, classes, attributes, or DOM order.

Do not rename or restructure hooks used by CSS, scripts, navigation, citations, or accessibility features unless the change requires it and all dependencies are updated together.

### CSS organization and visual system

Inspect:

- stylesheet location, cascade order, specificity, and custom properties;
- typography families, roles, sizes, weights, line heights, and line lengths;
- grids, alignment, spacing, margins, and viewport assumptions;
- colors, semantic color roles, contrast, borders, shadows, and gradients;
- shared slide layouts and intentional exceptions;
- breakpoints, container rules, overflow behavior, and print styles; and
- duplicated or conflicting rules that may make a local fix unsafe.

Determine whether a problem is caused by a shared token, component rule, slide-specific override, or content structure before choosing where to edit.

### Behavior and media

Inspect:

- navigation controls, keyboard shortcuts, deep links, and slide state;
- hover, focus, click, touch, expansion, tabs, tooltips, and animation;
- reduced-motion behavior;
- charts, their underlying values, axes, labels, scales, legends, and annotations;
- images, captions, alternative text, sizing, cropping, and loading behavior;
- citations, footnotes, source links, and any reveal mechanism; and
- fallbacks or initial states when scripts do not run or interaction has not occurred.

Record existing working behavior that must survive the edit. A visual change can unintentionally break behavior when it changes stacking, pointer events, visibility, overflow, focus order, or DOM structure.

### Responsive and accessibility behavior

Check representative desktop and small-screen widths, as well as keyboard use and enlarged text. Inspect:

- intentional column reflow and reading order;
- page-level and component-level overflow;
- fixed heights, absolute positioning, clipping, and overlap;
- navigation placement and touch target usability;
- semantic headings, landmarks, lists, tables, figures, and controls;
- accessible names, alternative text, focus order, and visible focus states;
- contrast and non-color cues; and
- whether hover-only or motion-dependent content remains available through other means.

## 2. Identify the user's requested change

Classify the request before planning edits. It may involve:

- visual styling;
- typography;
- color or theme;
- layout;
- readability;
- responsive or mobile behavior;
- interactions;
- charts;
- accessibility;
- structure or content; or
- a clearly related combination of these.

Translate the request into observable outcomes. For example, “improve mobile” may mean eliminating page-level horizontal overflow, stacking a comparison in a sensible order, keeping controls usable, and preserving readable type—not redesigning the desktop deck.

Separate required changes from opportunities noticed during inspection. Fix an adjacent issue only when it is necessary for the requested change, prevents a clear regression, or the user explicitly includes broader improvement in scope.

## 3. Diagnose the cause

For each requested outcome, identify:

- the specific slides, components, selectors, markup, or scripts involved;
- whether the issue is global or local;
- the source of the current behavior;
- which existing behaviors and content must remain unchanged;
- the smallest safe edit surface; and
- likely regression risks at other slides or viewport sizes.

Prefer fixing a shared cause when the issue is genuinely shared. Prefer a scoped override or local structural adjustment when changing the shared system would alter correct slides.

Do not mask a structural problem with arbitrary offsets, repeated overrides, or shrinking content until it fits.

## 4. Apply the minimal-change principle

Preserve everything that does not need to change.

- If the user asks to change colors, do not rewrite the narrative.
- If the user asks to improve mobile layout, do not redesign the desktop presentation unnecessarily.
- If the user asks to change typography, do not remove or replace working interactions.
- If the user asks to improve readability, preserve source meaning while improving hierarchy, grouping, measure, spacing, and density.
- If the user asks to improve a chart, preserve its underlying data and analytical meaning.
- If the user asks to change one slide, do not restyle the entire deck unless the requested result requires system-wide consistency.

When a deeper structural change is necessary, make the smallest coherent structural change that solves the problem. Update dependent selectors, scripts, navigation, ARIA relationships, citations, and responsive rules together. Do not partially migrate a component into an inconsistent state.

## 5. Review the design in context

Evaluate affected areas against:

- typography;
- hierarchy;
- whitespace;
- alignment;
- density;
- composition;
- color and contrast;
- consistency;
- useful versus harmful repetition;
- responsiveness;
- accessibility; and
- interaction clarity.

Use [editorial-design-system.md](editorial-design-system.md) as the design standard. Adapt it to the existing presentation and the user's request; do not blindly apply every rule or erase intentional visual identity.

The purpose of the review is to select relevant improvements, not to manufacture reasons for a complete redesign.

## Common editing decisions

### Typography

- Strengthen heading, body, label, and citation hierarchy.
- Improve body size, line height, and reading measure.
- Reduce font variation only where it weakens consistency or hierarchy.
- Preserve emphasis that communicates meaning.
- Fix wrapping, clipping, overflow, and awkward content constraints at their cause.
- Verify type changes across long titles, dense slides, controls, charts, and small screens.

Do not reduce type to make an overloaded slide fit. Reorganize, progressively disclose, or split content when the user's scope permits it.

### Layout and spacing

- Align elements to an intentional grid or shared edges.
- Increase or reduce spacing according to content relationships.
- Reduce crowding while preserving necessary information.
- Strengthen the reading order through position, scale, grouping, and whitespace.
- Replace fragile absolute positioning when it causes overlap or prevents reflow.
- Prevent clipped content and page-level horizontal overflow.

Do not center every element as a shortcut to alignment. Do not wrap all content in cards merely to create separation.

### Mobile and responsive behavior

- Reflow layouts intentionally rather than uniformly scaling the desktop canvas.
- Stack or reorganize columns in the correct reading order.
- Allow content-bearing slides to grow vertically when needed.
- Adjust typography within readable bounds rather than shrinking it indiscriminately.
- Keep navigation, controls, charts, and citations usable on touch devices.
- Maintain sufficiently large touch targets and space between adjacent controls.
- Rework wide tables, comparisons, and diagrams into a usable small-screen treatment without hiding essential information.
- Account for sticky controls, browser chrome, and safe-area edges.

Preserve the desktop behavior when it is already correct. A mobile repair should not weaken a successful large-screen composition.

### Color and theme

- Improve text, control, chart, and focus-indicator contrast.
- Consolidate colors into a coherent, restrained palette when requested.
- Preserve colors that encode categories, status, series, or another semantic distinction.
- Use accent color consistently and meaningfully.
- Remove or reduce decorative gradients when they harm readability or conflict with the requested direction.
- Pair semantic color with text, shape, position, pattern, or another non-color cue.

When changing a semantic color, update every associated legend, label, state, and interaction consistently.

### Repetitive layouts

- Identify repeated compositions and determine whether repetition creates useful continuity or monotonous communication.
- Preserve repeated structures when they support comparison, sequence, or orientation.
- Introduce meaningful variation when a different composition better expresses the slide's information.
- Vary layout without abandoning the deck's grid, typography, navigation, or visual identity.

Do not create variation for novelty alone, and do not replace repetition with a series of unrelated visual styles.

### Interactions and motion

- Preserve working navigation and interactions unless they conflict with the request or accessibility requirements.
- Improve discoverability with clear labels, affordances, states, and instructions where needed.
- Preserve state changes and content relationships when restyling controls.
- Maintain visible hover, focus, active, selected, expanded, and disabled states as applicable.
- Ensure keyboard and touch operation remain available.
- Avoid unnecessary motion and respect reduced-motion preferences where practical.
- Keep the essential message understandable before interaction and without animation.

Do not remove a script or dependency merely because its output is not visible in the initial state. Trace its role first.

### Charts and data displays

- Preserve the correct underlying data, labels, units, periods, categories, definitions, and source.
- Improve label size, direct annotation, spacing, hierarchy, and contrast.
- Ensure axis scales and baselines do not mislead.
- Preserve consistent series identity across slides and interaction states.
- Reduce nonessential gridlines, effects, and decoration when they obstruct the comparison.
- Adapt charts responsively without hiding essential data or making labels unreadable.

Do not change factual values, derive new claims, change the analytical question, or merge distinct metrics without explicit user instruction and adequate source support.

### Accessibility

- Preserve or improve semantic structure and logical DOM order.
- Keep native control semantics where possible.
- Maintain accessible names, descriptions, expanded/selected states, and ARIA relationships.
- Preserve meaningful alternative text and captions.
- Maintain visible focus states and logical keyboard order.
- Ensure interaction instructions do not depend only on hover, color, or visual position.
- Verify that zoom and text enlargement do not cause clipping, overlap, or loss of functionality.

Do not replace a working accessible component with a visually similar but non-semantic element.

## Source integrity

Never change factual content merely to improve visual appearance.

Preserve:

- numbers and signs;
- units, currencies, and scale;
- dates and reporting periods;
- definitions, denominators, and calculation methods;
- citations and source attribution;
- reported, adjusted, constant-currency, GAAP, non-GAAP, and other financial distinctions;
- qualifiers, assumptions, uncertainty, ranges, and limitations; and
- actual, estimated, and forward-looking status.

Keep citations attached to the claims and values they support. When moving or splitting content, move its relevant provenance with it and retain working citation links or reveal behavior.

If the requested design change conflicts with factual or source integrity, preserve the factual content. Implement the compatible portion of the request and explain the limitation rather than silently altering meaning.

## 6. Plan and edit

Before editing, make a concise plan that identifies:

- the requested outcome;
- the affected slides and shared components;
- the specific markup, CSS, or behavior that must change;
- the content and functionality that must remain unchanged;
- expected desktop and small-screen behavior; and
- the validations needed to detect regressions.

Apply focused edits. Follow existing naming, organization, formatting, and implementation patterns unless those patterns cause the issue being fixed. Avoid adding dependencies or a new architecture to solve a local problem.

After each coherent change, review the affected behavior and nearby shared consumers. If the edit causes a regression, repair it within the original scope rather than expanding into an unrelated redesign.

## 7. Validate and visually review

Validation must cover both code behavior and the rendered presentation.

### Functional validation

Confirm that:

- the document still opens as intended;
- navigation reaches the correct slides and states;
- keyboard shortcuts and controls still work;
- tabs, expansions, tooltips, charts, and other interactions still work;
- deep links, anchors, citations, and source links still resolve;
- no referenced asset or selector was accidentally broken; and
- no new runtime error was introduced.

### Visual review

Review the edited presentation at representative desktop and mobile sizes. Inspect the changed slide, shared components, and enough neighboring slides to detect system-wide regressions.

Confirm that:

- the requested visual outcome is apparent;
- text remains readable and follows a clear hierarchy;
- content is not clipped;
- elements do not overlap;
- page-level horizontal overflow does not exist;
- stacked content follows a sensible reading order;
- navigation and controls do not cover content;
- charts, images, tables, and citations remain legible; and
- focus, hover, active, and expanded states remain visually clear.

Test unusually long titles, dense content, enlarged text, and the smallest supported viewport when they could expose the edited rule's limits.

## 8. Repair and repeat

When validation finds a regression:

1. Identify whether it comes from the new edit or a pre-existing condition exposed by it.
2. Repair the narrowest cause that is within scope.
3. Repeat the relevant functional and visual checks.
4. Stop expanding the edit once the requested outcome and required safeguards pass.

Do not declare success because the source code looks plausible. The rendered behavior is the result that matters.

## Final quality check

Before delivering the edited presentation, verify:

- the requested changes were actually made;
- unrelated content, styling, and behavior were preserved;
- any structural change was necessary and limited to the smallest coherent scope;
- navigation still works;
- interactions still work with pointer, keyboard, and touch where applicable;
- citations and source links still work and remain attached to the correct content;
- numbers, units, dates, definitions, financial distinctions, and qualifiers remain accurate;
- desktop and responsive behavior work as intended;
- typography remains readable;
- contrast and visible focus states remain sufficient;
- no content is clipped;
- no elements overlap;
- no page-level horizontal overflow exists;
- accessibility has not regressed; and
- the edited result remains consistent with the broader editorial design, interaction, accessibility, and source-integrity standards.

If a check fails, repair and retest before delivery.
