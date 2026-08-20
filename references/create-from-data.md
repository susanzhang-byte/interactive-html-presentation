# Create from data

Use this workflow to transform raw data, tables, spreadsheet content, research findings, and quantitative information into a clear presentation narrative. Understand what the data means before choosing a chart or slide composition.

The source data is the factual authority. Improve its organization and communication without changing definitions, manufacturing comparability, or overstating what the evidence supports.

## Data workflow

Follow this sequence:

```text
DATA
  → Inspect
  → Identify structure
  → Identify important metrics
  → Normalize units and periods
  → Identify comparisons and trends
  → Identify the main insight
  → Choose visual representation
  → Design slide
  → Add source and provenance
  → Quality check
```

Do not begin with a preferred chart type. Each visual choice must follow from the analytical question and the structure of the data.

## 1. Inspect the data

Review the complete available dataset, including titles, labels, notes, formulas, footnotes, source lines, and surrounding explanation.

Determine:

- what each row, column, series, and value represents;
- which fields are dimensions, categories, measures, dates, or identifiers;
- the units, currency, scale, sign convention, and precision;
- the reporting period and frequency;
- whether values are totals, subtotals, percentages, rates, indices, averages, medians, or counts;
- whether percentages use the same denominator;
- whether values are actual, estimated, projected, modeled, or scenario-based;
- whether blanks mean zero, unavailable, not applicable, suppressed, or unknown;
- which notes or definitions affect interpretation; and
- where the data originated and how precisely it can be cited.

Do not treat a formatted spreadsheet cell or prominent table row as automatically important. Meaning comes from the metric definition and the presentation purpose, not formatting alone.

If a value's meaning cannot be established, do not infer it from appearance. Preserve the ambiguity or exclude the value from analysis until it can be resolved.

## 2. Identify the structure

Describe the dataset before analyzing it. Establish:

- the observation level, such as one row per month, customer, geography, or product;
- the primary categories and their nesting or hierarchy;
- the time axis and whether periods are consecutive and comparable;
- the measures available for each observation;
- totals, components, benchmarks, targets, and comparison groups;
- missing, duplicate, suppressed, or anomalous entries;
- whether a table is wide, long, cross-tabulated, or already aggregated; and
- which fields can be compared without further qualification.

Check whether displayed totals reconcile with components when the source makes that relationship explicit. A mismatch may reflect rounding, exclusions, eliminations, or an error; retain the source note or flag the discrepancy rather than silently forcing a reconciliation.

## 3. Identify important metrics

Select metrics according to the presentation purpose and the decision or question they inform. Do not give every available measure equal visual weight.

For each candidate metric, record:

- exact name and definition;
- value and unit;
- date or reporting period;
- category, segment, geography, or population;
- denominator or baseline, when applicable;
- whether it is reported, adjusted, calculated, estimated, or projected;
- source location;
- qualifiers, uncertainty, or limitations; and
- the audience question it helps answer.

A metric is more likely to deserve prominence when it establishes scale, reveals meaningful change, explains a driver or constraint, distinguishes groups, measures progress, or supports a stated conclusion.

Do not promote a number merely because it is large, surprising, or easy to visualize.

## 4. Normalize units and periods safely

Normalize only to improve valid comparison. Retain the original values and definitions so every transformation remains traceable.

- Make units and scale explicit, including thousands, millions, billions, percentages, percentage points, basis points, currencies, and indexed values.
- Align time periods only when their duration and definitions are comparable.
- Distinguish fiscal and calendar periods.
- Distinguish point-in-time values from period totals or averages.
- Keep nominal, real, reported, adjusted, organic, and constant-currency values separate unless the source provides a valid reconciliation.
- Keep counts, rates, shares, and growth rates separate.
- Preserve the denominator for percentages and per-unit measures.
- Label any conversion or derived calculation and retain the inputs and method.
- Preserve appropriate precision; do not imply greater accuracy by adding decimal places.
- When rounding, use a consistent method and ensure the rounded display does not reverse or materially distort a comparison.

