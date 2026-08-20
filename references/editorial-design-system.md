# Editorial design system

Use this reference when choosing the visual language, composition, typography, and responsive behavior of an HTML presentation. The goal is a premium editorial web experience that still reads and navigates like a presentation—not a dashboard, document facsimile, or collection of generic cards.

## Core standard

Design every presentation around comprehension. A viewer should recognize the main point of a slide within a few seconds, understand the intended reading order, and be able to explore supporting detail without losing context.

- Prioritize readability above decoration or novelty.
- Restructure source material around presentation logic; do not reproduce the source page by page.
- Give each slide one primary communication goal.
- Use a consistent underlying system while varying compositions to fit the information.
- Use visual elements only when they carry meaning, establish hierarchy, or aid navigation.
- Preserve source facts. Never invent information to complete a composition or make it appear more persuasive.

## Design decision sequence

For each slide, make decisions in this order:

1. State the single idea the viewer should retain.
2. Identify the evidence or context needed to support that idea.
3. Choose the simplest composition that communicates the relationship.
4. Establish a clear reading order through hierarchy and placement.
5. Remove, split, or progressively disclose secondary material that crowds the slide.
6. Check the composition at desktop and small-screen widths.
7. Remove any element that has no communication purpose.

Do not begin by choosing a decorative layout and forcing content into it.

## Typography

Typography may be the primary visual material. It should create hierarchy and character without compromising reading comfort.

### Typeface system

- Prefer one primary typeface. Add at most one supporting typeface only when it has a clear role, such as separating editorial display text from utilitarian labels.
- Prefer system or broadly available fonts when a presentation must remain truly standalone. Do not depend on a remote font unless the delivery requirements explicitly permit external assets.
- Assign stable roles to typefaces and do not switch families arbitrarily between slides.
- Limit weights and styles to those needed for hierarchy. In most cases, regular plus one emphasized weight is sufficient.
- Avoid decorative faces for body copy, data labels, controls, citations, and other functional text.

### Hierarchy

Use a small, repeatable set of roles rather than styling each text block independently:

- Display: the principal statement or section-opening idea.
- Slide title: the slide's topic or conclusion.
- Deck or standfirst: a short explanatory introduction.
- Body: supporting prose written for continuous reading.
- Label: eyebrow, category, navigation, or chart annotation.
- Caption/source: provenance or secondary context that must remain legible.

Create distinction first through scale, spacing, placement, and weight. Use color or typeface changes only when those signals add meaning.

### Readability rules

- Never use tiny body text or tiny chart labels to fit more content.
- Choose fluid, responsive type sizes with sensible minimum and maximum values rather than scaling all text in proportion to the viewport.
- Keep ordinary body text around 45–75 characters per line. Use narrower measures for large display text and wider measures only for compact data tables where necessary.
- Use comfortable line height: approximately 1.4–1.7 for body copy and tighter spacing for large headings when letterforms remain clear.
- Break long passages into meaningful paragraphs, annotations, pull quotes, or additional slides. Do not convert every paragraph into bullets.
- Keep labels concise and visually distinct, but not so small or faint that they become difficult to read.
- When oversized elements—including percentages, large numbers, financial figures, statistics, KPI displays, hero metrics, oversized headings, and large chart annotations—are paired with supporting labels, captions, descriptions, or footnotes, reserve explicit visual space for the oversized element before placing the supporting text. Supporting text must never visually collide with or compete against the oversized element; prefer layout and spacing fixes before reducing its type size.
- Prevent widows, awkward single-word lines, and dense all-caps passages where practical.

## Layout and spatial system

### Grid and alignment

- Establish a consistent content grid with stable outer margins and a small number of reusable columns.
- Align elements to shared edges or baselines. Intentional exceptions may create emphasis; accidental near-alignments create noise.
- Use generous outer margins and internal spacing. Increase space between unrelated groups and reduce it within related groups.
- Treat whitespace as structure: it should establish rhythm, emphasis, grouping, and pauses between ideas.
- Do not center everything by default. Left-aligned text is usually easier to scan; centered alignment is appropriate for concise hero statements, transitions, or deliberate ceremonial moments.
- Use asymmetric layouts when they improve emphasis, narrative movement, or the relationship between text and evidence.

### Slide boundaries

- A slide should feel complete at its intended viewing size, but content must never be clipped to preserve a fixed canvas.
- Do not force every source detail onto one slide. Split the argument when the evidence cannot remain readable.
- On large screens, sections may occupy the viewport to create presentation pacing.
- On small screens or with enlarged text, allow sections to grow vertically and the page to scroll. Content integrity takes priority over fixed-height slides.
- Keep navigation and essential controls clear of content and safe-area edges.

