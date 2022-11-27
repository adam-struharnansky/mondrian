import math

from mondrian_color import *
import random

MIN_SIZE = 80
WHITE_TO_COLOR_RATIO = 3
FILL_STOP_RATIO = 0.5
STOP_RATIO = 0.7

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
        if rr(0, WHITE_TO_COLOR_RATIO):
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


def recursive_mondrian_stop(t, width, height, x, y, fill):
    t.jump_to(x, y)
    t.setheading(90)
    new_fill = fill
    if fill:
        if rr(0, WHITE_TO_COLOR_RATIO):
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
        if random_bool(STOP_RATIO):
            recursive_mondrian_stop(t, b, height, x, y, new_fill)
        if random_bool(STOP_RATIO):
            recursive_mondrian_stop(t, width - b, height, x + b, y, new_fill)
    else:
        b = random.uniform(MIN_SIZE / 2, height - MIN_SIZE / 2)
        t.jump_to(x, y + b)
        t.setheading(0)
        t.fd(width)
        if random_bool(STOP_RATIO):
            recursive_mondrian_stop(t, width, b, x, y, new_fill)
        if random_bool(STOP_RATIO):
            recursive_mondrian_stop(t, width, height - b, x, y + b, new_fill)


def advanced_chunk_mondrian(t, a, b, x, y, depth=4, counter=0):
    MIN_SIZE = 30
    if counter == depth:
        return

    t.jump_to(x, y)

    if a - MIN_SIZE < MIN_SIZE or b - MIN_SIZE < MIN_SIZE:
        t.rectangle(a, b, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])
        return

    r = random.randint(0, 2)
    if counter == 0:
        r = 0

    if r != 1:
        t.rectangle(a, b, mondrian_black(), mondrian_white())
        newA = random.randint(MIN_SIZE, a - MIN_SIZE)
        newB = random.randint(MIN_SIZE, b - MIN_SIZE)

        if newA + int(newB/2) < newB:
            newB -= int(newB/2)
        elif newB + int(newA/2) < newA:
            newA -= int(newA/2)

        advanced_chunk_mondrian(t, newA, newB, x, y, depth, counter + 1)
        advanced_chunk_mondrian(t, newA, b - newB, x + newB, y, depth, counter + 1)
        advanced_chunk_mondrian(t, a - newA, b - newB, x + newB, y + newA, depth, counter + 1)
        advanced_chunk_mondrian(t, a - newA, newB, x, y + newA, depth, counter + 1)
    else:
        t.rectangle(a, b, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])


def diamond_mondrian(t, a, b, x, y, depth=4, width=14):
    t.width(width)
    advanced_chunk_mondrian(t, a, b, x, y, depth=depth)
    t.jump_to((x + b/2), y)
    t.setheading(90)
    t.rt(45)
    for i in range(4):
        t.rectangle(a, b, 'white', 'white')
        t.jump_fd(math.sqrt((a/2) ** 2 + (b/2) ** 2))
        t.lt(90)
