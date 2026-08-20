# Final presentation quality checklist

Use this mandatory quality gate for every newly generated or edited HTML presentation.

## Core principle

Never deliver a presentation immediately after generation or editing. Always complete this cycle:

```text
Generate or edit HTML
  → Validate
  → Render desktop/tablet/mobile
  → Inspect
  → Repair
  → Revalidate
  → Rerender
  → Final quality gate
  → Deliver
```

Evaluate the complete presentation as a narrative and interactive experience, not only a collection of individually acceptable slides. A deck can fail because of its sequence, repetition, pacing, or inconsistency even when each slide appears reasonable in isolation.

Record material issues and their disposition during review. Do not declare a check passed based only on the intended implementation; inspect the actual output whenever the relevant behavior is observable.

## 1. Narrative quality

Review the presentation from beginning to end without focusing on styling first.

### Pass checks

- The purpose is clear early enough for the audience to orient itself.
- The sequence answers the audience's likely questions in a logical order.
- The presentation has an appropriate beginning, middle, and end when the material calls for one.
- Context appears before evidence that depends on it.
- Each slide has one primary communication goal.
- Important ideas receive enough space and evidence.
- Transitions make changes in topic, scale, time, or argument understandable.
- Redundant, weak, or off-purpose slides have been removed, combined, or moved to supporting detail.
- The conclusion follows from the evidence and resolves the presentation's governing question when appropriate.
- The final presentation is easier to understand than the original source.

### Fail conditions

- Slides appear in a random or source-page order without narrative justification.
- Multiple slides repeat the same point without adding evidence or progression.
- A conclusion is unsupported or stronger than the preceding evidence.
- Important evidence appears before the audience has the context needed to interpret it.
- Slides behave like document pages pasted into a presentation.
- Every source section becomes a slide regardless of importance.
- The deck ends without a supported conclusion, implication, decision, or appropriate close.

## 2. Content quality

### Pass checks

- Every factual statement is supported by supplied source material or clearly identified as a supported calculation.
- Facts, source interpretation, and recommendations are distinguishable.
- Definitions required to interpret claims remain available.
- Important qualifications, caveats, uncertainty, and limitations are preserved.
- Summaries retain the source's scope, certainty, direction, and meaning.
- Repetition exists only when it helps orientation, comparison, or deliberate emphasis.
- Slide copy is concise without becoming vague, fragmented, or misleading.
- Quotations are exact and attributed; paraphrases are not presented as quotations.

### Fail conditions

- Unsupported claims, conclusions, examples, or details were introduced.
- Important context or a material limitation was removed.
- A conditional claim became absolute.
- A possibility, estimate, or forecast became a fact.
- A source opinion or management assertion appears as independently verified fact.
- A shortened headline overstates the evidence.
- Content was converted mechanically into bullets instead of being meaningfully structured.

## 3. Source integrity

Verify every important claim and quantitative element against the source or its traceability record.

Check:

- numbers and signs;
- units, currency, scale, and precision;
- dates, “as of” dates, and reporting periods;
- category and series labels;
- definitions and denominators;
- assumptions, footnotes, qualifiers, ranges, and limitations;
- quotations and attribution;
- citations and source locations;
- chart, table, map, and diagram values;
- derived calculations, inputs, formulas, assumptions, and rounding; and
- financial distinctions, including GAAP versus non-GAAP, reported versus constant currency, actual versus adjusted, revenue versus ARR, quarterly versus annual, and historical versus forward-looking.

Confirm that:

- every important number is traceable to source material;
- every generated visual uses source-supported or transparently derived values;
- derived values are not presented as source-reported values;
- source disagreements were not silently reconciled;
- missing values were not invented or silently interpolated; and
- transformations did not create false comparability.

Any material source-integrity failure blocks delivery.

## 4. Readability

Inspect every slide at its intended viewing size and at smaller supported sizes.

Check:

- body typography is comfortably readable;
- headings, body, labels, annotations, controls, citations, and footnotes remain legible;
- type hierarchy is clear and consistent;
- line lengths support comfortable reading;
- line height and paragraph spacing aid scanning;
- whitespace separates unrelated material and groups related material;
- information density matches the slide's purpose;
- chart labels and legends do not require zooming;
- contrast remains sufficient on every background and state;
- no text is tiny merely to fit the slide;
- no region feels crowded, compressed, or visually noisy; and
- the primary message can be recognized within a few seconds.

