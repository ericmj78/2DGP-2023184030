# 실습 과제 진행
from pico2d import *
import math

open_canvas(800,600)

character = load_image('character.png')

def draw_character(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.01)



def move_circle():
    print("CIRCLE")
    
    for degree in range(360):
        radian = math.radians(degree)
        x = 400 + 200*math.cos(radian)
        y = 300 + 200*math.sin(radian)
        draw_character(x,y)

    
def move_rectangle():
    print("RECTANGLE")
    pass

def move_triangle():
    print("TRIANGLE")
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass


cloase_canvas()