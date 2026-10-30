"""Draw static/og.png, the 1200x630 link-preview image.

Run from the project root after `npm install` (it reads the fonts from node_modules):
    python scripts/make_og_image.py
Needs Pillow. Colours match the tokens in src/app.css.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / 'node_modules/@fontsource/jetbrains-mono/files'
OUT = ROOT / 'static/og.png'

BG = '#0b0d0c'
BORDER = '#1f2924'
TEXT = '#d3dbd5'
MUTED = '#7d8c83'
ACCENT = '#4ade80'
ACCENT_DIM = '#2c6a45'

# Same first frame as invaderFrames in src/routes/+page.svelte.
INVADER = [
    '..X.....X..',
    '...X...X...',
    '..XXXXXXX..',
    '.XX.XXX.XX.',
    'XXXXXXXXXXX',
    'X.XXXXXXX.X',
    'X.X.....X.X',
    '...XX.XX...',
]


def font(weight, size):
    return ImageFont.truetype(str(FONTS / f'jetbrains-mono-latin-{weight}-normal.woff'), size)


def draw_runs(draw, xy, runs):
    """Draw (text, colour, font) runs left to right on one baseline."""
    x, y = xy
    for text, fill, f in runs:
        draw.text((x, y), text, fill=fill, font=f, anchor='ls')
        x += draw.textlength(text, font=f)


def main():
    img = Image.new('RGB', (1200, 630), BG)
    draw = ImageDraw.Draw(img)
    left = 96

    prompt = font(400, 30)
    draw_runs(draw, (left, 150), [
        ('hugo@barroca', ACCENT, prompt),
        (':~$ ', MUTED, prompt),
        ('whoami', TEXT, prompt),
    ])

    draw.text((left, 300), 'Hugo Barroca', fill=TEXT, font=font(700, 96), anchor='ls')

    role = font(400, 34)
    draw_runs(draw, (left, 370), [
        ('Software developer', ACCENT, role),
        (' / ', ACCENT_DIM, role),
        ('C# & .NET', ACCENT, role),
        (' / ', ACCENT_DIM, role),
        ('Azure', ACCENT, role),
    ])

    draw.line([(left, 470), (1200 - left, 470)], fill=BORDER, width=2)
    draw.text((left, 540), 'hugobarroca.dev', fill=MUTED, font=font(400, 30), anchor='ls')

    cell = 16
    ox = 1200 - left - cell * 11
    oy = 180
    for y, row in enumerate(INVADER):
        for x, c in enumerate(row):
            if c == 'X':
                draw.rectangle(
                    [ox + x * cell, oy + y * cell, ox + (x + 1) * cell - 1, oy + (y + 1) * cell - 1],
                    fill=ACCENT_DIM,
                )

    img.save(OUT, optimize=True)
    print(f'wrote {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
