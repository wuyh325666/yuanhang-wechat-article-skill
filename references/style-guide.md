# 远航收藏夹 Style Guide

## Account Positioning

Account name: 远航收藏夹

Content should feel like a practical AI/productivity collector explaining what is actually useful after testing tools and methods. The tone should be direct, lightly humorous, and specific.

## Writing Voice

Use:

- short paragraphs mixed with complete explanatory paragraphs
- first-person experience when useful
- clear judgments
- mild吐槽 when it helps reader identification
- concrete analogies from work, tools, workflows, and everyday operations
- standalone short sentences only when they create emphasis or transition

Avoid:

- generic AI marketing language
- "在当今时代..." openings
- repetitive "痛点-方案-总结" templates
- long abstract paragraphs
- a whole article made of one-line sentences
- over-polished consultant phrasing
- too many slogans without operations

Good sentence pattern:

- "不是它不聪明。是它不认识你。"
- "仓库的价值是存东西。大脑的价值是帮你判断。"
- "聊天记录不是知识库。回写之后，才算沉淀。"

## Article Rhythm

Open with one of:

- a recognizable work scene
- a blunt conclusion
- a misconception correction
- a specific failure story

Then move quickly into the practical promise. For tool/tutorial topics, reach the core claim within the first 3-5 paragraphs. Do not spend too long warming up.

For tutorial articles, keep pain and misconception around the first third. Spend the remaining two thirds on specific steps, prompts, examples, and checks.

After a draft, run a rhythm pass:

- merge adjacent short sentences when they are explanatory rather than emphatic
- keep short lines for judgment, contrast, and punchlines
- avoid making every paragraph one sentence long
- make the first screen directly answer "why should I click/read this"

## WeChat Typesetting

Default theme:

- Use `references/theme-yellow-black.md` as the visual component source.
- The account's stable visual language is white background, black structure, yellow attention markers.
- Black carries hierarchy and judgment; yellow carries reminders and scan anchors.
- Do not turn yellow into a large background field; keep it as a precise accent.

Base typography:

- body font size: 15px
- body color: `#2f3742`
- line height: 1.95
- paragraph margin bottom: 18px
- font family: PingFang SC / system Chinese sans-serif

Main title:

- In WeChat editor output, omit the Markdown H1 from the body by default because the WeChat title field already carries the title.
- If a standalone preview page needs a visible title, use 24px, bold, `#111827`, line-height 1.45.
- bold
- color `#111827`
- line-height 1.45

Section headings:

- use a `section` wrapper, not only `h2`
- margin: `36px 0 16px`
- padding-left: `12px`
- left border: `4px solid #111827`
- heading text: 21px, bold, `#111827`, line-height 1.45
- Chinese numbered headings are preferred for long tutorials: `一、...`

Highlights:

- yellow background: `rgb(255, 218, 81)`
- use yellow for reader attention, reminders, caveats, or practical next actions
- use bold for core judgments, definitions, and conceptual pivots
- do not combine bold and yellow by default; choose one based on purpose
- apply to short key spans or sentences, not whole paragraphs
- place bold/yellow emphasis near the middle of a section or paragraph when possible, not always at the first or last paragraph; avoid making the visual weight feel top-heavy or end-heavy

Images:

- center aligned
- white background
- border: `1px solid #979899`
- padding: 4px
- no rounded corners
- caption: 13px, `#64748b`, centered
- Insert images after key claims or operational steps, not only at the end.
- Captions should be plain, short, and descriptive. Avoid highlighting captions with yellow.

Code blocks:

- light gray background
- 13px text
- border `#e2e8f0`
- no rounded corners

WeChat paste notes:

- Prefer inline styles.
- Preserve heading style with `section` and left border.
- Avoid relying on global CSS.
- Do not paste the article title as body content unless the user asks.
