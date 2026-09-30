from pathlib import Path
from pico2d import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_WIDTH = 680
FRAME_HEIGHT = 472
COLUMNS = 8
ANIMATIONS = (
    ('Idle', 0, 10, (7, 31, 381, 425)),
    ('Walk', 2, 10, (0, 11, 377, 457)),
    ('Run', 4, 8, (9, 5, 451, 460)),
    ('Jump', 5, 12, (7, 18, 453, 472)),
    ('Dead', 7, 8, (33, 69, 665, 471)),
)

def draw_frame(sheet, animation, frame_index):
    left, top, right, bottom = animation[3]
    scale = max(420 / (right - left), 310 / (bottom - top))
    row = animation[1] + frame_index // COLUMNS
    column = frame_index % COLUMNS
    source_bottom = sheet.h - (row + 1) * FRAME_HEIGHT
    draw_x = CANVAS_WIDTH / 2 + (FRAME_WIDTH / 2 - (left + right) / 2) * scale
    draw_y = CANVAS_HEIGHT / 2 - (FRAME_HEIGHT / 2 - (top + bottom) / 2) * scale
    sheet.clip_draw(column * FRAME_WIDTH, source_bottom, FRAME_WIDTH, FRAME_HEIGHT, draw_x, draw_y, FRAME_WIDTH * scale, FRAME_HEIGHT * scale)

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sheet = load_image(str(Path(__file__).resolve().with_name('freedino_spritesheet.png')))
for animation in ANIMATIONS:
    for frame_index in range(animation[2]):
        clear_canvas()
        draw_frame(sheet, animation, frame_index)
        update_canvas()
        delay(0.08)
close_canvas()
