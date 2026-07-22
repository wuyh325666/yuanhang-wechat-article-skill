---
name: yuanhang-wechat-article
description: Produce publish-ready WeChat public account articles for the user's account "远航收藏夹". Use when the user asks to write, rewrite, compare drafts, polish, typeset, summarize, package, or create cover assets for a 远航收藏夹公众号 article; when turning videos, transcripts, links, notes, or Obsidian materials into WeChat articles; or when generating WeChat editor HTML, 50-character summaries, titles, cover prompts, or 2.35:1 cover images in the user's established style.
---

# 远航收藏夹公众号文章

## Output Goal

Deliver a publish-ready package, not just prose:

1. Article draft in the 远航收藏夹 voice.
2. Optional 3-4 version comparison when the user is selecting direction.
3. WeChat-editor HTML fragment with inline styles. Do not duplicate the article title inside the body by default; WeChat has its own title field.
4. 50-character share summary when requested.
5. Titles and cover direction when useful.
6. 2.35:1 cover image when requested.
7. Clipboard handoff when the user wants to paste into WeChat.

Do not attempt to automate `mp.weixin.qq.com` UI. The current environment may block direct operation on WeChat backend pages. Prefer generating a paste-ready HTML fragment and optionally copying it to the local clipboard.

## Required References

- Read `references/style-guide.md` before writing or rewriting a 远航收藏夹 article.
- Read `references/theme-yellow-black.md` before typesetting a 远航收藏夹 article, creating WeChat editor HTML, or deciding emphasis/image/component placement.
- Read `references/article-structures.md` when choosing article structure, producing comparison drafts, or fixing an "AI-ish" draft.
- Read `references/published-learnings.md` when revising the skill's own outputs or when the user references published articles as feedback.

## Workflow

### 1. Gather Source Material

Use local files first when available. For user-provided URLs, fetch current content when allowed and needed. For video/transcript material, preserve copyright constraints unless the user confirms ownership.

Extract:

- core claim
- reader pain
- misconception to correct
- concrete method or steps
- examples and usable analogies
- source-specific terms that should remain

### 2. Decide Article Shape

Pick one structure based on the topic and reader promise:

- story-entry: pain is easy to dramatize
- sharp-opinion: topic needs a stronger IP point of view
- practical-checklist: user expects a tutorial
- framework-explainer: topic needs conceptual clarity plus execution

Avoid repeating the same opening format across weekly articles.

### 3. Draft in Voice

Write readable paragraphs with varied rhythm. Use short standalone sentences for emphasis, not as the default for every sentence. Prefer direct judgment over generic exposition. Use concrete metaphors only when they clarify the point.

Default proportion for tutorial topics:

- first third: pain + misconception
- final two thirds: executable framework + concrete steps

### 4. Create Comparison Drafts

When the user asks to compare drafts, produce 3-4 complete variants, each with a clear positioning note:

- current/framework version
- story-entry version
- sharp-opinion version
- practical-checklist version

Save each variant as a separate Markdown file and render each to HTML if the user needs visual comparison.

### 5. Typeset for WeChat

Use `scripts/render_wechat_html.py` to convert Markdown into WeChat-compatible HTML.

The default visual system is `references/theme-yellow-black.md`: white background, black structure, yellow attention markers. Use `**...**` for bold judgments and `==...==` for yellow reminders. Do not combine them by default.

```bash
python3 /Users/wuyuanhang/.codex/skills/yuanhang-wechat-article/scripts/render_wechat_html.py input.md --out-dir output-folder
```

The script writes:

- `*_远航收藏夹排版版.html` for browser preview
- `*_远航收藏夹排版_编辑器片段.html` for WeChat editor paste

Important: use the fragment file for the WeChat editor.

By default, the script uses the Markdown H1 as metadata only and omits it from the article body. Use `--include-title` only when the body itself needs a visible title.

### 6. Clipboard Handoff

When the user asks to paste into WeChat or use "method 3", copy the editor fragment:

```bash
pbcopy < path/to/*_编辑器片段.html
```

Tell the user to click the WeChat article body and press `Command+V`.

### 7. Cover Image

For WeChat cover images, use exact 2.35:1 ratio. Recommended deterministic size: `1175 x 500`.

Use `scripts/make_cover.py` for a simple local cover:

```bash
python3 /Users/wuyuanhang/.codex/skills/yuanhang-wechat-article/scripts/make_cover.py \
  --title "别再让AI每次都重新认识你" \
  --subtitle "Obsidian + LLM Wiki 第二大脑" \
  --output cover.png
```

If using image generation instead, verify the output ratio. If wrong, regenerate or crop to 2.35:1.

## Quality Checklist

Before final delivery, check:

- the article does not use a repetitive template opening
- the reader value is clear within the first screen
- the opening reaches the core claim within the first 3-5 paragraphs
- short sentences are used deliberately, not throughout the whole article
- pain and misconception do not occupy more than needed
- concrete operations dominate tutorial articles
- headings are direct and useful
- WeChat HTML uses inline styles
- small headings use `section` with left border, not only `h2`
- body HTML does not duplicate the WeChat title unless explicitly requested
- cover image is exactly 2.35:1 when delivered
- final answer includes exact local file links