When a slide is too dense, improve grouping, remove true redundancy, use appropriate progressive detail, or split the slide. Prefer restructuring over shrinking typography.

Fail readability when essential text, labels, notes, or controls cannot be read comfortably under normal viewing conditions.

## 5. Visual hierarchy

For each slide, identify:

1. What does the viewer see first?
2. What does the viewer see second?
3. Where is the supporting information?
4. Does that reading order match the intended message?

Confirm that hierarchy is created intentionally through scale, position, whitespace, contrast, typography, grouping, and sequence.

Fail when:

- everything has equal visual weight;
- the slide title competes with or obscures the main message;
- secondary labels dominate evidence;
- several elements all appear primary;
- decorative elements attract more attention than meaningful content; or
- the visual reading order conflicts with the semantic or narrative order.

## 6. Composition and deck-level visual quality

Review individual layouts and the rhythm across consecutive slides.

Check:

- the composition matches the information relationship;
- alignment follows an intentional grid;
- whitespace creates emphasis and grouping;
- the visual balance feels intentional rather than mechanically symmetrical;
- slide compositions vary when the content needs different treatment;
- repeated layouts support comparison or continuity rather than convenience;
- charts, tables, diagrams, images, or text are used only when they are the clearest form; and
- the deck retains a coherent typography, color, spacing, and navigation system.

Look specifically for excessive repetition.

Avoid:

- repeated card grids;
- identical slide structures throughout the deck;
- unnecessary boxed content;
- decorative clutter;
- centered layouts used by default; and
- forced variation that abandons consistency without improving communication.

Consistency is good. Sameness is not.

## 7. Data visualization

Review every chart, table, big number, timeline, and quantitative diagram.

Verify:

- displayed values match the source or documented calculation;
- units, denominators, currency, and precision are correct;
- dates, periods, category order, and time spacing are correct;
- scale and baseline choices do not exaggerate or conceal differences;
- the chart type answers the analytical question;
- labels and annotations are readable;
- the title states a supported insight or an accurate neutral description;
- series are identified consistently and with more than color alone when needed;
- missing values and comparability limitations are visible;
- estimates, actuals, forecasts, reported, and adjusted measures remain distinct;
- no 3D effect, perspective, area, or decorative treatment distorts the data; and
- interaction does not silently change definitions, units, periods, or denominators.

Ask for each chart: **Would a simpler presentation of the number communicate this better?**

If yes, replace the chart with a big number, direct comparison, table, or concise text. Data availability alone is not a reason to chart.

## 8. Interaction

Review every navigation control, tooltip, disclosure, tab, diagram selection, chart interaction, citation marker, popover, detail panel, and animation.

For each interaction, ask:

- Why does this interaction exist?
- Does it improve understanding, navigation, or access to useful detail?
- Is the control discoverable and clearly labeled?
- Can it be reached and operated by keyboard?
- Can it be operated by touch without hover or precision pointing?
- Is its focus state visible?
- Are selected, expanded, current, and disabled states clear without color alone?
- Does reduced-motion mode preserve the state change and meaning?
- Does the primary message remain understandable before interaction?
- Does the interaction avoid clipping, overlap, layout shift, and overflow?
- Does focus remain predictable when content opens, closes, or changes?

Exercise every interaction rather than checking markup alone. Remove interactions that provide no meaningful communication value.

## 9. Accessibility

Check:

- semantic HTML is used where practical;
- slide and document headings form a logical hierarchy;
- DOM and focus order follow the intended reading order;
- keyboard navigation reaches and operates all controls;
- focus indicators remain visible on every background;
- text, controls, charts, and state indicators have sufficient contrast;
- color is not the only indication of meaning or state;
- buttons, links, tabs, disclosures, and other controls have meaningful accessible names;
- selected, expanded, current, checked, and disabled states are exposed when applicable;
- images and visuals have appropriate text alternatives or are marked decorative;
- charts and complex diagrams provide an accessible explanation or data alternative when needed;
- reduced-motion preferences disable nonessential movement without removing meaning;
- essential content is not available only on hover;
- touch targets are usable and adequately separated; and
- zoom or text enlargement does not cause loss of content or functionality.

A component that looks accessible but cannot be operated or understood without a mouse does not pass.

## 10. Responsive design

Check at minimum:

- a representative desktop viewport;
- a tablet or medium-width viewport; and
- a mobile viewport.

Also test enlarged text when typography or fixed-height regions could create overflow.

At every size, verify:

