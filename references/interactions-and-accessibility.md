# Level 2 interactions and accessibility

Use this reference when deciding whether and how to add interaction to an HTML presentation. Level 2 interaction provides focused exploration or progressive detail without turning the presentation into a complex application.

## Core principle

Interaction must improve understanding. Never add it merely to make a presentation feel more impressive.

The initial state must communicate the slide's primary message. Interaction may reveal context, comparisons, evidence, definitions, citations, or sequence, but it must not be required to discover what the slide is fundamentally saying.

Prefer a clear static composition when interaction would add effort without adding comprehension.

## Supported Level 2 interactions

Use only interactions that match a communication need:

- hover and focus states;
- tooltips;
- expandable or collapsible details;
- progressive disclosure;
- tabs;
- clickable diagrams;
- interactive charts;
- highlighted or selected states;
- animated processes;
- clickable presentation navigation;
- source or citation popovers; and
- contextual detail panels.

This list describes available patterns, not a requirement to use them. A presentation may need only navigation.

## Interaction decision test

Before adding any interaction, answer:

1. What information problem does it solve?
2. Would the slide be clearer without it?
3. Is important information being hidden?
4. Can keyboard users discover and operate it?
5. Can touch users discover and operate it?
6. Does it preserve meaning with reduced motion?
7. Does the initial state preserve the slide's primary message?

Add the interaction only when the answers show clear communication value. If a static label, annotation, sequence, table, or additional slide communicates more directly, use that instead.

## Shared interaction requirements

Every interactive component must:

- have a visible, understandable control or affordance;
- use concise labels that describe the action or destination;
- be reachable and operable without a mouse;
- provide visible hover, focus, active, selected, expanded, and disabled states when applicable;
- communicate state with more than color alone;
- preserve a logical reading and focus order;
- work at touch sizes without tightly packed targets;
- avoid page-level horizontal overflow when opened or updated;
- keep its state visually connected to the content it controls;
- avoid obscuring primary content or navigation;
- remain understandable before interaction; and
- fail safely whenever practical.

Do not make a decorative image, icon, label, or entire container appear interactive unless it performs a meaningful action.

## Hover and focus states

Hover may reinforce discoverability, but it cannot be the only way to reveal or operate content.

- Give keyboard focus the same information and functional access offered by hover.
- Provide click or tap activation when the content must remain available on touch devices.
- Keep focus indicators visible against every background and state.
- Do not move controls on hover in a way that changes the hit target or causes layout shift.
- Avoid hover effects on noninteractive elements when they could imply clickability.
- Ensure pointer hover does not dismiss content while the pointer moves from a trigger into an interactive popup.

Anything available on hover must also be available through keyboard focus or click/tap.

## Tooltips

Use a tooltip for short, optional context such as:

- a concise term definition;
- an exact chart value or brief annotation;
- a compact source summary; or
- a short explanation of a label.

Do not place essential information only in a tooltip. Use visible content, an expandable section, a detail panel, or another persistent form when the explanation is long, interactive, necessary for interpretation, or contains several links.

### Tooltip behavior

- Use a real button when the tooltip is intentionally opened or closed. A naturally focusable data point may also serve as a trigger when its role is clear.
- Open on focus as well as hover when hover behavior is provided.
- Support click or tap when touch access is needed.
- Associate the trigger and tooltip with an appropriate semantic relationship when native semantics are insufficient.
- Keep the tooltip within the viewport and prevent it from covering the trigger or essential content where practical.
- Allow dismissal without forcing the user to move focus unpredictably.
- Keep wording brief enough to scan without a complex internal layout.

Do not make users chase moving tooltips or rely on precise pointer placement.

## Expandable and collapsible details

Use expandable content when supporting material is useful but not required for first-pass understanding, including:

- methodology or definitions;
- detailed evidence;
- citations and caveats;
- examples; or
- optional implementation detail.

The collapsed state must still communicate the primary message and any qualification required to interpret it accurately.

