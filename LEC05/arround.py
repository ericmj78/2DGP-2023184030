from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

center_x = 400
center_y = 300
radius = 200
degree = 0

while degree < 360:
    angle = math.radians(degree)

    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()

    degree += 2
    delay(0.01)

delay(1)
close_canvas()