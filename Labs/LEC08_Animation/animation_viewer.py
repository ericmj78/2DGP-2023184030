from pathlib import Path
from pico2d import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_WIDTH = 680
FRAME_HEIGHT = 472
COLUMNS = 8
def draw_frame(sheet, frame):
    column = frame % COLUMNS
    row = frame // COLUMNS
    source_left = column * FRAME_WIDTH
    source_bottom = sheet.h - (row + 1) * FRAME_HEIGHT
    scale = max(420 / (381 - 7), 310 / (425 - 31))
    draw_x = CANVAS_WIDTH / 2 + (FRAME_WIDTH / 2 - (7 + 381) / 2) * scale
    draw_y = CANVAS_HEIGHT / 2 - (FRAME_HEIGHT / 2 - (31 + 425) / 2) * scale
    draw_width = FRAME_WIDTH * scale
    draw_height = FRAME_HEIGHT * scale
    sheet.clip_draw(source_left, source_bottom, FRAME_WIDTH, FRAME_HEIGHT, draw_x, draw_y, draw_width, draw_height)

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sheet = load_image(str(Path(__file__).resolve().with_name('freedino_spritesheet.png')))
for frame in range(10):
    clear_canvas()
    draw_frame(sheet, frame)
    update_canvas()
    delay(0.08)
close_canvas()
