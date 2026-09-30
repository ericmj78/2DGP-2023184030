from pathlib import Path
from pico2d import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_WIDTH = 680
FRAME_HEIGHT = 472
COLUMNS = 8
open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sheet = load_image(str(Path(__file__).resolve().with_name('freedino_spritesheet.png')))
for frame in range(8):
    clear_canvas()
    sheet.clip_draw(frame % COLUMNS * FRAME_WIDTH, sheet.h - FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT, 400, 300, FRAME_WIDTH, FRAME_HEIGHT)
    update_canvas()
    delay(0.08)
close_canvas()