### Expansion behavior

- Prefer native `details` and `summary` when their behavior and semantics fit.
- Otherwise use a `button` whose label names the content and whose expanded state is communicated.
- Keep the control next to the content it reveals.
- Use labels such as “Show methodology” or “Hide methodology,” not vague labels such as “More.”
- Keep revealed content in the logical reading order.
- Do not collapse content merely to make an overloaded slide appear sparse.
- Ensure expansion reflows the slide without clipping, overlap, or page-level horizontal overflow.

## Tabs

Use tabs when multiple related views occupy the same conceptual space, such as:

- categories or segments;
- scenarios;
- perspectives;
- time periods; or
- alternate but equivalent views of the same evidence.

Do not use tabs merely to hide overcrowded or unrelated content. If the audience needs to compare views simultaneously, use an aligned comparison or separate slides instead.

### Tab behavior

- Give every tab a concise, unique label.
- Identify the active tab through more than color, such as weight, underline, border, icon, or shape.
- Associate every tab with exactly one tab panel and every panel with its controlling tab.
- Keep tab order consistent with panel order.
- Make the tab list keyboard reachable.
- Support arrow-key movement between tabs when practical, with activation behavior applied consistently.
- Support Enter or Space when activation is not automatic.
- Keep focus visible and do not reset it unexpectedly after a view change.
- Ensure inactive panels are not exposed as duplicate content to assistive technology.
- Preserve the essential conclusion outside the tabs or make it clear in the initially selected view.

Do not place so many tabs in one row that labels become tiny or overflow. Recompose the control for smaller screens.

## Progressive disclosure

Use progressive disclosure when sequence improves understanding, for example to:

- reveal process stages;
- introduce components of a framework;
- build an argument step by step;
- add layers to a diagram; or
- progressively reveal supporting evidence.

Each state must add a meaningful unit of understanding. The final state should read as a complete composition rather than a pile of accumulated effects.

- Provide an obvious way to advance and, when useful, return to an earlier state.
- Show position or progress when the number of stages is not otherwise clear.
- Keep previously revealed information visible only when it helps the next step; avoid uncontrolled visual accumulation.
- Ensure the same content can be reached by pointer, keyboard, and touch.
- Do not time advances automatically when the audience needs time to read.
- With JavaScript unavailable, expose the essential content in a logical static order whenever practical.

## Clickable diagrams

Use a clickable diagram when the audience needs both an overview and component-level detail and when relationships between multiple meaningful parts matter.

- Keep the overview comprehensible before selection.
- Make interactive regions visually discoverable and large enough to operate.
- Use actual buttons or links, including within SVG when appropriate, rather than attaching behavior only to generic containers.
- Provide accessible names that identify each component.
- Make the selected component obvious through at least two cues, such as border plus label, weight plus shape, or icon plus contrast.
- Keep the detail panel close to the diagram and clearly identify which component it describes.
- Preserve a logical focus order between diagram controls and detail.
- Provide a readable linear alternative when the spatial relationship cannot translate directly to small screens.

Do not make decorative graphics clickable. Do not invent relationships, sequence, or causality to justify a diagram.

## Interactive charts

Use chart interaction only when it helps the audience:

- inspect exact values;
- compare series;
- highlight categories;
- reveal relevant annotations;
- switch between meaningful views; or
- explore useful secondary detail.

A static chart is preferable when it communicates the message more clearly. Do not turn a simple number or straightforward comparison into an interactive chart.

### Chart interaction behavior

- State the main insight visibly before interaction.
- Keep axes, units, periods, categories, and necessary qualifiers visible.
- Make data points or series reachable without requiring pixel-precise pointer control.
- Provide keyboard and touch alternatives to hover inspection.
- Show selected or highlighted series with more than color alone, using direct labels, stroke, weight, pattern, or de-emphasis of other series.
- Preserve a consistent series identity between views and states.
- Prevent filtering or view switching from silently changing units, denominators, definitions, or time periods.
- Announce meaningful state changes when the visible update would otherwise be unavailable to assistive technology.
- Keep exact values and source information traceable.
- Provide a readable table or textual alternative when the chart cannot expose its information accessibly.