## Information density

- Give every slide one primary communication goal and subordinate all other elements to it.
- Preserve important information while changing its structure, grouping, sequence, or placement.
- Reorganize dense material into a sequence, focused comparison, annotated graphic, expandable detail, or additional slide. Never solve overcrowding by shrinking type to an unreasonable size.
- Separate the headline conclusion from its supporting evidence. The evidence should remain discoverable without competing equally for attention.
- Use progressive disclosure when secondary detail is valuable but would obstruct the first reading. The initial state must still communicate the essential point.
- Prefer concise prose when a sentence communicates better than fragments. Use bullets only for genuinely parallel, scannable items.
- For tables, retain the rows and columns needed for the argument, emphasize the relevant comparison, and provide access to important detail rather than compressing everything into illegibility.

## Visual hierarchy

A viewer should understand what matters most within a few seconds. Establish an intentional first, second, and third reading level through:

- **Scale:** Make the primary idea unmistakably more prominent than supporting detail.
- **Position:** Place important content where the reading path reaches it early.
- **Whitespace:** Isolate key ideas and separate unrelated groups.
- **Contrast:** Distinguish importance while maintaining readable text and backgrounds.
- **Typography:** Use stable roles, size, and weight to signal function.
- **Grouping:** Place related evidence together and label the relationship clearly.
- **Sequence:** Reveal or arrange content in the order needed to understand it.

Do not rely on every hierarchy signal at once. A restrained combination is usually stronger than excessive emphasis.

## Choosing a composition

Choose the composition from the information, not from a desire for variety alone. Across a deck, vary scale, density, alignment, and media placement enough to create rhythm without abandoning the shared grid and type system.

- **Hero statement:** Use for a concise thesis, opening, or decisive takeaway.
- **Big number:** Use when one verified figure is the message. Include its unit, period, context, and source; use a chart only if change or comparison matters.
- **Editorial text:** Use for a short argument, explanation, or narrative passage with a disciplined reading measure.
- **Quote:** Use only when the speaker and exact wording matter. Identify the speaker and source.
- **Comparison:** Use aligned columns, a shared baseline, or another direct structure that makes differences easy to scan.
- **Timeline:** Use when chronology or change over time is essential. Keep intervals and ordering accurate.
- **Process:** Use when stages, dependencies, or handoffs are the point; clearly indicate direction.
- **Framework:** Use for a named conceptual structure whose parts and relationships are supported by the source.
- **Matrix:** Use only when two meaningful dimensions reveal a useful relationship. Label both axes explicitly.
- **Chart:** Use when shape, change, distribution, or comparison is clearer visually than in prose or a single number.
- **Table:** Use when exact values or several aligned comparisons matter more than visual pattern.
- **Diagram:** Use when structure, flow, hierarchy, or causality cannot be explained as clearly with simple prose.
- **Image-led composition:** Use when an image is evidence, subject matter, or meaningful context—not generic decoration.
- **Case study:** Combine situation, action, and outcome with enough evidence to keep the story credible.
- **Transition or section divider:** Use sparingly to orient the viewer and reset pacing.
- **Closing slide:** Reinforce the final takeaway, decision, or next step rather than merely repeating the title slide.

Do not turn every slide into a card grid. Cards are appropriate only when they express a real set of discrete, peer-level items. Avoid repeating the same composition on consecutive slides unless repetition communicates a deliberate comparison or sequence.

## Color

- Use a restrained palette: a readable foreground and background, a small neutral range, and a limited set of purposeful accents.
- Prioritize text/background contrast over brand subtlety or visual mood.
- Assign accent colors stable meanings, such as emphasis, category, status, or series identity. Do not apply accents randomly.
- Use large fields of color selectively to mark sections, shifts in tone, or emphasis.
- Do not use gradients merely for decoration. A gradient is acceptable only when it encodes a meaningful continuum or serves a necessary image treatment without reducing readability.
- Do not rely on color alone for important distinctions. Pair it with text, shape, position, pattern, or another perceivable cue.
- Verify chart colors against the slide background and against one another. Labels and direct annotation are preferable to an ambiguous legend when space allows.

## Meaningful visual elements

- Use charts, images, diagrams, rules, shapes, and icons only when they explain, organize, compare, orient, or provide evidence.
- Prefer direct labels and annotations over decorative legends or ornamental callouts.
- Use a simple number instead of a chart when the number alone communicates the point.
- Avoid generic decorative illustrations unless the user explicitly requests them and they contribute to the narrative.
- Do not add visual filler to occupy whitespace. Empty space is preferable to meaningless decoration.
- Keep corner radii, shadows, borders, and containers restrained. Group with alignment and spacing before adding a card.

