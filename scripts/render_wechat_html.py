#!/usr/bin/env python3
import argparse
import html
import re
from pathlib import Path


P_STYLE = "margin:0 0 18px;color:#2f3742;font-size:15px;line-height:1.95;letter-spacing:0;text-align:justify;"
TITLE_STYLE = "margin:0 0 24px;color:#111827;font-size:24px;line-height:1.45;font-weight:700;letter-spacing:0;"
H2_WRAP = "margin:36px 0 16px;padding:0 0 0 12px;border-left:4px solid #111827;box-sizing:border-box;"
H2_TEXT = "margin:0;color:#111827;font-size:21px;line-height:1.45;letter-spacing:0;font-weight:700;"
H3_STYLE = "margin:28px 0 14px;color:#111827;font-size:17px;line-height:1.55;font-weight:700;letter-spacing:0;"
LIST_STYLE = "margin:0 0 18px;padding-left:1.2em;color:#2f3742;font-size:15px;line-height:1.95;"
LI_STYLE = "margin:0 0 8px;color:#2f3742;font-size:15px;line-height:1.95;"
CODE_STYLE = "display:block;margin:18px 0 22px;padding:14px 16px 14px 18px;background:#f8fafc;border:1px solid #e2e8f0;border-left:4px solid #ffda51;border-radius:0;color:#334155;font-size:13px;line-height:1.75;white-space:pre-wrap;overflow-wrap:break-word;"
FIGURE_STYLE = "margin:24px 0 26px;text-align:center;"
IMG_STYLE = "display:block;width:100%;max-width:100%;height:auto;box-sizing:border-box;background:#ffffff;border:1px solid #979899;padding:4px;border-radius:0;"
CAPTION_STYLE = "margin:8px 0 0;color:#64748b;font-size:13px;line-height:1.65;text-align:center;letter-spacing:0;"
QUOTE_STYLE = "margin:22px 0 24px;padding:14px 16px 14px 18px;background:#fff8d9;border-left:4px solid #111827;color:#2f3742;font-size:15px;line-height:1.9;letter-spacing:0;text-align:justify;box-sizing:border-box;"
HR_STYLE = "margin:30px auto;border:0;border-top:1px solid #e5e7eb;width:72%;"


def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r'<code style="padding:1px 4px;background:#f1f5f9;color:#334155;font-size:13px;border-radius:0;">\1</code>', text)
    text = re.sub(
        r"==([^=]+)==",
        r'<span style="background-color:rgb(255, 218, 81);color:#111827;">\1</span>',
        text,
    )
    text = re.sub(
        r"\*\*([^*]+)\*\*",
        r'<strong style="color:#111827;font-weight:700;">\1</strong>',
        text,
    )
    return text


def render(markdown: str, include_title: bool = False) -> tuple[str, str]:
    lines = markdown.splitlines()
    out: list[str] = []
    para: list[str] = []
    title = "公众号文章"
    i = 0

    def flush_para() -> None:
        nonlocal para
        if para:
            out.append(f'<p style="{P_STYLE}">{inline(" ".join(para))}</p>')
            para = []

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            flush_para()
            i += 1
            code: list[str] = []
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i])
                i += 1
            out.append(f'<pre style="{CODE_STYLE}"><code>{html.escape(chr(10).join(code))}</code></pre>')
            i += 1
            continue
        if line.startswith("# "):
            flush_para()
            title = line[2:].strip()
            if include_title:
                out.append(f'<p style="{TITLE_STYLE}"><strong>{inline(title)}</strong></p>')
            i += 1
            continue
        if line.startswith("## "):
            flush_para()
            text = line[3:].strip()
            out.append(f'<section style="{H2_WRAP}" data-role="title"><p style="{H2_TEXT}"><strong>{inline(text)}</strong></p></section>')
            i += 1
            continue
        if line.startswith("### "):
            flush_para()
            text = line[4:].strip()
            out.append(f'<p style="{H3_STYLE}"><strong>{inline(text)}</strong></p>')
            i += 1
            continue
        if line.startswith("> "):
            flush_para()
            quotes = []
            while i < len(lines) and lines[i].startswith("> "):
                quotes.append(lines[i][2:].strip())
                i += 1
            out.append(f'<section style="{QUOTE_STYLE}">{inline(" ".join(quotes))}</section>')
            continue
        if line.strip() in {"---", "***"}:
            flush_para()
            out.append(f'<hr style="{HR_STYLE}">')
            i += 1
            continue
        image_match = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", line.strip())
        if image_match:
            flush_para()
            caption = image_match.group(1).strip()
            src = image_match.group(2).strip()
            figure = f'<section style="{FIGURE_STYLE}"><img src="{html.escape(src)}" alt="{html.escape(caption)}" style="{IMG_STYLE}">'
            if caption:
                figure += f'<p style="{CAPTION_STYLE}">{inline(caption)}</p>'
            figure += "</section>"
            out.append(figure)
            i += 1
            continue
        if re.match(r"^[-*]\s+", line):
            flush_para()
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i]):
                items.append(re.sub(r"^[-*]\s+", "", lines[i]))
                i += 1
            out.append(f'<ul style="{LIST_STYLE}">' + "".join(f'<li style="{LI_STYLE}">{inline(item)}</li>' for item in items) + "</ul>")
            continue
        if re.match(r"^\d+\.\s+", line):
            flush_para()
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i]))
                i += 1
            out.append(f'<ol style="{LIST_STYLE}">' + "".join(f'<li style="{LI_STYLE}">{inline(item)}</li>' for item in items) + "</ol>")
            continue
        if not line.strip():
            flush_para()
            i += 1
            continue
        para.append(line.strip())
        i += 1

    flush_para()
    fragment = (
        '<section data-role="outer" label="edit by 135editor" '
        'style="margin:0;padding:0;color:#222222;background-color:#ffffff;'
        'font-family:&quot;PingFang SC&quot;,-apple-system,BlinkMacSystemFont,&quot;Helvetica Neue&quot;,&quot;Microsoft YaHei&quot;,Arial,sans-serif;">\n'
        '<section style="margin:0 auto;padding:0 0 8px;max-width:677px;box-sizing:border-box;">\n'
        + "\n".join(out)
        + "\n</section>\n</section>"
    )
    return title, fragment


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--include-title", action="store_true", help="render Markdown H1 inside the article body")
    parser.add_argument("--copy", action="store_true", help="copy editor fragment to macOS clipboard")
    args = parser.parse_args()

    source = args.input.read_text(encoding="utf-8")
    title, fragment = render(source, include_title=args.include_title)
    out_dir = args.out_dir or args.input.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.input.stem
    fragment_path = out_dir / f"{stem}_远航收藏夹排版_编辑器片段.html"
    preview_path = out_dir / f"{stem}_远航收藏夹排版版.html"
    fragment_path.write_text(fragment, encoding="utf-8")
    preview = f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)}</title></head><body style="margin:0;background:#ffffff;"><main style="max-width:677px;margin:0 auto;padding:28px 18px 56px;box-sizing:border-box;">{fragment}</main></body></html>'
    preview_path.write_text(preview, encoding="utf-8")
    if args.copy:
        import subprocess

        subprocess.run(["pbcopy"], input=fragment, text=True, check=True)
    print(fragment_path)
    print(preview_path)


if __name__ == "__main__":
    main()