Interaction must not change the underlying data or imply unsupported analysis.

## Highlighted and selected states

Use highlighting to focus attention on an existing relationship, not to decorate arbitrary elements.

- Preserve enough surrounding context to understand what is highlighted.
- Use a stable selected state rather than hover alone when the audience needs time to inspect detail.
- Communicate selection with multiple cues.
- Ensure de-emphasized content remains legible when it is still relevant.
- Provide a clear way to reset the view when several selections are possible.

## Citation and source interactions

Compact citation markers may provide source detail without crowding the main composition.

A useful pattern is:

```text
Hover or focus → show a short source summary
Click or activate → reveal fuller source details
```

Source detail may include:

- source title;
- page, section, table, or figure;
- reporting period;
- metric definition;
- author or organization;
- publication date; and
- URL when available.

### Citation behavior

- Keep the marker adjacent to the claim, value, chart, or quotation it supports.
- Use a meaningful accessible label such as “Source for revenue growth,” not only a numeral or icon name.
- Make the compact summary available on focus as well as hover.
- Make fuller details reachable by keyboard and touch.
- Keep the source text selectable and links operable.
- Return focus to the triggering marker when a dismissible popover closes.
- Prevent popovers from obscuring the claim, overflowing the viewport, or covering presentation navigation.
- Preserve traceable source information even when interaction is unavailable; visible source notes or an accessible source list are valid fallbacks.

Do not use a citation popup to hide a qualification that must remain visible for the claim to be accurate.

## Contextual detail panels

Use a detail panel when one stable region can explain selections from a chart, diagram, map, or comparison.

- Give the panel a clear heading tied to the selected item.
- Update all related labels and state indicators together.
- Keep the panel in a predictable position and reading order.
- Announce substantial content changes when needed.
- On small screens, place the panel immediately after its controlling content rather than forcing a distant side-by-side layout.
- Provide an understandable default or empty state.

## Navigation

Presentation navigation is functional interaction and must remain predictable.

- Use labeled buttons or links for next, previous, section, and direct-slide navigation.
- Communicate the current slide and overall progress.
- Disable unavailable previous or next actions rather than letting them fail silently.
- Support the documented keyboard commands without interfering with typing, native controls, or assistive technology commands.
- Keep navigation controls reachable, visible, and clear of slide content.
- After a slide change, keep focus predictable and ensure the active slide is available to assistive technology while inactive slides are not read as duplicate visible content.
- Do not make swipe gestures the only navigation method.

## Motion and animated processes

Use motion only to explain:

- sequence;
- change;
- hierarchy;
- cause and effect; or
- a transition between meaningful states.

Keep motion short, restrained, and subordinate to the content. The audience must control the pace when reading or analysis is involved.

Avoid:

- bouncing or spinning;
- unnecessary parallax;
- constant looping animation;
- excessive entrance animation;
- motion applied to every element;
- long transitions that delay access; and
- animation whose direction or timing implies an unsupported relationship.

Use opacity, emphasis, or short spatial transitions only when they help explain the state change. Do not animate merely to make a slide feel active.

## Reduced motion

Respect `prefers-reduced-motion`.

When reduced motion is requested:

- remove nonessential transitions;
- remove animated movement and parallax;
- stop automatic or looping animation;
- show state changes immediately or with a minimal nonmoving treatment;
- preserve control, selection, progress, and expanded/collapsed states; and
- ensure no meaning is lost.

Do not remove the underlying interaction merely because its animation is disabled. The state change must still occur and remain visually clear.

## Keyboard accessibility

Interactive controls must:

- be reachable in a logical order;
- have visible focus states on every background;
- use Enter and Space where expected for their semantic role;
- support arrow-key behavior for composite components such as tabs when practical;
- expose current, expanded, selected, checked, or disabled state when applicable; and
- avoid keyboard traps.

