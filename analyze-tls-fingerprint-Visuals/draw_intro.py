#!/usr/bin/env python3
"""analyze-tls-fingerprint intro: the examiner's waiting area before the first candidate,
pure scenery, nothing that can be read. Foreground: the nearest chair at close focus, its
wooden seat worn smooth, a clipboard resting on it with its sheet blank side showing a faint
printed grid too soft to read, the steel clip catching the window light. Midground: the row
of chairs, hooks on the enamel blue wall with hanging boards, spare sheets stacked on the
desk, a coat on its hook, the timetable frame turned so its face is hidden. Background: the
window and the wet road beyond, junction markings, a waiting car at the kerb with headlamps
lit in the grey morning, a pale coastal sky over rooftops."""
import random, sys
from PIL import Image, ImageDraw
random.seed(31)
A = sys.argv[1] if len(sys.argv) > 1 else ""
W, H = 1600, 680
BLUE = (36, 80, 126); WHITE = (247, 245, 238); RUST = (180, 85, 45); STEEL = (150, 154, 158); WOOD = (146, 110, 74)
img = Image.new("RGB", (W, H), (198, 204, 208)); d = ImageDraw.Draw(img, "RGBA")
# window and wet road, right background
d.rectangle([1010, 60, 1560, 430], fill=(176, 188, 196))
for (rx, ry, rw) in [(1080, 330, 130), (1260, 318, 170), (1470, 330, 110)]:  # distant rooftops
    d.polygon([(rx, ry), (rx + rw // 2, ry - 44), (rx + rw, ry), (rx + rw, ry + 60), (rx, ry + 60)], fill=(140, 150, 158))
d.rectangle([1010, 300, 1560, 430], fill=(58, 60, 62))  # wet asphalt
for i in range(6):  # junction markings and a give way pair of dashes
    d.line([(1060 + i * 84, 392), (1110 + i * 84, 392)], fill=(240, 240, 236), width=7)
d.line([(1180, 330), (1400, 330)], fill=(240, 240, 236), width=4)
for (x, y) in [(1210, 356), (1268, 356), (1330, 356), (1388, 356)]:
    d.polygon([(x, y), (x + 22, y), (x + 11, y + 16)], fill=(240, 240, 236))
# waiting car at the kerb, driver invisible, headlamps lit
d.polygon([(1150, 268), (1210, 226), (1330, 226), (1396, 268), (1396, 306), (1150, 306)], fill=(70, 76, 84))
d.rectangle([1226, 234, 1320, 262], fill=(168, 182, 192))
for hx in (1176, 1352):
    d.ellipse([hx - 17, 278, hx + 17, 300], fill=(255, 238, 170)); d.ellipse([hx - 30, 272, hx + 30, 306], fill=(255, 238, 170, 60))
d.rectangle([1010, 60, 1560, 430], outline=(120, 126, 132), width=10)
d.line([(1285, 60), (1285, 430)], fill=(120, 126, 132), width=8)
# enamel blue wall, left and centre
d.rectangle([0, 0, 1010, 470], fill=BLUE)
d.rectangle([0, 420, 1010, 470], fill=(28, 64, 102))
# timetable frame on the wall, face turned hidden against the plaster (v1 shows its columns)
d.rectangle([600, 96, 940, 300], fill=(104, 88, 66))
d.rectangle([614, 110, 926, 286], fill=(128, 112, 88))
if A == "--v1":
    for yy in range(134, 280, 26): d.line([(636, yy), (904, yy)], fill=(240, 238, 230), width=6)
    for xx in (700, 780, 850): d.line([(xx, 116), (xx, 280)], fill=(240, 238, 230), width=4)
# hooks with hanging boards
for hx in (120, 250, 380):
    d.ellipse([hx - 7, 108, hx + 7, 122], fill=STEEL)
    d.rectangle([hx - 52, 122, hx + 52, 262], fill=(30, 68, 108), outline=(18, 48, 78), width=3)
    d.rectangle([hx - 34, 140, hx + 34, 244], fill=WHITE)
    d.rectangle([hx - 16, 116, hx + 16, 134], fill=STEEL)
# desk with a stack of spare sheets and a kettle
d.rectangle([560, 356, 990, 380], fill=(110, 84, 56))
d.rectangle([600, 380, 624, 470], fill=(92, 70, 46)); d.rectangle([940, 380, 964, 470], fill=(92, 70, 46))
for i in range(5): d.rectangle([648, 330 - i * 5, 800, 336 - i * 5], fill=(250, 249, 244), outline=(200, 200, 194), width=1)
d.polygon([(856, 356), (856, 316), (872, 300), (916, 300), (932, 316), (932, 356)], fill=(70, 72, 76))  # kettle
d.arc([916, 312, 962, 348], 270, 90, fill=(70, 72, 76), width=5)
# coat on its hook
d.ellipse([486, 104, 500, 118], fill=STEEL)
d.polygon([(462, 118), (514, 118), (528, 236), (500, 246), (476, 236)], fill=(84, 70, 58))
# floor
d.rectangle([0, 470, W, H], fill=(168, 156, 138))
for x in range(0, W, 120): d.line([(x, 470), (x - 60, H)], fill=(150, 138, 118), width=3)
# row of plain chairs midground
def chair(x, y, s):
    d.rectangle([x, y - 120 * s, x + 12 * s, y], fill=WOOD)
    d.rectangle([x + 88 * s, y - 120 * s, x + 100 * s, y], fill=WOOD)
    d.rectangle([x - 6 * s, y - 60 * s, x + 106 * s, y - 44 * s], fill=(158, 120, 80))
    d.rectangle([x, y - 128 * s, x + 100 * s, y - 112 * s], fill=WOOD)
for (x, y, s) in [(90, 560, 1.0), (300, 548, .94), (500, 538, .88)]:
    if (x, y, s) == (90, 560, 1.0): continue
    chair(x, y, s)
# nearest chair at close focus, foreground left, clipboard resting on its seat
chair(120, 640, 1.7)
# clipboard on the seat: blue board, blank sheet with a faint grid too soft to read, steel clip
d.polygon([(196, 452), (330, 438), (348, 566), (214, 580)], fill=BLUE)
d.polygon([(208, 464), (320, 452), (334, 552), (222, 564)], fill=(250, 249, 244))
for i in range(5):
    yy = 482 + i * 15; d.line([(220, yy), (326, yy - 10)], fill=(226, 228, 224), width=2)
d.polygon([(238, 430), (292, 426), (296, 452), (242, 456)], fill=STEEL)
d.line([(244, 434), (290, 430)], fill=(236, 240, 242), width=4)  # clip catching the window light
if A == "--v2":  # v2 flaw: a printed row with box marks on the sheet, readable as a form entry
    for i in range(3): d.rectangle([228 + i * 30, 492, 250 + i * 30, 512], outline=(60, 60, 60), width=3)
    d.line([(228, 530), (322, 522)], fill=(60, 60, 60), width=4)
img.save(sys.argv[2] if len(sys.argv) > 2 else "intro-banner.png")
print("intro saved")
