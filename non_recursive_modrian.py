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


def checkerboard(t, a, b, size):
    t.width(2)
    x, y = -((a * size) / 2), -((b * size) / 2)
    t.jump_to(x, y)
    for i in range(a):
        pos = t.pos()
        for j in range(b):
            t.rectangle(size, size, 'black', checkerboard_random())
            t.jump_to(t.xcor(), t.ycor() + size)
        t.jump_to(pos)
        t.jump_by(size, 0)


def overlap(mode, y, rows, columns, c_x, c_y, w, h) -> bool:
    isOverlaping = False
    if mode == 0:
        for i in rows:
            if i - 20 < y < i + 20:
                isOverlaping = True
        if c_y + h < y + 20 or c_y > y - 20:
            isOverlaping = True

    if mode == 1:
        for i in columns:
            if i - 20 < y < i + 20:
                isOverlaping = True
        if y - 20 < c_x or y + 20 > c_x + w:
            isOverlaping = True
    return isOverlaping


def crop_new_york(t, width, height, x, y):
    t.jump_to(x, y)
    t.setheading(0)
    for i in range(4):
        if i == 0 or i == 2:
            t.rectangle(width, width, 'white', 'white')
            t.jump_fd(width)
        if i == 1 or i == 3:
            t.rectangle(height, height, 'white', 'white')
            t.jump_fd(height)
        t.lt(90)


def new_york_city(t, width, height, x, y, num_rows, num_columns):
    t.width(10)
    rows = []
    columns = []
    for i in range(num_rows + num_columns):

        if ri(0, 1) == 0 and num_rows != 0:
            t.jump_to(x, y)
            t.setheading(0)
            newY = ri(y, y + height)
            while overlap(0, newY, rows, [], x, y, width, height):
                newY = ri(y, y + height)
            rows.append(newY)
            t.jump_to(x, newY)
            t.color(mondrian_random())
            t.fd(width)
            t.jump_to(x, y)
            num_rows -= 1
        elif num_columns != 0:
            t.jump_to(x, y)
            t.setheading(90)
            newX = ri(x, x + width)
            while overlap(1, newX, [], columns, x, y, width, height):
                newX = ri(x, x + width)
            columns.append(newX)
            t.jump_to(newX, y)
            t.color(mondrian_random())
            t.fd(height)
            t.jump_to(x, y)
            num_columns -= 1
        else:
            i -= 1
    crop_new_york(t, width, height, x, y)
