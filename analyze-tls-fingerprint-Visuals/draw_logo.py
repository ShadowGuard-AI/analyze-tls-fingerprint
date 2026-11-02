#!/usr/bin/env python3
"""analyze-tls-fingerprint logo: an examiner's clipboard held at the angle an examiner holds
it, tilted a few degrees off square, filling the mark. The board is coastal line blue enamel
worn at the corners to bare metal, its spring clip at the top a plain bar of rust flecked steel
gripping a single sheet in timetable white. On the sheet one printed row waits alone: three
empty boxes in a line, a short rule, and a longer empty space beside it. No hand, no pencil,
no car. Below the board the name is set in BIZ UDMincho in timetable white on coastal line
blue, spaced like the entries on a printed schedule. At 64 pixels: a blue board, a white
sheet, and a steel clip; if the sheet merges into a tablet, the clip has been drawn too small."""
import sys
from PIL import Image, ImageDraw, ImageFont
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1000, 800
BLUE = (36, 80, 126); WHITE = (247, 245, 238); RUST = (180, 85, 45); STEEL = (150, 154, 158); METAL = (196, 198, 200)
img = Image.new("RGB", (W, H), (214, 218, 220)); d = ImageDraw.Draw(img, "RGBA")
# the board, tilted a few degrees off square
board = [(268, 66), (742, 40), (768, 540), (294, 566)]
d.polygon(board, fill=BLUE)
# enamel worn at the corners to bare metal
for (cx, cy) in [(282, 76), (730, 52), (756, 528), (306, 552)]:
    d.polygon([(cx - 20, cy - 8), (cx + 16, cy - 14), (cx + 8, cy + 16), (cx - 14, cy + 10)], fill=METAL)
# the single sheet gripped under the clip
sheet = [(322, 128), (694, 106), (712, 486), (338, 506)]
d.polygon(sheet, fill=WHITE)
d.polygon(sheet, outline=(198, 198, 192), width=2)
# the spring clip: a plain bar of rust flecked steel (v1 draws it too small to survive)
if A == "--v1":
    d.rectangle([452, 84, 556, 104], fill=STEEL)
else:
    d.rectangle([408, 62, 606, 122], fill=STEEL, outline=(110, 112, 116), width=3)
    d.rectangle([408, 62, 606, 78], fill=(172, 176, 180))
    for (fx, fy) in [(440, 88), (500, 100), (562, 80), (478, 108), (540, 106)]:
        d.ellipse([fx - 4, fy - 3, fx + 4, fy + 3], fill=RUST)  # rust flecks
    d.ellipse([486, 70, 528, 100], outline=(110, 112, 116), width=4)  # clip ring
# one printed row waiting alone: three empty boxes, a short rule, a longer empty space
ry = 268
for i in range(3):
    x = 366 + i * 62; d.rectangle([x, ry, x + 42, ry + 42], outline=(52, 56, 60), width=4)
d.line([(566, ry + 21), (622, ry + 18)], fill=(52, 56, 60), width=4)   # short rule
d.line([(640, ry + 21), (694, ry + 19)], fill=(206, 208, 204), width=3)  # the longer empty space, left blank
if A == "--v2":  # v2 flaw: the sheet filled with further rows, losing the one waiting row
    for yy in (348, 416):
        for i in range(3):
            x = 366 + i * 62; d.rectangle([x, yy, x + 42, yy + 42], outline=(52, 56, 60), width=4)
        d.line([(566, yy + 21), (680, yy + 19)], fill=(52, 56, 60), width=4)
# name plate below the board
d.rectangle([0, 590, W, H], fill=BLUE)
d.rectangle([0, 590, W, 600], fill=RUST)
base = __file__.rsplit("/", 1)[0]
name = "analyze-tls-fingerprint"
f = ImageFont.truetype(base + "/fonts/BIZ-UDMincho.ttf", 52)
widths = [d.textlength(ch, font=f) for ch in name]
gap = 9; total = sum(widths) + gap * (len(name) - 1); x = (W - total) / 2
for ch, wch in zip(name, widths):
    d.text((x, 668), ch, font=f, fill=WHITE); x += wch + gap
img.save(sys.argv[2] if len(sys.argv) > 2 else "logo.png")
print("logo saved")
