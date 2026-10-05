"""LEC09 Sonic 스프라이트 시트 애니메이션 뷰어."""

from dataclasses import dataclass
from pathlib import Path

from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    clear_canvas,
    close_canvas,
    delay,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
)

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SPRITE_SCALE = 8


@dataclass(frozen=True)
class Frame:
    left: int
    bottom: int
    width: int
    height: int
    offset_x: int = 0
    offset_y: int = 0


@dataclass(frozen=True)
class Animation:
    name: str
    baseline_bottom: int
    fps: float
    frames: tuple[Frame, ...]


ANIMATIONS = (
    Animation('시트 1행', 447, 10, (
        Frame(1, 447, 29, 39),
        Frame(31, 447, 26, 38),
        Frame(58, 447, 29, 39),
        Frame(87, 447, 29, 38),
        Frame(118, 447, 30, 38),
        Frame(150, 447, 30, 38),
        Frame(182, 447, 30, 38),
        Frame(212, 448, 29, 38),
        Frame(241, 448, 28, 38),
        Frame(270, 448, 24, 32),
        Frame(302, 448, 29, 26),
    )),
    Animation('시트 2행', 407, 10, (
        Frame(8, 408, 26, 37),
        Frame(37, 408, 27, 37),
        Frame(65, 407, 31, 38),
        Frame(97, 408, 37, 37),
        Frame(135, 410, 32, 35),
        Frame(170, 408, 32, 38),
        Frame(206, 408, 26, 38),
        Frame(238, 408, 24, 37),
        Frame(263, 408, 30, 37),
        Frame(295, 408, 36, 37),
        Frame(334, 409, 32, 36),
        Frame(370, 408, 29, 38),
    )),
    Animation('시트 3행', 361, 10, (
        Frame(1, 361, 33, 40),
        Frame(39, 362, 35, 39),
        Frame(89, 362, 35, 38),
        Frame(130, 362, 34, 42),
        Frame(181, 362, 34, 41),
        Frame(228, 363, 33, 40),
    )),
    # 다음 시트 행의 애니메이션을 여기에 추가한다.
)


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sheet_path = Path(__file__).resolve().parent / 'sonic-sprite.png'
        sheet = load_image(str(sheet_path))
        animation = ANIMATIONS[0]
        frame = animation.frames[0]
        running = True
        while running:
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False
            clear_canvas()
            sheet.clip_draw(
                frame.left, frame.bottom, frame.width, frame.height,
                CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
                frame.width * SPRITE_SCALE, frame.height * SPRITE_SCALE,
            )
            update_canvas()
            delay(1 / 60)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()



