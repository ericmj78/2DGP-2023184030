from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')


def draw_position(position):
    clear_canvas()
    character.draw(*position)
    update_canvas()
    delay(0.01)


def circle_path():
    center = (400, 300)
    radius = 200
    for degree in range(360):
        angle = math.radians(degree)
        yield (center[0] + radius * math.cos(angle),
               center[1] + radius * math.sin(angle))


def line_path(start, end):
    distance = math.hypot(end[0] - start[0], end[1] - start[1])
    steps = int(distance / 5)
    for step in range(steps + 1):
        ratio = step / steps
        x = start[0] + (end[0] - start[0]) * ratio
        y = start[1] + (end[1] - start[1]) * ratio
        yield (x, y)


def polygon_path(corners):
    for index, start in enumerate(corners):
        end = corners[(index + 1) % len(corners)]
        yield from line_path(start, end)


def rectangle_path():
    corners = [(50, 550), (750, 550), (750, 50), (50, 50)]
    yield from polygon_path(corners)


def triangle_path():
    corners = [(100, 100), (700, 100), (400, 500)]
    yield from polygon_path(corners)


while True:
    for path in (circle_path(), rectangle_path(), triangle_path()):
        for position in path:
            draw_position(position)


close_canvas()
