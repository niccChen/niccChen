"""Draw a pixel workspace in front of the light Banff landscape."""
import math

from PIL import ImageDraw

from banff_banner import make_frame as landscape_frame
from build_assets import WIDTH, FONTS, BANNER_SECONDS, rect, text


def make_frame(t):
    img = landscape_frame(t)
    d = ImageDraw.Draw(img)
    phase = math.tau * t / BANNER_SECONDS

    # A broad sill places the landscape outside, and a quiet work corner inside.
    rect(d, 0, 267, WIDTH, 43, "#f1f7f6")
    rect(d, 0, 262, WIDTH, 4, "#f8fcfb")
    rect(d, 0, 266, WIDTH, 1, "#d9e6e3")
    rect(d, 419, 296, 239, 3, "#e2ece8")

    # Slim desk: desaturated oak keeps the pale blue-green palette cohesive.
    rect(d, 422, 248, 236, 6, "#cbd0bc")
    rect(d, 422, 254, 236, 4, "#a4b3a4")
    rect(d, 432, 258, 7, 38, "#96aba2")
    rect(d, 641, 258, 7, 38, "#96aba2")
    rect(d, 439, 258, 202, 3, "#d8e3dc")

    # Laptop with code and a small research plot, rather than a productivity label.
    rect(d, 490, 191, 83, 51, "#577b86")
    rect(d, 487, 194, 89, 45, "#577b86")
    rect(d, 493, 197, 77, 39, "#2f5362")
    rect(d, 496, 200, 71, 3, "#466a78")
    for x, c in [(498, "#b7d9d1"), (503, "#d1d9bb"), (508, "#d8bdaf")]:
        rect(d, x, 200, 2, 2, c)
    for x, y, w, c in [
        (499, 209, 10, "#a5d5c6"), (513, 209, 15, "#e0d5b7"),
        (503, 215, 21, "#b8d4df"), (507, 221, 11, "#b8d4df"),
        (522, 221, 8, "#b2c99d"), (503, 227, 14, "#a5d5c6"),
    ]:
        rect(d, x, y, w, 2, c)
    if math.sin(phase * 2) > 0:
        rect(d, 520, 227, 2, 3, "#dfecd9")
    rect(d, 538, 210, 1, 20, "#658794")
    rect(d, 538, 230, 26, 1, "#658794")
    for x, y, w in [(542, 225, 5), (546, 222, 5), (550, 225, 4), (553, 217, 4), (556, 212, 6)]:
        rect(d, x, y, w, 2, "#b4ddcc")
    rect(d, 483, 241, 97, 4, "#a2b8bf")
    rect(d, 480, 245, 103, 3, "#7998a2")
    rect(d, 522, 242, 21, 2, "#ccdbdf")

    # An open notebook with a diagram and a pencil suggests thoughtful work.
    rect(d, 584, 238, 43, 10, "#9aafa8")
    rect(d, 587, 234, 17, 12, "#ffffff")
    rect(d, 604, 236, 20, 10, "#f8fbf3")
    rect(d, 603, 236, 1, 10, "#c7d7cd")
    for y, w in [(238, 9), (241, 11), (244, 6)]:
        rect(d, 590, y, w, 1, "#9eb5b9")
    rect(d, 608, 239, 3, 3, "#a1bfc4")
    rect(d, 617, 242, 3, 3, "#b5c7ad")
    rect(d, 610, 241, 7, 1, "#b8cdc8")
    rect(d, 593, 232, 19, 2, "#bb9b7f")
    rect(d, 610, 232, 3, 2, "#6b7a76")

    # A ceramic mug, tiny steam movement, and a plant bring a little everyday life.
    rect(d, 452, 228, 20, 17, "#c6a697")
    rect(d, 455, 245, 14, 3, "#b48e7d")
    rect(d, 472, 231, 6, 11, "#c6a697")
    rect(d, 472, 234, 3, 5, "#e4efeb")
    rect(d, 452, 226, 20, 3, "#e8d5c4")
    rect(d, 455, 227, 14, 1, "#a18a78")
    drift = round(math.sin(phase) * 2)
    rect(d, 461 + drift, 211, 2, 8, "#ffffff")
    rect(d, 463 + drift, 207, 2, 4, "#ffffff")
    rect(d, 633, 233, 17, 3, "#f6eee3")
    rect(d, 635, 236, 13, 12, "#d6c5ae")
    rect(d, 641, 213, 2, 20, "#8dac94")
    rect(d, 633, 216, 9, 4, "#a0b99a")
    rect(d, 629, 212, 9, 4, "#a0b99a")
    rect(d, 643, 207, 9, 5, "#a7c3a2")
    rect(d, 648, 203, 7, 4, "#a7c3a2")
    rect(d, 640, 205, 3, 8, "#90ae93")

    text(d, (29, 278), "Research · Engineering", FONTS["small"], "#456873")
    return img
