from mondrian_color import *
import random

LINE_WIDTH = 20


def crossroads(t, x_coordinates, y_coordinates):
    for x in x_coordinates:
        for y in y_coordinates:
            t.jump_to(x - LINE_WIDTH / 2, y + LINE_WIDTH / 2)
            color = mondrian_random_and_white()
            t.rectangle(LINE_WIDTH, LINE_WIDTH, color, color)


def lines(t, width, height, x, y, x_coordinates, y_coordinates):
    t.setheading(90)
    for tmp_x in x_coordinates:
        t.jump_to(tmp_x, y)
        t.myFd(mondrian_yellow(), mondrian_yellow(), height, LINE_WIDTH)
    t.setheading(0)
    for tmp_y in y_coordinates:
        t.jump_to(x, tmp_y)
        t.myFd(mondrian_yellow(), mondrian_yellow(), width, LINE_WIDTH)


def check_element(element, previous):
    for p in previous:
        if abs(element - p) < 2 * LINE_WIDTH:
            return False
    return True


def possible_new_element(min_value, max_value, previous):
    new_element = random.randrange(min_value, max_value)
    while not check_element(new_element, previous):
        new_element += 1
        if new_element > max_value:
            new_element = min_value
    return new_element


def line_mondrian(t, width, height, x, y, rows_num, columns_num):
    x_coordinates = []
    y_coordinates = []
    for _ in range(rows_num):
        x_coordinates.append(possible_new_element(x, x + width, x_coordinates))
    for _ in range(columns_num):
        y_coordinates.append(possible_new_element(y, y + height, y_coordinates))
    y_coordinates.sort()
    x_coordinates.sort()

    lines(t, width, height, x, y,  x_coordinates, y_coordinates)
    crossroads(t, x_coordinates, y_coordinates)
