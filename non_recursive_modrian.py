import random
from mondrian_color import *


def generate_square(t):
    if random.randint(0, 2) == 1:
        t.rectangle(200, 200, 'black', mondrian_random())
    else:
        a = random.randint(20, 180)
        b = random.randint(20, 180)
        t.rectangle(a, b, 'black', [mondrian_random(), 'white'][random.randrange(0, 2)])
        t.jump_by(b, 0)
        t.rectangle(a, 200 - b, 'black', [mondrian_random(), 'white'][random.randrange(0, 2)])
        t.jump_by(0, a)
        t.rectangle(200 - a, 200 - b, 'black', [mondrian_random(), 'white'][random.randrange(0, 2)])
        t.jump_by(-b, 0)
        t.rectangle(200 - a, b, 'black', [mondrian_random(), 'white'][random.randrange(0, 2)])


def for_mondrian(t):
    t.jump_to(-200, -200)
    t.rectangle(400, 400, 'black', 'white')
    generate_square(t)
    t.jump_to(0, -200)
    generate_square(t)
    t.jump_to(0, 0)
    generate_square(t)
    t.jump_to(-200, 0)
    generate_square(t)