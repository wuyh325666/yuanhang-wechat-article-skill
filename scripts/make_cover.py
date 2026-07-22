#!/usr/bin/env python3
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def make_cover(title: str, subtitle: str, output: Path, width: int = 1175, height: int = 500) -> None:
    img = Image.new("RGB", (width, height), "#f7f8f6")
    draw = ImageDraw.Draw(img)
    for x in range(0, width, 70):
        draw.line((x, 0, x, height), fill="#eef0ec", width=1)
    for y in range(0, height, 70):
        draw.line((0, y, width, y), fill="#eef0ec", width=1)

    card = Image.new("RGBA", (430, 300), (255, 255, 255, 0))
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle((20, 30, 410, 250), radius=18, fill=(255, 255, 255, 210), outline=(215, 220, 220, 180), width=2)
    for yy, w in [(70, 250), (105, 310), (140, 220), (175, 285), (210, 190)]:
        cd.rounded_rectangle((65, yy, 65 + w, yy + 12), radius=6, fill=(38, 55, 66, 45))
    nodes = [(305, 80), (350, 140), (300, 205), (235, 160)]
    for a, b in zip(nodes, nodes[1:]):
        cd.line((*a, *b), fill=(17, 24, 39, 80), width=2)
    for x, y in nodes:
        cd.ellipse((x - 8, y - 8, x + 8, y + 8), fill=(255, 218, 81, 230), outline=(17, 24, 39, 120))
    card = card.filter(ImageFilter.GaussianBlur(0.2))
    img.paste(card, (715, 95), card)

    title_lines = title.replace("AI", "AI").split("\\n")
    if len(title_lines) == 1 and len(title) > 12:
        title_lines = [title[:6], title[6:12], title[12:]]
    y = 78
    for idx, line in enumerate(title_lines[:3]):
        size = 72 if idx == 0 else 68
        draw.text((70, y), line, font=font(size), fill="#111827")
        y += 86
    draw.rounded_rectangle((72, 348, 430, 360), radius=6, fill="#ffda51")
    draw.text((70, 380), subtitle, font=font(32), fill="#2f3742")
    draw.text((875, 430), "让 AI 读懂你的长期上下文", font=font(22), fill="#64748b")

    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--width", type=int, default=1175)
    parser.add_argument("--height", type=int, default=500)
    args = parser.parse_args()
    make_cover(args.title, args.subtitle, args.output, args.width, args.height)
    print(args.output)
    print(f"{args.width}x{args.height} ratio={args.width / args.height:.2f}")


if __name__ == "__main__":
    main()

