---
name: quick-summary
description: Turn videos, timestamped transcripts, webpages, articles, and plain text into concise, visually structured interactive summaries: TL;DR, full topic navigator, expandable explanations, plain-language technical analogies, business implications, and grounded timestamps or quotes. No archive or website setup.
---

# Quick Summary

## Goal
Help a reader decide within ~30 seconds whether a source deserves deeper attention, while preserving all important source arguments in expandable topic-level detail. Prioritize high readability, concise but substantive explanations, diagrams, compact UI, and minimal scrolling—not an uninterrupted wall of text.

## When to use
When a user provides a video or article URL, transcript (with or without timecodes), or source text and requests a summary, or calls Quick Summary by name. Respond in the source's language unless asked otherwise. Never ask for website setup or archive credentials.

## Workflow
1. **Ground the source.** Read the user-provided text fully where feasible; for a video, obtain a reliable transcript or chapter/source material. Clearly note if only a description or partial transcript was available. Do not pretend to have watched inaccessible footage. Establish actual title, creator, source date, duration when available. Where current context materially matters, verify against reliable sources and cite.
2. **Map all important topics.** Identify distinct claims, mechanisms, examples, qualifications, and conclusions in source order; merge genuine repetitions but do not omit important points. Avoid inventing chapter boundaries or timestamps. For videos and timestamped scripts, preserve exact supplied or verified timecodes; make timecodes link to the original video's start position when feasible. If there are no known timecodes, do not manufacture any.
3. **Create a TL;DR.** Use 2–4 information-dense, accessible sentences explaining the source's main thesis and strongest supporting insights.
4. **Render topic navigation.** Show every important topic as a compact numbered expandable row/card with a short title, timestamp if verified, one-sentence core takeaway and—when the space allows—a brief business implication. Default all detail panels closed. If the interface offers interactive state, each click expands only the selected topic (others need not close). If no interactive components exist, use a compact linked outline with short details organized under headings.
5. **Provide depth only on demand.** Expanded details include: what is argued and why; concrete, source-grounded examples; technical term explanations in ordinary language with a detailed and accurate analogy (and limits of analogy when misleading); practical business implications (opportunity, risk, or decision for relevant stakeholders); caveats and significant counterpoints; a short source-verified quote if the input is plain text and quoting adds value. Ensure the analogy is understandable to someone with no technical background.
6. **Visualize when useful.** Include one small, meaningful diagram, flow, timeline, contrast matrix, or process illustration for a source with a clear structure. Never invent quantitative metrics to populate visuals. Use horizontal space for paired analogy/business implication cards in expanded details, rather than vertically stacking many paragraphs.
7. **Finish in the same response.** Do not add website links, archive status, JSON exports, saving instructions, or an extra Part 2. End after the topics and at most one optional line about a highly relevant previous source, if confidently established.

## Required layout
- Compact source title and short metadata line; no hero thumbnails or large podcast/video imagery.
- TL;DR panel, 2–4 sentences.
- Optional single compact explanatory diagram, only if valuable.
- All important topics visible immediately as collapsed interactive accordions or topic selector, preserving source order.
- When expanded, readable explanatory detail, two small side-by-side panels for **Everyday analogy** and **Business implications**, optional technical term/caveat, and verified linked video timecode.
- **Previous learning connection:** at most ONE short sentence or link, only if strongly relevant and reliably supported. No expanded related-content section.

## Color, density, and UX rules
- Restrained, purposeful accents: muted indigo/purple for active topics or navigation, slate for metadata, soft sage/green for business implications, and muted amber for meaningful risks or uncertainty. Warm light background and readable charcoal text. Never use a rainbow of colors or encode meaning with color alone.
- Make an at-a-glance topic map; prioritize horizontal space; short expandable rows with enough whitespace to read but minimal vertical scrolling. Don't add large evaluation cards, tall hero images, decorative section cards, 'Worth your time?' scores, or 'Most valuable section' cards.
- Keep technical complexity in expanded details, not on the overview. Avoid boilerplate or repeat explanations across topics.
- Do NOT add a standalone news/real-world examples section. Only when user requests it, or a current example is essential, add up to 1–2 brief verified references inside the relevant expanded topic.
- Don't create a separate giant list of your own takeaways after covering the full topic map.
- Ensure buttons are real and keyboard-accessible when the interface supports them. On mobile, collapse to one column with a compact topic picker.

## Fidelity and judgment
- Attribute speaker claims versus established facts versus your business interpretation.
- Ground technical analogies and note boundaries if simplification would mislead.
- Use exact timestamps when provided; otherwise only timestamps established from source. Never recycle timestamps from memory without verifying for this source.
- For plain text, select only brief, consequential direct quotations and reproduce them accurately; do not present paraphrases as quotes.
- Cover all important topics even if there are many; increase navigational density rather than cutting essential content. Avoid invented data, quotes, metrics, source dates, links and events.
- If a transcript or article cannot be accessed, summarize only content verifiably available and label the limitation rather than invent details.

## Final quality checklist
- [ ] TL;DR explains the central argument in 2–4 substantive sentences.
- [ ] All important topics appear in a compact navigable overview, in source order.
- [ ] Details are collapsed initially; each expansion explains meaning, analogy and business implications.
- [ ] Verified video/script timestamps or brief verified plain-text quotes are present where available.
- [ ] Colors are tasteful; scanning and readability are prioritized over decorative imagery.
- [ ] No archive, OAuth, website, database, saving action, or Part 2 instructions appear.