Never silently change units or time periods. Never combine incompatible metrics because their labels appear similar.

## 5. Identify comparisons, patterns, and trends

Determine the analytical relationship the audience needs to see:

- change over time;
- difference between categories or groups;
- ranking;
- composition of a total;
- contribution to a change;
- progress against a target or benchmark;
- distribution or variability;
- relationship between two variables;
- geographic variation;
- sequence of events; or
- flow, dependency, or system structure.

Validate each comparison before using it. Confirm that the values share compatible definitions, units, populations, periods, and calculation methods. If comparability is limited, state the limitation next to the comparison rather than relying on a distant note.

Treat correlation as correlation. Do not imply causation unless the source establishes a causal relationship. Do not call a short-term movement a trend unless the available series supports that description.

## 6. Identify the main insight

Before designing the slide, answer:

1. What is the important finding?
2. What changed or differs?
3. Compared with what?
4. Why does it matter to the intended audience?
5. What evidence supports the finding?
6. What caveat, uncertainty, or qualification must remain visible?

Write the slide's provisional headline as the supported insight, not merely the chart topic.

- Weak: “Revenue by Segment”
- Stronger, only when supported: “Software and Infrastructure drove the strongest growth”

If the data does not support a defensible conclusion, use a neutral descriptive headline. Never strengthen a claim simply to make the presentation feel more decisive.

## 7. Choose the visual representation

Use the simplest representation that answers the analytical question accurately. Do not create a chart merely because numeric data exists.

### Big number

Use when:

- one value is the main message;
- the comparison is simple; and
- emphasis matters more than displaying every value.

Show the metric name, unit, period, comparison context, and source. A concise explanation may be clearer than a chart.

### Bar chart

Use when:

- categories need comparison;
- ranking matters; or
- differences in magnitude are important.

Use a shared baseline for comparable magnitudes. Order bars by value when ranking is the point, or preserve a meaningful source order when sequence or category convention matters.

### Line chart

Use when:

- change over time is the main message; and
- the sequence and continuity of values matter.

Use a true chronological order, identify gaps, and avoid implying continuity between periods that are not comparable.

### Stacked bar chart

Use when:

- composition matters;
- the parts and total both matter; and
- the number of categories remains readable.

Avoid stacking so many categories that internal segments cannot be compared. Use a 100% stack only when proportional composition—not absolute total—is the intended question.

### Waterfall chart

Use when:

- a starting value changes through identifiable positive and negative contributors; and
- the bridge between beginning and ending values is the main story.

Ensure contributors reconcile to the ending value or clearly identify any residual, rounding, or omitted component.

### Scatter plot

Use when:

- the relationship between two quantitative variables matters; and
- enough observations exist for the relationship to be meaningful.

Label axes and units, disclose relevant grouping, and avoid presenting association as proof of causation. Do not add a trend line unless it is analytically justified.

### Table

Use when:

- exact values are important;
- the audience may compare several specific values; or
- a chart would hide necessary detail.

Align numbers consistently, keep units visible, use appropriate precision, and emphasize only the rows or columns relevant to the point.

### Timeline

Use when:

- sequence or dates are the main point; and
- events or milestones matter more than quantitative magnitude.

Keep chronological spacing honest when distance represents elapsed time. If spacing is schematic, make that clear.

### Comparison layout

Use when the audience needs to understand differences between options, periods, groups, or strategies and the content mixes quantitative and qualitative evidence. Align equivalent fields so comparisons do not depend on memory.

### Process or diagram

Use when the data describes a flow, relationship, dependency, hierarchy, or system rather than a simple numeric comparison. Do not imply direction, causality, or hierarchy that the source does not establish.

## 8. Manage data density

When there are too many values, resolve the problem in this order:

1. Identify the values necessary for the decision, conclusion, or comparison.
2. Remove redundant repetition while preserving distinct evidence.
3. Group related information and establish a clear visual order.
4. Use progressive disclosure for useful secondary detail when the primary message remains complete in the initial state.
5. Split the material into multiple slides when each resulting slide has a clear purpose.
6. Move reference-level values to a table or appendix when they must remain available but do not belong in the main reading path.

