from pathlib import Path
from pico2d import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
sheet = load_image(str(Path(__file__).resolve().with_name('freedino_spritesheet.png')))
clear_canvas()
sheet.clip_draw(0, sheet.h - 472, 680, 472, 400, 300, 680, 472)
update_canvas()
delay(2)
close_canvas()
