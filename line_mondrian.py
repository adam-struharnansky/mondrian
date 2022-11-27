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

def rectangles(t, x_coordinates, y_coordinates):
    for _ in range(len(x_coordinates)):
        x_str = random.randrange(1, len(x_coordinates) - 1)
        y_str = random.randrange(1, len(y_coordinates) - 1)

        x = 0
        y = 0
        side = 0
        other_side = 0
        color = [mondrian_red(), mondrian_blue()][random.randrange(0, 2)]
        inner_color = mondrian_random_and_white()
        if random.randrange(0, 2):
            if y_coordinates[y_str + 1] - y_coordinates[y_str] > 3 * LINE_WIDTH:
                side = random.randrange(2 * LINE_WIDTH, y_coordinates[y_str + 1] - y_coordinates[y_str] - LINE_WIDTH)
                other_side = x_coordinates[x_str + 1] - x_coordinates[x_str]
                x = x_coordinates[x_str]
                y = (y_coordinates[y_str + 1] + y_coordinates[y_str]) // 2 - side // 2
        else:
            if x_coordinates[x_str + 1] - x_coordinates[x_str] > 3 * LINE_WIDTH:
                side = y_coordinates[y_str + 1] - y_coordinates[y_str]
                other_side = random.randrange(2 * LINE_WIDTH,
                                              x_coordinates[x_str + 1] - x_coordinates[x_str] - LINE_WIDTH)
                x = (x_coordinates[x_str + 1] + x_coordinates[x_str]) // 2 - other_side // 2
                y = y_coordinates[y_str]
        t.jump_to(x, y)
        t.rectangle(side, other_side, color, color)
        if side > 2 * LINE_WIDTH and other_side > 2 * LINE_WIDTH:
            t.jump_to(x + other_side / 4, y + side / 4)
            t.rectangle(side / 2, other_side / 2, inner_color, inner_color)


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
    start = random.randrange(y, y + LINE_WIDTH)
    # squares on vertical
    for rect_x in x_coordinates:
        rect_y = start
        y_squares = y_coordinates.copy()
        while rect_y < y + height:
            if check_element(rect_y, y_squares):
                color = mondrian_random_and_white()
                centred_square(t, rect_x, rect_y, LINE_WIDTH, color, color)
                y_squares.append(rect_y)
            rect_y += LINE_WIDTH / 5
    # squares on horizontal
    for rect_y in y_coordinates:
        rect_x = start
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

    rectangles(t, x_coordinates, y_coordinates)
    lines(t, width, height, x, y,  x_coordinates, y_coordinates)
    crossroads(t, x_coordinates, y_coordinates)
    squares(t, x, y, width, height, x_coordinates, y_coordinates)
