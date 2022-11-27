from myColor import *
import random


def mondrian_red():
    return MyColor(221, 1, 0)


def mondrian_blue():
    return MyColor(34, 80, 149)


def mondrian_yellow():
    return MyColor(250, 201, 1)


def mondrian_random():
    return [mondrian_yellow(), mondrian_blue(), mondrian_red()][random.randrange(0, 3)]


def mondrian_white():
    return MyColor(249, 249, 249)


def mondrian_black():
    return MyColor(23, 18, 17)


def mondrian_random_and_white():
    return [mondrian_yellow(), mondrian_red(), mondrian_blue(), mondrian_white()][random.randrange(0, 4)]


def mondrian_random_all():
    return [mondrian_yellow(), mondrian_white(), mondrian_blue(), mondrian_red(), mondrian_black()][
        random.randrange(0, 5)]


def checkerboard_orange():
    return MyColor(232, 67, 3)


def checkerboard_pink():
    return MyColor(225, 37, 81)


def checkerboard_blue():
    return MyColor(0, 97, 191)


def checkerboard_random():
    return [checkerboard_blue(), checkerboard_pink(), checkerboard_orange()][random.randrange(0, 3)]
