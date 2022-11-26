from mondrian_color import *
import random

LINE_WIDTH = 20


def centred_square(t, x, y, side, rim_color, fill_color):
    t.jump_to(x - side / 2, y + side / 2)
    t.rectangle(side, side, rim_color, fill_color)


def crossroads(t, x_coordinates, y_coordinates):
    for x in x_coordinates:
        for y in y_coordinates:
            color = mondrian_random_and_white()
            centred_square(t, x, y, LINE_WIDTH, color, color)


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


def squares(t, x, y, width, height, x_coordinates, y_coordinates):
    # squares on vertical
    for rect_x in x_coordinates:
        rect_y = random.randrange(y, y + LINE_WIDTH)
        y_squares = y_coordinates.copy()
        while rect_y < y + height:
            if check_element(rect_y, y_squares):
                color = mondrian_random_and_white()
                centred_square(t, rect_x, rect_y, LINE_WIDTH, color, color)
                y_squares.append(rect_y)
            rect_y += LINE_WIDTH / 5
    # squares on horizontal
    for rect_y in y_coordinates:
        rect_x = random.randrange(x, x + LINE_WIDTH)
        x_squares = x_coordinates.copy()
        while rect_x < x + width:
            if check_element(rect_x, x_squares):
                color = mondrian_random_and_white()
                centred_square(t, rect_x, rect_y, LINE_WIDTH, color, color)
                x_squares.append(rect_x)
            rect_x += LINE_WIDTH / 5


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
    squares(t, x, y, width, height, x_coordinates, y_coordinates)
