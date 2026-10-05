"""LEC09 Sonic 스프라이트 시트 애니메이션 뷰어."""

from pico2d import (
    SDL_KEYDOWN,
    SDL_QUIT,
    SDLK_ESCAPE,
    clear_canvas,
    close_canvas,
    delay,
    get_events,
    open_canvas,
    update_canvas,
)

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        running = True
        while running:
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False
            clear_canvas()
            update_canvas()
            delay(1 / 60)
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
