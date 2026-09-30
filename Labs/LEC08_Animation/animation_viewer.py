from pathlib import Path
from pico2d import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_WIDTH = 680
FRAME_HEIGHT = 472
COLUMNS = 8
open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sheet = load_image(str(Path(__file__).resolve().with_name('freedino_spritesheet.png')))
clear_canvas()
frame = 0
column = frame % COLUMNS
row = frame // COLUMNS
sheet.clip_draw(column * FRAME_WIDTH, sheet.h - (row + 1) * FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT, 400, 300, FRAME_WIDTH, FRAME_HEIGHT)
update_canvas()
delay(2)
close_canvas()
