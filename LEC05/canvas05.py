from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

y = 100
x = 200
while x < 600:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    update_canvas()
    x += 4
    delay(0.01)

while y < 400:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(600, y)
    update_canvas()
    y += 4
    delay(0.01)

while x > 200:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 400)
    update_canvas()
    x -= 4
    delay(0.01)

while y > 100:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(200, y)
    update_canvas()
    y -= 4
    delay(0.01)

grass.draw(400, 30)
character.draw(400, 90)
update_canvas()
delay(5)
close_canvas()