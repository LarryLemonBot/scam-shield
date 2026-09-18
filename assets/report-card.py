#!/usr/bin/env python3
"""Render the shareable Scam Shield Report Card example.

Re-run from repo root or this directory:

    python3 assets/report-card.py

Writes assets/report-card-example.png (1080x1350). Data is eval #01
(fake toll-road text) plus the field rules in bot-template/report-card-format.md.
Money at risk is never invented. Actions listed are the YES-gated loop-close
example for this card, not a live FTC confirmation number.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "report-card-example.png"
W, H = 1080, 1350

# Dark theme
BG = (7, 9, 13, 255)
SURFACE = (16, 20, 28, 255)
SURFACE_2 = (22, 27, 38, 255)
LINE = (36, 43, 58, 255)
RED = (232, 45, 74, 255)
RED_DIM = (58, 16, 24, 255)
RED_SOFT = (255, 90, 110, 255)
TEXT = (244, 246, 248, 255)
MUTED = (139, 147, 167, 255)
WHITE = (255, 255, 255, 255)

FONT_DIR = Path("/usr/share/fonts/truetype/noto")
DEJAVU = Path("/usr/share/fonts/truetype/dejavu")


def _font(name: str, size: int, fallback: str = "DejaVuSans.ttf") -> ImageFont.FreeTypeFont:
    for path in (FONT_DIR / name, DEJAVU / fallback, DEJAVU / "DejaVuSans-Bold.ttf"):
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


FONT_BRAND = _font("NotoSansDisplay-ExtraBold.ttf", 28, "DejaVuSans-Bold.ttf")
FONT_LABEL = _font("NotoSans-SemiBold.ttf", 22, "DejaVuSans-Bold.ttf")
FONT_VERDICT = _font("NotoSansDisplay-ExtraBold.ttf", 118, "DejaVuSans-Bold.ttf")
FONT_TYPE = _font("NotoSans-Bold.ttf", 40, "DejaVuSans-Bold.ttf")
FONT_SUB = _font("NotoSans-Regular.ttf", 26, "DejaVuSans.ttf")
FONT_QUOTE = _font("NotoSans-SemiBold.ttf", 28, "DejaVuSans-Bold.ttf")
FONT_BODY = _font("NotoSans-Regular.ttf", 30, "DejaVuSans.ttf")
FONT_FOOT = _font("NotoSans-Regular.ttf", 22, "DejaVuSans.ttf")
FONT_FOOT_B = _font("NotoSans-SemiBold.ttf", 22, "DejaVuSans-Bold.ttf")


def _text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if _text_size(draw, trial, font)[0] <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [text]


def round_rect(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    radius: int,
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int] | None = None,
    width: int = 1,
) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_shield(draw: ImageDraw.ImageDraw, cx: int, cy: int, w: int, h: int) -> None:
    pts = [
        (cx - w // 2, cy - h // 2 + 4),
        (cx + w // 2, cy - h // 2 + 4),
        (cx + w // 2, cy + h // 8),
        (cx, cy + h // 2),
        (cx - w // 2, cy + h // 8),
    ]
    draw.polygon(pts, fill=RED)
    inner = [
        (cx - w // 2 + 7, cy - h // 2 + 10),
        (cx + w // 2 - 7, cy - h // 2 + 10),
        (cx + w // 2 - 7, cy + h // 8 - 2),
        (cx, cy + h // 2 - 10),
        (cx - w // 2 + 7, cy + h // 8 - 2),
    ]
    draw.polygon(inner, fill=BG)
    # Check
    draw.line(
        [(cx - 8, cy + 2), (cx - 2, cy + 10), (cx + 12, cy - 10)],
        fill=RED,
        width=4,
        joint="curve",
    )


def section_label(draw: ImageDraw.ImageDraw, x: int, y: int, text: str) -> int:
    draw.text((x, y), text.upper(), font=FONT_LABEL, fill=MUTED)
    return y + 36


def render() -> None:
    img = Image.new("RGBA", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Top brand bar
    draw.rectangle((0, 0, W, 8), fill=RED)
    draw_shield(draw, 88, 64, 44, 52)
    draw.text((122, 42), "SCAM SHIELD", font=FONT_BRAND, fill=TEXT)
    brand_w, _ = _text_size(draw, "SCAM SHIELD", FONT_BRAND)
    draw.text((122 + brand_w + 16, 46), "REPORT CARD", font=FONT_LABEL, fill=MUTED)

    # Verdict banner
    banner = (48, 108, W - 48, 308)
    round_rect(draw, banner, 28, RED_DIM, outline=RED, width=3)
    label = "VERDICT"
    lw, lh = _text_size(draw, label, FONT_LABEL)
    draw.text(((W - lw) // 2, 128), label, font=FONT_LABEL, fill=RED_SOFT)
    verdict = "SCAM"
    vw, vh = _text_size(draw, verdict, FONT_VERDICT)
    draw.text(((W - vw) // 2, 168), verdict, font=FONT_VERDICT, fill=WHITE)

    # Scam type
    panel_x1, panel_x2 = 48, W - 48
    y = 336
    round_rect(draw, (panel_x1, y, panel_x2, y + 148), 22, SURFACE)
    y_in = section_label(draw, 80, y + 22, "Scam type")
    draw.text((80, y_in + 4), "Toll-road smishing", font=FONT_TYPE, fill=TEXT)
    draw.text((80, y_in + 58), "Government imposter  ·  unpaid-toll SMS", font=FONT_SUB, fill=MUTED)

    # Red flags
    flags = [
        "Pay within 24 hours or your plate will be suspended",
        "Tap to pay: https://bit.ly/toll-pay-now",
        "DMV Enforcement Division",
    ]
    y = 508
    flag_bottom = y + 430
    round_rect(draw, (panel_x1, y, panel_x2, flag_bottom), 22, SURFACE)
    y_in = section_label(draw, 80, y + 22, "Red flags")
    quote_top = y_in + 8
    row_h = 118
    for i, quote in enumerate(flags):
        ry = quote_top + i * row_h
        round_rect(draw, (72, ry, panel_x2 - 24, ry + 104), 16, SURFACE_2)
        draw.rectangle((72, ry + 16, 80, ry + 88), fill=RED)
        num = f"{i + 1}"
        draw.text((96, ry + 16), num, font=FONT_LABEL, fill=RED_SOFT)
        wrapped = wrap(draw, f"“{quote}”", FONT_QUOTE, panel_x2 - 160)
        ty = ry + 18
        for line in wrapped[:2]:
            draw.text((128, ty), line, font=FONT_QUOTE, fill=TEXT)
            ty += 36

    # Money at risk
    y = 962
    round_rect(draw, (panel_x1, y, 516, y + 196), 22, SURFACE)
    y_in = section_label(draw, 80, y + 22, "Money at risk")
    money_lines = wrap(draw, "Unknown — no payment made", FONT_BODY, 400)
    my = y_in + 12
    for line in money_lines:
        draw.text((80, my), line, font=FONT_BODY, fill=TEXT)
        my += 38

    # Actions taken
    round_rect(draw, (540, y, panel_x2, y + 196), 22, SURFACE)
    y_in = section_label(draw, 572, y + 22, "Actions taken")
    actions = ["Forwarded to 7726", "Reported to FTC"]
    ay = y_in + 10
    for action in actions:
        draw.ellipse((572, ay + 8, 592, ay + 28), fill=RED)
        # check mark
        draw.line([(577, ay + 18), (581, ay + 24), (588, ay + 12)], fill=WHITE, width=3)
        draw.text((608, ay), action, font=FONT_BODY, fill=TEXT)
        ay += 48

    # Footer
    draw.line((48, 1190, W - 48, 1190), fill=LINE, width=2)
    draw.text((48, 1220), "checked by Scam Shield", font=FONT_FOOT_B, fill=MUTED)
    draw.text((48, 1256), "github.com/LarryLemonBot/scam-shield", font=FONT_FOOT, fill=MUTED)
    src = "eval #01  ·  quotes from the original message"
    sw, _ = _text_size(draw, src, FONT_FOOT)
    draw.text((W - 48 - sw, 1256), src, font=FONT_FOOT, fill=MUTED)

    img.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    render()
