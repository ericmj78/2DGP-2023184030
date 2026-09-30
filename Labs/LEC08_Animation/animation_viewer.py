"""Show every dinosaur animation from the sprite sheet in the center."""

import json
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


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAMES_PER_SECOND = 12
REPEAT_COUNT = 5
PAUSE_SECONDS = 1.0


def draw_frame(sheet, animation, frame):
    """Crop a variable size frame and keep its character position stable."""
    left, top, right, bottom = animation["union_bbox"]
    scale = max(420 / (right - left), 310 / (bottom - top))

    frame_left, frame_top, frame_right, frame_bottom = frame["source_bbox"]
    center_x = CANVAS_WIDTH / 2 + (
        (frame_left + frame_right - left - right) / 2
    ) * scale
    center_y = CANVAS_HEIGHT / 2 - (
        (frame_top + frame_bottom - top - bottom) / 2
    ) * scale

    # 프레임마다 다른 잘라낼 크기를 사용한다. (추가점수: 가변 프레임 크기)
    sheet.clip_draw(
        frame["left"], frame["bottom"], frame["width"], frame["height"],
        center_x, center_y, frame["width"] * scale, frame["height"] * scale,
    )


def main():
    asset_dir = Path(__file__).resolve().parent
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        with (asset_dir / "dino_frames.json").open(encoding="utf-8") as data_file:
            data = json.load(data_file)
        sheet = load_image(str(asset_dir / data["sprite_sheet"]))
        animations = data["animations"]

        animation_index = 0
        elapsed = 0.0
        previous_time = get_time()
        running = True

        while running:
            for event in get_events():
                if event.type == SDL_QUIT or (
                    event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
                ):
                    running = False
            if not running:
                break

            now = get_time()
            elapsed += now - previous_time
            previous_time = now

            while True:
                animation = animations[animation_index]
                frames = animation["frames"]
                # 동작마다 프레임 수가 달라도 각 동작을 정확히 5회 재생한다.
                play_seconds = len(frames) * REPEAT_COUNT / FRAMES_PER_SECOND
                if elapsed < play_seconds + PAUSE_SECONDS:
                    break
                elapsed -= play_seconds + PAUSE_SECONDS
                animation_index = (animation_index + 1) % len(animations)

            if elapsed < play_seconds:
                frame_index = int(elapsed * FRAMES_PER_SECOND) % len(frames)
            else:
                frame_index = len(frames) - 1  # 1초 동안 마지막 프레임 유지

            clear_canvas()
            draw_frame(sheet, animation, frames[frame_index])
            update_canvas()
            delay(0.01)
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