Never solve density problems by making labels, annotations, citations, or body text unreadably small. Never hide an important qualifier solely to simplify a visual.

## 9. Design the data-driven slide

Build the slide around one primary finding.

- Use an insight-led title when the evidence supports one.
- Make the important comparison visually obvious through position, scale, direct annotation, or restrained emphasis.
- Keep nearby the units, periods, categories, and qualifiers needed to interpret the visual.
- Prefer direct labels when they are clearer than a separate legend.
- Use a restrained and consistent palette. Assign accent color to a meaningful series, benchmark, exception, or focus—not to decoration.
- Minimize gridlines, borders, markers, labels, and effects that do not help interpretation.
- Keep every label readable at the intended viewport and on smaller screens.
- Ensure the slide remains understandable without hover or animation. Interaction may provide additional depth, not the only access to essential values.

## Chart readability and integrity

Every chart must:

- have a clear analytical purpose;
- use a meaningful title or adjacent insight;
- identify units and relevant time periods;
- use readable labels and annotations;
- preserve the correct scale and category order;
- distinguish series consistently;
- make the intended comparison easy to find;
- use restrained colors and minimal decoration;
- retain material caveats; and
- remain interpretable without relying only on color.

Never:

- use 3D charts;
- add decorative chart effects that obscure values;
- use excessive gridlines or visual noise;
- distort area, length, angle, or perspective to exaggerate a difference;
- omit missing periods in a way that implies continuity;
- use unequal time spacing as though it were equal;
- truncate an axis to exaggerate a difference; or
- label a derived value as though it came directly from the source.

A non-zero or truncated axis may be appropriate for some analytical views, but only when the scale is clearly visible, the choice does not mislead, and the analytical reason justifies it. Bar charts normally require a zero baseline because length encodes magnitude.

## Source and provenance

Record provenance for important values while analyzing them, not after slide design.

Capture whenever available:

- source name;
- page or section;
- table or figure name;
- date or reporting period;
- source URL or document identifier;
- relevant note, definition, or methodology; and
- whether a displayed value is copied, rounded, converted, or derived.

Associate provenance with the specific value, series, or claim it supports. Do not invent a citation or source detail when it is missing.

Plan the eventual HTML so provenance can appear visibly or through an accessible interaction. The slide's main meaning and necessary qualifiers must not depend on opening that interaction.

## Financial data safeguards

Preserve distinctions including:

- GAAP versus non-GAAP;
- reported versus constant currency;
- actual versus adjusted;
- annual versus quarterly;
- revenue versus annual recurring revenue (ARR);
- margin versus growth rate;
- historical versus forward-looking;
- fiscal versus calendar period;
- point-in-time versus period-end or period-average values; and
- currency, scale, and segment definitions.

Do not merge these categories because their labels or magnitudes appear similar. When reported and adjusted measures appear together, label each directly and retain any reconciliation or qualification supplied by the source.

Do not present forward-looking information as an achieved result. Preserve the source's uncertainty, assumptions, ranges, and cautionary language where they materially affect interpretation.

## Pre-finalization quality check

Before finalizing a data-driven slide, verify:

- every displayed number is traceable to the source or clearly labeled as a derived calculation;
- metric names and definitions remain accurate;
- units, currencies, scale, denominators, dates, and periods are correct;
- categories and series have not been silently combined or omitted;
- reported, adjusted, and other material distinctions remain visible;
- comparisons use compatible definitions and time frames;
- the chart type matches the analytical question;
- the main insight is visually obvious and supported by the data;
- axis choices, ordering, area, and perspective do not mislead;
- labels, legends, annotations, and citations remain readable;
- no important qualifier, limitation, or uncertainty has been removed;
- correlation has not been described as causation;
- the slide is not overloaded; and
- the slide remains understandable at small-screen sizes and without optional interaction.

If any check fails, revise the analysis, comparison, visual choice, or slide composition before continuing.