- no page-level horizontal overflow exists;
- no text, chart, image, table, citation, or control is clipped;
- no elements overlap;
- typography remains readable;
- controls and touch targets remain usable;
- navigation remains visible and does not cover slide content;
- columns stack in a meaningful reading order;
- annotations remain connected to the content they describe;
- interactive panels, tooltips, and expanded regions remain within the viewport;
- content-bearing slides can grow vertically when necessary; and
- the hierarchy of the desktop composition survives the reflow.

Do not pass a layout that merely shrinks the desktop presentation until it fits. Small-screen layouts must reflow intentionally.

## 11. Technical quality

Run the checks appropriate to the implementation and inspect the actual standalone file.

Verify:

- the document is valid enough for target browsers to parse consistently;
- required document metadata and semantic presentation elements are present;
- JavaScript syntax is valid;
- no internal anchor, slide target, citation reference, or control relationship is broken;
- no required asset, selector, ID, or element is missing;
- no unintended external stylesheet, script, font, image, or CDN dependency exists;
- the presentation opens directly as a standalone file without a build step;
- no observable console error occurs during load or interaction;
- all navigation methods work and boundary states behave correctly;
- every interaction control performs its intended action;
- fullscreen enters and exits correctly when supported and degrades safely when unavailable;
- inactive and active slide states remain consistent; and
- no code change has broken print, fallback, or no-interaction behavior when those modes are supported.

Do not infer technical success from source inspection alone when behavior can be exercised.

## 12. Citations

Check:

- important factual claims have appropriate provenance;
- important data, quotations, charts, and derived values have source information;
- citations identify the relevant source precisely enough for verification;
- citations remain visually subordinate but readable;
- every citation can be mapped to the claim, value, series, or visual it supports;
- derived calculations identify their source inputs and calculated status;
- citation markers, links, popovers, and source panels work with keyboard and touch;
- citations do not obscure primary content or navigation;
- essential qualifications are not hidden only in citation detail; and
- moved or split content retained its correct citation.

Fail when citations are generic despite precise provenance being available, when a source does not support the associated claim, or when citation text is too small to use.

## 13. Anti-pattern scan

Explicitly inspect the full presentation for:

- excessive gradients;
- excessive rounded cards;
- tiny text, chart labels, citations, or controls;
- generic decorative illustrations without a communication purpose;
- six-card grids or card grids used as the default composition;
- excessive centered layouts;
- too many typefaces, weights, or styles;
- decorative elements without meaning;
- repetitive slide layouts;
- unnecessary charts;
- every paragraph converted into bullets;
- source pages copied directly into slides;
- content overflow;
- clipped content;
- overlapping elements;
- page-level horizontal scrolling;
- inaccessible or hover-only interaction;
- unnecessary or constant animation; and
- unsupported factual claims, values, sources, or citations.

One occurrence may be enough to fail when it materially harms comprehension, accessibility, factual accuracy, or usability. “Excessive” patterns require deck-level judgment rather than a mechanical count.

## 14. Repair loop

When a problem is found:

1. Identify the visible or factual problem precisely.
2. Determine the underlying rule, structure, or assumption that caused it.
3. Make the smallest coherent repair that addresses the cause.
4. Re-run the checks directly related to the repair.
5. Recheck neighboring slides, shared styles, navigation, data, citations, and responsive states for regressions.
6. Continue until the presentation passes or a genuine external constraint prevents repair.

Do not patch symptoms repeatedly with arbitrary offsets, tiny type, hidden content, or exceptions that create new inconsistencies.

If an issue cannot be repaired within the user's scope or available source material, disclose it clearly. Do not mark a material unresolved issue as passed.

## 15. Final delivery standard

Do not deliver until all applicable gates pass:

- narrative quality;
- content quality;
- source integrity;
- readability;
- visual hierarchy and composition;
- data visualization;
- interaction;
- accessibility;
- responsive behavior;
- technical validation;
- citation review; and
- anti-pattern review.

A presentation may be delivered with a remaining issue only when it is minor, disclosed when relevant, and does not materially reduce comprehension, accessibility, factual accuracy, trust, or usability.

Before delivery, perform one uninterrupted end-to-end review in the same order an audience will experience the presentation. Confirm that repairs did not introduce a late regression.

## Final rule

Optimize in this order:

```text
Understanding
  → Readability
  → Trust
  → Usefulness
  → Visual quality
```

Do not optimize for visual novelty at the expense of any earlier priority.