## Interaction and motion

- Add interaction only when it clarifies information, supports navigation, or gives optional access to useful detail.
- Use tabs, expansion, tooltips, highlighting, filtering, or animated diagrams only when the interaction matches the content relationship.
- Make the essential message understandable before interaction. Hidden content may add depth but must not contain the only expression of the slide's primary point.
- Give interactive elements clear labels, visible states, and an obvious response to hover, focus, and activation.
- Keep motion brief and purposeful. Do not animate merely to make a slide feel active.
- Respect reduced-motion preferences where practical by disabling or simplifying nonessential transitions.
- Do not let motion delay access to information or prevent users from navigating at their own pace.

Detailed behavior belongs in `interactions-and-accessibility.md`; this section defines the visual standard interactions must satisfy.

## Responsive behavior

Treat responsive design as recomposition, not uniform shrinking.

- Test at representative desktop and small-screen widths and at increased text sizes.
- Never allow page-level horizontal overflow.
- Reflow multi-column layouts into a deliberate vertical sequence that preserves reading order.
- Move supporting annotations near the content they describe when columns stack.
- Convert wide comparisons, tables, charts, and diagrams into a readable small-screen treatment. This may require stacking, focusing on subsets, or providing controlled local scrolling with clear affordances; do not clip them.
- Keep body text, labels, chart annotations, controls, and tap targets usable on small screens.
- Avoid fixed pixel heights for content-bearing regions. Use viewport-sized presentation framing only when content can still expand safely.
- Give persistent presentation UI—including navigation, progress indicators, fullscreen controls, and other floating controls—a defined safe area at desktop, tablet, and mobile sizes. Reserve layout space for this UI; it must never overlap slide content, tables, charts, citations, source notes, or other meaningful information.
- Preserve the hierarchy of the desktop design rather than making every element equally prominent after stacking.

## Accessibility baseline

- Maintain strong text/background contrast, including secondary text, chart labels, controls, and focus indicators.
- Use semantic HTML where practical so headings, sections, figures, tables, quotations, and controls retain meaning beyond their visual styling.
- Use a logical heading structure and DOM order that matches the intended reading order.
- Do not communicate important meaning only through color, hover, animation, or spatial position.
- Maintain visible focus states with sufficient contrast; do not remove outlines without an equally clear replacement.
- Make controls understandable and operable by keyboard. Use native elements when they provide the required behavior.
- Ensure hover-revealed information is also available through focus and activation, and remains accessible on touch devices.
- Provide useful text alternatives for meaningful images and accessible names for controls. Treat decorative images as decorative in markup.
- Support zoom and text enlargement without clipping, overlap, or loss of functionality.

## Prohibited anti-patterns

Never:

- use excessive gradients;
- use excessive rounded cards or a six-card grid as the default solution;
- use tiny text, chart labels, citations, or controls;
- add generic decorative illustrations without a communication purpose;
- center everything by default;
- use unnecessary typefaces, weights, or styles;
- sacrifice readability for novelty;
- use a chart when a simple number is clearer;
- add decorative elements with no meaning;
- repeat the same slide layout throughout the presentation;
- turn every paragraph into bullet points;
- blindly copy the source document's page structure;
- clip or overlap content;
- permit page-level horizontal overflow;
- create interactions that are inaccessible or required to understand an otherwise hidden primary message; or
- invent information, numbers, imagery presented as evidence, sources, or citations to make a slide look better.

## Reference inspiration

Draw principles—not branding, assets, or copied layouts—from these references:

- **Purpose Talent:** editorial typography, generous whitespace, intentional composition, and web-native visual storytelling.
- **IBM 2025 Annual Report:** restrained visual language, strong hierarchy, careful handling of dense information, and clear presentation of financial data.

The generated presentation must develop its own visual system appropriate to its subject, audience, source material, and delivery context.

## Slide-level review

Before accepting a composition, confirm:

- The slide has one clear primary communication goal.
- The first reading path is apparent within a few seconds.
- Type remains comfortably readable at the intended size.
- Line lengths, spacing, contrast, and grouping support comprehension.
- Every visual and interactive element has a communication purpose.
- The composition differs from neighboring slides when the content calls for a different treatment.
- Source information remains accurate and sufficiently complete.
- The small-screen version reflows intentionally without clipping, overlap, or page-level horizontal overflow.
- The slide remains understandable without hover, animation, or optional interaction.
