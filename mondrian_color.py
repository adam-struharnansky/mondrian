from myColor import *


def mondrian_red():
    return MyColor(221, 1, 0)


def mondrian_blue():
    return MyColor(34, 80, 149)


def mondrian_yellow():
    return MyColor(250, 201, 1)


def mondrian_random():
    return [mondrain_yellow(), mondrain_blue(), mondrain_red()][random.randrange(0, 3)]
