import math

from mondrian_color import *
import random

MIN_SIZE = 80
WHITE_TO_COLOR_RATIO = 3
FILL_STOP_RATIO = 0.5
STOP_RATIO = 0.7


def recursive_mondrian(t, width, height, x, y):
    """
    Jednoducha funkcia ktore rekurzivne vygeneruje obraz poodbny Mondrianovmu dielu Tableau. Funguje tak, ze vstupny
    obdlznik vyfarbi, potom ho rozdeli, a na obe casti zavola rekurzivne seba. Skonci, ak niektori z rozmerov bude
    mensi, ako MIN_SIZE
    JE POTREBNE NASTAVIT tracer(1)!

    :param t: korytnacka
    :param width: sirka obrazku
    :param height: vyska obrazku
    :param x: x-ova suradnica lavej strany obrazku
    :param y: y-ova suradnica spodnej strany obrazku
    """
    t.jump_to(x, y)
    t.setheading(90)
    if rr(0, WHITE_TO_COLOR_RATIO):
        t.rectangle(height, width, mondrian_black(), mondrian_white())
    else:
        t.rectangle(height, width, mondrian_black(), mondrian_random())

    if width < MIN_SIZE or height < MIN_SIZE:
        return

    if rr(0, 2):
        b = random.uniform(MIN_SIZE/2, width - MIN_SIZE/2)
        recursive_mondrian(t, b, height, x, y)
        recursive_mondrian(t, width - b, height, x + b, y)
    else:
        b = random.uniform(MIN_SIZE/2, height - MIN_SIZE/2)
        recursive_mondrian(t, width, b, x, y)
        recursive_mondrian(t, width, height - b, x, y + b)


def random_bool(true_ratio):
    """
    Funkcia vracia nahodny bool

    :param true_ratio: pravdepodobnost, ze funkcia vrati True
    :return: nahodne True alebo False distribuovane podla true_ratio
    """
    return random.uniform(0, 1) < true_ratio


def recursive_mondrian_filling(t, width, height, x, y, fill):
    """
    Funkcia ktora rekurzivne vygeneruje obraz poodbny Mondrianovmu dielu Tableau. Funguje tak, ze vstupny
    obdlznik vyfarbi, potom ho rozdeli, a na obe casti zavola rekurzivne seba. Skonci, ak niektori z rozmerov bude
    mensi, ako MIN_SIZE. Moze sa rozhodnut, a zakazat rekurzivnym volaniam prefarbovat pod-obldzniky
    JE POTREBNE NASTAVIT tracer(1)!

    :param t: korytnacka
    :param width: sirka obrazku
    :param height: vyska obrazku
    :param x: x-ova suradnica lavej strany obrazku
    :param y: y-ova suradnica spodnej strany obrazku
    :param fill: to, ci moze prefarbit dany obdlznik, alebo iba ho rozdelit
    """
    t.jump_to(x, y)
    t.setheading(90)
    new_fill = fill
    if fill:
        if rr(0, WHITE_TO_COLOR_RATIO):
            t.rectangle(height, width, mondrian_black(), mondrian_white())
        else:
            t.rectangle(height, width, mondrian_black(), mondrian_random())
            if width < 2.5 * MIN_SIZE or height < 2.5 * MIN_SIZE:
                new_fill = random_bool(FILL_STOP_RATIO)

    if width < MIN_SIZE or height < MIN_SIZE:
        return

    if rr(0, 2):
        b = random.uniform(MIN_SIZE / 2, width - MIN_SIZE / 2)
        t.jump_to(x + b, y)
        t.setheading(90)
        t.fd(height)
        recursive_mondrian_filling(t, b, height, x, y, new_fill)
        recursive_mondrian_filling(t, width - b, height, x + b, y, new_fill)
    else:
        b = random.uniform(MIN_SIZE / 2, height - MIN_SIZE / 2)
        t.jump_to(x, y + b)
        t.setheading(0)
        t.fd(width)
        recursive_mondrian_filling(t, width, b, x, y, new_fill)
        recursive_mondrian_filling(t, width, height - b, x, y + b, new_fill)


