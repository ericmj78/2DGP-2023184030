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


def move_top():
    for x in range(50,751,5):
        draw_character(x,550)


def move_right():
    for y in range(550,49,-5):
        draw_character(750,y)


def move_bottom():
    for x in range(750,49,-5):
        draw_character(x,50)

def move_left():
    for y in range(50,551,5):
        draw_character(50,y)

        
def move_rectangle():
    print("RECTANGLE")

    move_top()
    move_right()
    move_bottom()
    move_left()



def move_triangle():
    print("TRIANGLE")

    # 아래쪽 변: (100, 100)에서 (700, 100)으로 이동
    for x in range(100, 701, 5):
        draw_character(x, 100)

    count = 100

    # 오른쪽 변: (700, 100)에서 (400, 500)으로 이동
    for step in range(count + 1):
        t = step / count
        x = 700 + (400 - 700) * t
        y = 100 + (500 - 100) * t
        draw_character(x, y)

    # 왼쪽 변: (400, 500)에서 (100, 100)으로 이동
    for step in range(count + 1):
        t = step / count
        x = 400 + (100 - 400) * t
        y = 500 + (100 - 500) * t
        draw_character(x, y)





while True:
    move_circle()
    move_rectangle()
    move_triangle()


close_canvas()