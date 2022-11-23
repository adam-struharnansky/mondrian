import random
from mondrian_color import *

MIN_SIZE = 20


def generate_square(t, width, height, x, y):
    if random.randint(0, 2) == 1:
        t.rectangle(width, height, 'black', mondrian_random())
    else:
        a = random.randint(MIN_SIZE, width - MIN_SIZE)
        b = random.randint(MIN_SIZE, height - MIN_SIZE)
        t.rectangle(a, b, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])
        t.jump_by(b, 0)
        t.rectangle(a, height - b, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])
        t.jump_by(0, a)
        t.rectangle(width - a, height - b, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])
        t.jump_by(-b, 0)
        t.rectangle(width - a, b, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])


def for_mondrian(t, width, height, x, y):
    t.jump_to(x, y)
    t.rectangle(width, height, mondrian_black(), mondrian_white())
    generate_square(t, width / 2, height / 2, x, y)
    t.jump_to(x + width / 2, y)
    generate_square(t,  width / 2, height / 2, x + width / 2, y)
    t.jump_to(x + width / 2, y + height / 2)
    generate_square(t,  width / 2, height / 2, x + width / 2, y + height / 2)
    t.jump_to(x, y + height / 2)
    generate_square(t,  width / 2, height / 2, x, y + height / 2)