Prefer native keyboard behavior. Do not add global shortcuts that override typing, browser commands, screen-reader commands, or focused controls. If a popup, panel, or modal-like component moves focus, return focus predictably when it closes.

## Semantic HTML

Prefer native elements whose meaning and behavior match the component:

- `button` for actions;
- `a` for navigation to a destination;
- `nav` for navigation groups;
- `section` for slides or meaningful regions;
- `figure` and `figcaption` for charts, diagrams, and their captions;
- `details` and `summary` for simple disclosure;
- headings for content hierarchy; and
- tables for genuinely tabular data.

Avoid using generic `div` or `span` elements as controls when a native element is appropriate. Do not recreate native behavior with JavaScript without a clear need.

## ARIA

Use ARIA only when semantic HTML is insufficient. Native semantics are preferable because incorrect ARIA can make a component less accessible.

When ARIA is needed:

- give controls meaningful accessible names;
- communicate expanded or collapsed state;
- communicate selected, current, checked, or disabled state as applicable;
- connect controls to the content they operate;
- connect tabs to panels, citations to detail, and labels to charts or diagrams;
- keep ARIA state synchronized with the visible state; and
- avoid adding roles that conflict with native elements.

Do not add redundant labels or landmark roles. Do not use ARIA as a substitute for keyboard behavior, focus management, readable text, or semantic structure.

## Color and state

Never communicate an interactive state through color alone. Combine color with at least one other perceivable cue, such as:

- border;
- weight;
- icon;
- text label;
- position;
- shape; or
- underline.

Maintain sufficient contrast for controls, labels, focus indicators, selected states, disabled states, and content revealed by interaction. A disabled state may be muted but must remain identifiable.

## Touch behavior

- Make controls large enough to activate reliably and leave adequate space between adjacent targets.
- Do not require hover, right-click, or a precision gesture.
- Keep controls reachable without covering primary content or device safe areas.
- Ensure expanded content and popovers remain within the viewport.
- Recompose dense horizontal controls for narrow screens rather than shrinking labels.
- Preserve an explicit control for any gesture-based action.

Test touch behavior conceptually as a different input mode, not as mouse behavior on a smaller screen.

## Fail-safe behavior

If JavaScript fails or an interaction is unavailable, the audience should still understand the essential message whenever practical.

- Put primary claims, required qualifiers, and critical values in the initial HTML.
- Use semantic source order so content remains intelligible without visual repositioning.
- Prefer native disclosure when it provides a suitable no-script behavior.
- Provide visible or linear alternatives for essential chart, diagram, and source content.
- Do not leave blank regions or controls that appear functional when their content cannot load.
- Keep navigation-independent access possible when the delivery context permits scrolling through slides.

Progressive enhancement is the preferred model: begin with understandable content, then add useful behavior.

## Interaction quality check

Before finalizing an interactive presentation, verify:

- every interaction solves a specific information or navigation problem;
- the initial state communicates each slide's primary message;
- controls are visually discoverable and meaningfully labeled;
- keyboard navigation and expected Enter, Space, or arrow-key behavior work;
- focus order is logical and focus states remain visible;
- touch controls work without hover or precision pointing;
- reduced-motion behavior preserves all meaning and state changes;
- no essential information is available only on hover;
- selected, expanded, and current states use more than color alone;
- tooltips, popovers, panels, and expanded content remain within the viewport;
- interactions do not cause clipping, overlap, or page-level horizontal overflow;
- citations remain attached to claims and traceable to their sources;
- chart interaction preserves data, units, periods, definitions, and qualifiers;
- interactive content remains readable;
- semantic HTML is used where practical and ARIA is limited to genuine gaps;
- interaction failure leaves the essential message available whenever practical; and
- no motion or interaction exists solely for decoration.

If an interaction fails any check, simplify, repair, replace, or remove it before delivery.
