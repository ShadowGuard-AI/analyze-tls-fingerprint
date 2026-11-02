#!/usr/bin/env python3
"""analyze-tls-fingerprint banner: the examiner's waiting area at the start of a test morning,
seen across the room toward the window where the road shows beyond it. A row of plain chairs
stands empty, a clipboard rests face up on the nearest chair with the day's first printed row
still blank, clipboards hang from hooks on the enamel blue wall beside a timetable board whose
frame is up but whose columns are turned away, and through the window the test road runs past
in wet coastal light with a give way line and a waiting car at the kerb, headlamps on. A kettle,
a coat hook with one coat, and a stack of spare sheets complete the room. The name is printed
in BIZ UDMincho in timetable white on the coastal line blue board mounted above the hooks, one
board only, and no other readable writing on any sheet, wall, or window."""
import sys
from PIL import Image, ImageDraw, ImageFont
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1600, 680
BLUE = (36, 80, 126); WHITE = (247, 245, 238); RUST = (180, 85, 45); STEEL = (150, 154, 158); WOOD = (146, 110, 74)
img = Image.new("RGB", (W, H), (198, 204, 208)); d = ImageDraw.Draw(img, "RGBA")
# window and road, background right
d.rectangle([1060, 56, 1570, 440], fill=(178, 190, 198))
for (rx, ry, rw) in [(1130, 330, 130), (1310, 318, 170), (1500, 330, 90)]:
    d.polygon([(rx, ry), (rx + rw // 2, ry - 42), (rx + rw, ry), (rx + rw, ry + 58), (rx, ry + 58)], fill=(142, 152, 160))
d.rectangle([1060, 302, 1570, 440], fill=(58, 60, 62))
for i in range(6): d.line([(1100 + i * 80, 400), (1146 + i * 80, 400)], fill=(240, 240, 236), width=7)
for (x, y) in [(1240, 356), (1298, 356), (1360, 356), (1418, 356)]:
    d.polygon([(x, y), (x + 22, y), (x + 11, y + 16)], fill=(240, 240, 236))  # give way triangles
d.polygon([(1190, 272), (1250, 230), (1370, 230), (1436, 272), (1436, 310), (1190, 310)], fill=(70, 76, 84))
d.rectangle([1266, 238, 1360, 264], fill=(168, 182, 192))
for hx in (1216, 1392):
    d.ellipse([hx - 17, 282, hx + 17, 304], fill=(255, 238, 170)); d.ellipse([hx - 30, 276, hx + 30, 310], fill=(255, 238, 170, 60))
d.rectangle([1060, 56, 1570, 440], outline=(120, 126, 132), width=10)
# enamel blue wall
d.rectangle([0, 0, 1060, 480], fill=BLUE)
d.rectangle([0, 428, 1060, 480], fill=(28, 64, 102))
# title board above the hooks, carrying the name (ship); v1 lettering goes on the timetable board
base = __file__.rsplit("/", 1)[0]
name = "analyze-tls-fingerprint"
f = ImageFont.truetype(base + "/fonts/BIZ-UDMincho.ttf", 40)
d.rectangle([70, 52, 700, 118], fill=(24, 60, 98), outline=STEEL, width=3)
if A != "--v1": d.text((385, 85), name, font=f, fill=WHITE, anchor="mm")
# hooks and hanging clipboards
for hx in (130, 280, 430):
    d.ellipse([hx - 7, 150, hx + 7, 164], fill=STEEL)
    d.rectangle([hx - 54, 164, hx + 54, 310], fill=(30, 68, 108), outline=(18, 48, 78), width=3)
    d.rectangle([hx - 36, 184, hx + 36, 292], fill=WHITE)
    d.rectangle([hx - 17, 158, hx + 17, 178], fill=STEEL)
# timetable board, frame up, columns turned away from the viewer
d.rectangle([600, 150, 990, 330], fill=(104, 88, 66))
d.rectangle([614, 164, 976, 316], fill=(130, 114, 90))
if A == "--v1":
    fb = ImageFont.truetype(base + "/fonts/BIZ-UDMincho.ttf", 30)
    d.text((795, 240), name, font=fb, fill=WHITE, anchor="mm")
if A == "--v2":  # v2 flaw: figures on the hanging sheets
    for hx in (130, 280, 430):
        for yy in (206, 238, 268): d.line([(hx - 26, yy), (hx + 26, yy)], fill=(60, 60, 60), width=4)
# desk: kettle, coat hook with one coat, stack of spare sheets
d.rectangle([560, 372, 1030, 396], fill=(110, 84, 56))
d.rectangle([596, 396, 620, 480], fill=(92, 70, 46)); d.rectangle([980, 396, 1004, 480], fill=(92, 70, 46))
for i in range(5): d.rectangle([640, 348 - i * 5, 792, 354 - i * 5], fill=(250, 249, 244), outline=(200, 200, 194), width=1)
d.polygon([(872, 372), (872, 330), (888, 314), (932, 314), (948, 330), (948, 372)], fill=(70, 72, 76))
d.ellipse([516, 140, 530, 154], fill=STEEL)
d.polygon([(492, 154), (544, 154), (558, 272), (530, 282), (506, 272)], fill=(84, 70, 58))
# floor and the row of empty chairs
d.rectangle([0, 480, W, H], fill=(168, 156, 138))
for x in range(0, W, 120): d.line([(x, 480), (x - 60, H)], fill=(150, 138, 118), width=3)
def chair(x, y, s):
    d.rectangle([x, y - 118 * s, x + 12 * s, y], fill=WOOD); d.rectangle([x + 88 * s, y - 118 * s, x + 100 * s, y], fill=WOOD)
    d.rectangle([x - 6 * s, y - 58 * s, x + 106 * s, y - 42 * s], fill=(158, 120, 80))
    d.rectangle([x, y - 126 * s, x + 100 * s, y - 110 * s], fill=WOOD)
chair(660, 580, 1.05); chair(880, 568, .98)
# nearest chair with the clipboard face up, first printed row still blank
chair(150, 648, 1.55)
d.polygon([(206, 500), (330, 488), (346, 606), (222, 618)], fill=BLUE)
d.polygon([(218, 512), (320, 502), (332, 592), (230, 602)], fill=(250, 249, 244))
for i in range(3): d.rectangle([238 + i * 28, 528, 258 + i * 28, 548], outline=(120, 122, 120), width=2)
d.line([(240, 566), (322, 558)], fill=(214, 216, 212), width=2)
d.polygon([(246, 480), (298, 476), (302, 500), (250, 504)], fill=STEEL)
d.line([(252, 484), (296, 480)], fill=(238, 242, 244), width=4)
img.save(sys.argv[2] if len(sys.argv) > 2 else "banner.png")
print("banner saved")
