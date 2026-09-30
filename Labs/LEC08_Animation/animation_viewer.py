from pico2d import *

open_canvas(800, 600)
sheet = load_image('freedino_spritesheet.png')
clear_canvas()
sheet.clip_draw(0, sheet.h - 472, 680, 472, 400, 300, 680, 472)
update_canvas()
delay(2)
close_canvas()
