from mondrian_color import *
import random

WHITE_TO_COLOR_RATIO = 3


def grid_mondrian(t, width, height, x, y, rows_num, columns_num):
    """
    Funkcia na vygenerovanie obrazku podobneho Mondrianovmu obrazu Tableau, pricom je vcely vlozeny do istej mriezky.

    :param t: Kortnacka
    :param width: Sirka obrazku, ktory ma byt vygenerovany
    :param height: Vyska obrazku, ktory ma byt vygenerovany
    :param x: x-ova suradnica laveho okraja obrazku
    :param y: y-ova suradnica doleno okraja obrazku
    :param rows_num: pocet horizontalnych ciar okrem prvej a poslednej
    :param columns_num: pocet vertikalnych ciar okrem prvej a poslednej
    """
    x_coordinates = [x, x + width]
    y_coordinates = [y, y + height]
    for _ in range(rows_num):
        x_coordinates.append(random.randrange(0, width) + x)
    for _ in range(columns_num):
        y_coordinates.append(random.randrange(0, height) + y)
    y_coordinates.sort()
    x_coordinates.sort()

    t.setheading(90)
    for tmp_x in x_coordinates:
        t.jump_to(tmp_x, y)
        t.fd(height)
    t.setheading(0)
    for tmp_y in y_coordinates:
        t.jump_to(x, tmp_y)
        t.fd(width)

    t.setheading(90)
    for index_x in range(len(x_coordinates) - 1):
        for index_y in range(len(y_coordinates) - 1):
            if not random.randrange(0, WHITE_TO_COLOR_RATIO):
                t.jump_to(x_coordinates[index_x], y_coordinates[index_y])
                a = x_coordinates[index_x + 1] - x_coordinates[index_x]
                b = y_coordinates[index_y + 1] - y_coordinates[index_y]
                t.rectangle(b, a, mondrian_black(), mondrian_random())
