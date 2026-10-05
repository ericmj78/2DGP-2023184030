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
    get_time,
    load_image,
    open_canvas,
    update_canvas,
)

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SPRITE_SCALE = 8
REPEATS_PER_ACTION = 5


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
    Animation('시트 2행', 407, 12, (
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
    Animation('시트 4행', 325, 12, (
        Frame(1, 326, 29, 30),
        Frame(35, 327, 29, 31),
        Frame(67, 327, 30, 29),
        Frame(98, 327, 31, 29),
        Frame(131, 327, 29, 30),
        Frame(162, 326, 29, 31),
        Frame(193, 326, 30, 29),
        Frame(230, 326, 31, 29),
        Frame(268, 325, 30, 30),
    )),
    Animation('시트 5행', 292, 12, (
        Frame(1, 292, 30, 27),
        Frame(36, 292, 29, 27),
        Frame(70, 292, 29, 27),
        Frame(105, 292, 29, 27),
        Frame(139, 292, 29, 27),
        Frame(174, 292, 29, 27),
    )),
    Animation('시트 6행', 251, 10, (
        Frame(1, 251, 29, 35),
        Frame(36, 251, 30, 35),
        Frame(74, 251, 31, 35),
        Frame(111, 251, 31, 36),
        Frame(149, 251, 30, 35),
        Frame(186, 251, 31, 36),
    )),
    Animation('시트 7행', 207, 10, (
        Frame(1, 207, 29, 35),
        Frame(36, 207, 30, 35),
        Frame(72, 208, 39, 31),
        Frame(123, 208, 39, 32),
        Frame(172, 208, 39, 31),
        Frame(218, 208, 38, 32),
    )),
    Animation('시트 8행', 154, 10, (
        Frame(1, 154, 24, 45),
        Frame(31, 154, 29, 44),
        Frame(65, 154, 20, 44),
        Frame(90, 155, 25, 43),
        Frame(119, 155, 25, 43),
        Frame(149, 154, 20, 44),
        Frame(184, 156, 40, 28),
        Frame(232, 157, 39, 27),
    )),
    Animation('시트 9행', 108, 10, (
        Frame(1, 108, 27, 38),
        Frame(31, 110, 31, 36),
        Frame(64, 110, 31, 36),
        Frame(99, 110, 33, 38),
        Frame(136, 110, 32, 36),
        Frame(176, 110, 33, 36),
        Frame(217, 110, 33, 36),
        Frame(254, 111, 33, 36),
    )),
    Animation('시트 10행', 56, 10, (
        Frame(6, 56, 34, 40),
        Frame(49, 56, 34, 43),
        Frame(96, 59, 23, 39),
        Frame(125, 59, 23, 39),
    )),
    # 다음 시트 행의 애니메이션을 여기에 추가한다.
)


@dataclass
class Playback:
    action_index: int = 0
    frame_index: int = 0
    completed_repeats: int = 0
    finished: bool = False
    elapsed: float = 0.0

    def update(self, dt: float) -> None:
        self.elapsed += max(0.0, dt)
        frame_interval = 1 / ANIMATIONS[self.action_index].fps
        frame_count = len(ANIMATIONS[self.action_index].frames)
        while self.elapsed >= frame_interval and not self.finished:
            self.elapsed -= frame_interval
            if self.frame_index + 1 < frame_count:
                self.frame_index += 1
            else:
                self.completed_repeats += 1
                if self.completed_repeats == REPEATS_PER_ACTION:
                    self.finished = True
                else:
                    self.frame_index = 0

def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sheet_path = Path(__file__).resolve().parent / 'sonic-sprite.png'
        sheet = load_image(str(sheet_path))
        player = Playback()
        last_time = get_time()
        running = True
        while running:
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False
            now = get_time()
            player.update(now - last_time)
            last_time = now
            animation = ANIMATIONS[player.action_index]
            frame = animation.frames[player.frame_index]
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













