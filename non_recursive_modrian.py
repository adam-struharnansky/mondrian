from mondrian_color import *

MIN_SIZE = 20


def generate_square(t, width, height):
    """
    Podporna funkcia pre metodu for_mondrian, ktora vygeneruje
    styri utvary v zadanej oblasti.

    :param t: Korytnacka
    :param width: Sirka danej oblasti
    :param height: Vyska danej oblasti
    :return: None
    """
    if random.randint(0, 2) == 1:
        t.rectangle(width, height, 'black', mondrian_random())
    else:
        a = random.randint(MIN_SIZE, width - MIN_SIZE)
        b = random.randint(MIN_SIZE, height - MIN_SIZE)
        t.rectangle(a, b, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])
        t.jump_by(b, 0)
        t.rectangle(a, height - b, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])
        t.jump_by(0, a)
        t.rectangle(width - a, height - b, mondrian_black(),
                    [mondrian_random(), mondrian_white()][random.randrange(0, 2)])
        t.jump_by(-b, 0)
        t.rectangle(width - a, b, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])


def for_mondrian(t, width, height, x, y):
    """
    Jednoducha nerekurzivna funkcia generujuca vzor podobny dielu
    Tableau.

    :param t: Korytnacka
    :param width: Sirka obrazku
    :param height: Vyska obrazku
    :param x: x-ova suradnica laveho dolneho rohu
    :param y: y-ova suradnica laveho dolneho rohu
    :return: None
    """
    t.jump_to(x, y)
    t.rectangle(width, height, mondrian_black(), mondrian_white())
    generate_square(t, width / 2, height / 2)
    t.jump_to(x + width / 2, y)
    generate_square(t,  width / 2, height / 2)
    t.jump_to(x + width / 2, y + height / 2)
    generate_square(t,  width / 2, height / 2)
    t.jump_to(x, y + height / 2)
    generate_square(t,  width / 2, height / 2)


def checkerboard(t, num_of_columns, num_of_rows, size):
    """
    Metoda generujuca mozaiku podobnu dielu Checkerboard.

    :param t: Korytnacka
    :param num_of_columns: Pocet stlpcov mozaiky
    :param num_of_rows: Pocet riadkov mozaiky
    :param size: Velkost strany jedneho stvorceka
    :return: None
    """
    t.width(2)
    x, y = -((num_of_columns * size) / 2), -((num_of_rows * size) / 2)
    t.jump_to(x, y)
    for i in range(num_of_columns):
        pos = t.pos()
        for j in range(num_of_rows):
            t.rectangle(size, size, 'black', checkerboard_random())
            t.jump_to(t.xcor(), t.ycor() + size)
        t.jump_to(pos)
        t.jump_by(size, 0)


def overlap(mode, coordinate, rows: list, columns: list, c_x, c_y, w, h) -> bool:
    """
    Podporna funkcia pre metodu new_york_city, ktora kontroluje
    prekryvy medzi ciarou, ktora sa ma vygenerovat a tymi, ktore
    sa uz vygenerovali.

    :param mode: 0 - pre kontrolu novej ciary v riadku, 1 - pre kontrolu novej ciary v stlpci
    :param coordinate: Koordinat x alebo y ciary, ktoru chceme vygenerovat v zavislosti od zvoleneho modu
    :param rows: Zoznam y-ovych suradnic uz vygenerovanych ciar
    :param columns: Zoznam x-ovych suradnic uz vygenerovanych ciar
    :param c_x: x-ova suradnica laveho dolneho rohu
    :param c_y: y-ova suradnica laveho dolneho rohu
    :param w: Sirka obrazka
    :param h: Vyska obrazka
    :return: True alebo False podla toho ci by sa planovana ciara prekryvala s niektorou uz vygenerovanou alebo nie
    """
    is_overlaping = False
    if mode == 0:
        for i in rows:
            if i - 20 < coordinate < i + 20:
                is_overlaping = True
        if c_y + h < coordinate + 20 or c_y > coordinate - 20:
            is_overlaping = True

    if mode == 1:
        for i in columns:
            if i - 20 < coordinate < i + 20:
                is_overlaping = True
        if coordinate - 20 < c_x or coordinate + 20 > c_x + w:
            is_overlaping = True
    return is_overlaping


def crop_new_york(t, width, height, x, y):
    """
    Podporna funkcia pre metodu new_york_city, ktora oreze konce ciar tak aby neboli zaoblene

    :param t: Korytnacka
    :param width: Sirka obrazka
    :param height: Vyska obrazka
    :param x: x-ova suradnica laveho dolneho rohu
    :param y: y-ove suradnica laveho dolneho rohu
    :return: None
    """
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
    """
    Metoda generujuca obrazok podobny dielu New York City.

    :param t: Korytnacka
    :param width: Sirka obrazka
    :param height: Vyska obrazka
    :param x: x-ova suradnica laveho dolneho rohu
    :param y: y-ova suradnica laveho dolneho rohu
    :param num_rows: Pocet riadkov
    :param num_columns: Pocet stlpcov
    :return: None
    """
    t.width(10)
    rows = []
    columns = []
    for i in range(num_rows + num_columns):

        if ri(0, 1) == 0 and num_rows != 0:
            t.jump_to(x, y)
            t.setheading(0)
            new_y = ri(y, y + height)
            while overlap(0, new_y, rows, [], x, y, width, height):
                new_y = ri(y, y + height)
            rows.append(new_y)
            t.jump_to(x, new_y)
            t.color(mondrian_random())
            t.fd(width)
            t.jump_to(x, y)
            num_rows -= 1
        elif num_columns != 0:
            t.jump_to(x, y)
            t.setheading(90)
            new_x = ri(x, x + width)
            while overlap(1, new_x, [], columns, x, y, width, height):
                new_x = ri(x, x + width)
            columns.append(new_x)
            t.jump_to(new_x, y)
            t.color(mondrian_random())
            t.fd(height)
            t.jump_to(x, y)
            num_columns -= 1
        else:
            i -= 1
    crop_new_york(t, width, height, x, y)
