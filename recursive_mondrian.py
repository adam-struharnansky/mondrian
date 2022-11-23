from myTurtle_A import *
from myColor import *
from mondrian_color import *
import turtle
import random

MIN_SIZE = 80


def recursive_mondrian(t, width, height, x, y):
    t.jump_to(x, y)
    t.setheading(90)
    if rr(0, 3):
        t.rectangle(height, width, MyColor('black'), MyColor('white'))
    else:
        t.rectangle(height, width, MyColor('black'), mondrian_random())

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