def recursive_mondrian_stop(t, width, height, x, y, fill):
    """
    Funkcia ktora rekurzivne vygeneruje obraz poodbny Mondrianovmu dielu Tableau. Funguje tak, ze vstupny
    obdlznik vyfarbi, potom ho rozdeli, a na obe casti zavola rekurzivne seba. Skonci, ak niektori z rozmerov bude
    mensi, ako MIN_SIZE. Moze sa rozhodnut, a zakazat rekurzivnym volaniam prefarbovat pod-obldzniky. Tiez moze nahodne
    nezavolat niektoru z prislusnych rekurzivnych funkcii (a teda moze generovat aj celkom velke jednofarbne plochy).
    JE POTREBNE NASTAVIT tracer(1)!

    :param t: korytnacka
    :param width: sirka obrazku
    :param height: vyska obrazku
    :param x: x-ova suradnica lavej strany obrazku
    :param y: y-ova suradnica spodnej strany obrazku
    :param fill: to, ci moze prefarbit dany obdlznik, alebo iba ho rozdelit
    """
    t.jump_to(x, y)
    t.setheading(90)
    new_fill = fill
    if fill:
        if rr(0, WHITE_TO_COLOR_RATIO):
            t.rectangle(height, width, mondrian_black(), mondrian_white())
        else:
            t.rectangle(height, width, mondrian_black(), mondrian_random())
            if width < 2.5 * MIN_SIZE or height < 2.5 * MIN_SIZE:
                new_fill = random_bool(FILL_STOP_RATIO)

    if width < MIN_SIZE or height < MIN_SIZE:
        return

    if rr(0, 2):
        b = random.uniform(MIN_SIZE / 2, width - MIN_SIZE / 2)
        t.jump_to(x + b, y)
        t.setheading(90)
        t.fd(height)
        if random_bool(STOP_RATIO):
            recursive_mondrian_stop(t, b, height, x, y, new_fill)
        if random_bool(STOP_RATIO):
            recursive_mondrian_stop(t, width - b, height, x + b, y, new_fill)
    else:
        b = random.uniform(MIN_SIZE / 2, height - MIN_SIZE / 2)
        t.jump_to(x, y + b)
        t.setheading(0)
        t.fd(width)
        if random_bool(STOP_RATIO):
            recursive_mondrian_stop(t, width, b, x, y, new_fill)
        if random_bool(STOP_RATIO):
            recursive_mondrian_stop(t, width, height - b, x, y + b, new_fill)


def advanced_chunk_mondrian(t, height, width, x, y, depth=4, counter=0):
    """
    Rekurzivna funkcia generujuca vzor podobny dielu Tableau. Funkcia rozdeluje
    zakladny utvar na 4 casti a nasledne sa na kazdy rekurzivne zavola a proces sa
    opakuje.

    :param t: Korytnacka
    :param height: Vyska obrazka
    :param width: Sirka obrazka
    :param x: x-ova suradnica laveho dolneho rohu
    :param y: y-ova suradnica laveho dolneho rohu
    :param depth: Maximalna hlbka recenzie
    :param counter: Pocitadlo aktualnej hlbky recenzie
    :return: None
    """
    min_size = 30
    if counter == depth:
        return

    t.jump_to(x, y)

    if height - min_size < min_size or width - min_size < min_size:
        t.rectangle(height, width, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])
        return

    r = random.randint(0, 2)
    if counter == 0:
        r = 0

    if r != 1:
        t.rectangle(height, width, mondrian_black(), mondrian_white())
        new_a = random.randint(min_size, height - min_size)
        new_b = random.randint(min_size, width - min_size)

        if new_a + int(new_b/2) < new_b:
            new_b -= int(new_b/2)
        elif new_b + int(new_a/2) < new_a:
            new_a -= int(new_a/2)

        advanced_chunk_mondrian(t, new_a, new_b, x, y, depth, counter + 1)
        advanced_chunk_mondrian(t, new_a, width - new_b, x + new_b, y, depth, counter + 1)
        advanced_chunk_mondrian(t, height - new_a, width - new_b, x + new_b, y + new_a, depth, counter + 1)
        advanced_chunk_mondrian(t, height - new_a, new_b, x, y + new_a, depth, counter + 1)
    else:
        t.rectangle(height, width, mondrian_black(), [mondrian_random(), mondrian_white()][random.randrange(0, 2)])


def diamond_mondrian(t, side, x, y, depth=4, width=14):
    """
    Funkcia vyuzivajuca rekurzivnu metodu advanced_chunk_mondrian, ktorej
    vysledok nasledne oreze tak aby bol v tvare kosostvorca.

    :param t: Korytnacka
    :param side: Dlzka strany stvorca
    :param x: x-ova suradnica laveho dolneho rohu
    :param y: y-ova suradnica laveho dolneho rohu
    :param depth: Maximalna hlbka rekurzie
    :param width: Sirka ciary pri vykreslovani
    :return: None
    """
    t.width(width)
    advanced_chunk_mondrian(t, side, side, x, y, depth=depth)
    t.jump_to((x + side/2), y)
    t.setheading(90)
    t.rt(45)
    for i in range(4):
        t.rectangle(side, side, 'white', 'white')
        t.jump_fd(math.sqrt((side/2) ** 2 + (side/2) ** 2))
        t.lt(90)
