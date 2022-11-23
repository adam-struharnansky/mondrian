from mondrian_color import *
import random

MIN_SIZE = 80
WHITE_TO_COLOR_RATIO = 3
FILL_STOP_RATIO = 0.5


def recursive_mondrian(t, width, height, x, y):
    t.jump_to(x, y)
    t.setheading(90)
    if rr(0, WHITE_TO_COLOR_RATIO):
        t.rectangle(height, width, mondrian_black(), mondrian_white())
    else:
        t.rectangle(height, width, mondrian_black(), mondrian_random())

    if width < MIN_SIZE or height < MIN_SIZE:
        return

    if rr(0, 2):
        b = random.uniform(MIN_SIZE/2, width - MIN_SIZE/2)
        recursive_mondrian(t, b, height, x, y)
        recursive_mondrian(t, width - b, height, x + b, y)
    else:
        b = random.uniform(MIN_SIZE/2, height - MIN_SIZE/2)
        recursive_mondrian(t, width, b, x, y)
        recursive_mondrian(t, width, height - b, x, y + b)


def random_bool(true_ratio):
    return random.uniform(0, 1) < true_ratio


def recursive_mondrian_filling(t, width, height, x, y, fill):
    t.jump_to(x, y)
    t.setheading(90)
    new_fill = fill
    if fill:
        if rr(0, WHITE_TO_COLOR_RATIO) or not fill:
            t.rectangle(height, width, mondrian_black(), mondrian_white())
        else:
            t.rectangle(height, width, mondrian_black(), mondrian_random())
            if width < 2.5 * MIN_SIZE or height < 2.5 * MIN_SIZE:
                new_fill = random_bool(FILL_STOP_RATIO)

    if width < MIN_SIZE or height < MIN_SIZE:
        return

    if rr(0, 2):
        b = random.uniform(MIN_SIZE / 2, width - MIN_SIZE / 2)
        t.jump_to(x + b, y)
        t.setheading(90)
        t.fd(height)
        recursive_mondrian_filling(t, b, height, x, y, new_fill)
        recursive_mondrian_filling(t, width - b, height, x + b, y, new_fill)
    else:
        b = random.uniform(MIN_SIZE / 2, height - MIN_SIZE / 2)
        t.jump_to(x, y + b)
        t.setheading(0)
        t.fd(width)
        recursive_mondrian_filling(t, width, b, x, y, new_fill)
        recursive_mondrian_filling(t, width, height - b, x, y + b, new_fill)
