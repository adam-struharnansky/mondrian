from turtle import *
from random import randrange as rr, randint as ri

def toRGB(color):
    if isinstance(color, str):        	# meno alebo Tk color string
        try:
            r,g,b = Screen()._root.winfo_rgb(color)
            return r // 256, g // 256, b // 256
        except:
            raise Exception("invalid color name: {}".format(str(color)))
    if isinstance(color, tuple) or isinstance(color, list): # tuple or list
        try:
            r, g, b = color
        except (TypeError, ValueError):
            raise Exception("invalid color arguments: {}".format(str(color)))
        if ((0 <= r <= 1) and (0 <= g <= 1) and (0 <= b <= 1)):
            return (255 * r, 255 * g, 255 * b)
        if ((0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255)):
            return (r, g, b)
    raise Exception("invalid color sequence: {}".format(str(color)))

def any(r=None, g=None, b=None):
    if r is None: r = rr(256)
    if g is None: g = rr(256)
    if b is None: b = rr(256)
    return(r, g, b)

class MyColor(tuple):

    def __new__(cls, r=None, g=None, b=None, h=None, s=None, v=None):
        x, y, z = any(r, g, b)
        if isinstance(r, str):
            x, y, z = toRGB(r)
        elif isinstance(r, tuple) or isinstance(r, list):
            x, y, z = r
        elif h != None or s != None or v != None:
            x, y, z = hsv_to_rgb(*any2(h, s, v))
        elif r != None or g != None or b != None:
            x, y, z = any(r, g, b)
        return tuple.__new__(cls, tuple(round(min(max(f, 0), 255)) for f in (x, y, z)))

    def __init__(self, r=None, g=None, b=None, h=None, s=None, v=None):
        if r == None or isinstance(r, str) or isinstance(r, tuple) or isinstance(r, list):
            r = self[0]
        if g == None:
            g = self[1]
        if b == None:
            b = self[2]
        self.r, self.g, self.b = r, g, b
        self.h, self.s, self.v = rgb_to_hsv(r, g, b)

    def __add__(self, col):
        return MyColor(self.r + col.r, self.g + col.g, self.b + col.b)

    def __sub__(self, col):
        return MyColor(self.r - col.r, self.g - col.g, self.b - col.b)

    def __mul__(self, d):
        return MyColor(self.r * d, self.g * d, self.b * d)

    def __truediv__(self, d):
        return MyColor(self.r / d, self.g / d, self.b / d)

    def close(self, d):
        return MyColor(self.r + ri(-d, d), self.g + ri(-d, d), self.b + ri(-d, d))

def rgb_to_hsv(r, g, b):
    r, g, b = r / 255, g / 255, b / 255
    maxC = max(r, g, b)
    minC = min(r, g, b)
    v = maxC
    if minC == maxC: return (0.0, 0.0, v * 255)
    spec = maxC - minC
    rc, gc, bc = (maxC - r) / spec, (maxC - g) / spec, (maxC - b) / spec
    if r == maxC:
        h = bc - gc
    elif g == maxC:
        h = 2 + rc - bc
    else:
        h = 4 + gc - rc
    h = (h / 6.0) % 1.0
    return (h * 360, spec / maxC * 255, v * 255)

def hsv_to_rgb(a, b, c):
    h, s, v = a % 360 / 360, b / 255, c / 255
    if s == 0.0:
        code = v, v, v
    else:
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6
        if i == 0: code = v, t, p
        if i == 1: code = q, v, p
        if i == 2: code = p, v, t
        if i == 3: code = p, q, v
        if i == 4: code = t, p, v
        if i == 5: code = v, p, q
    return tuple((round(x * 255) for x in code))

def any2(h=None, s=None, v=None):
    if h is None: h = rr(360)
    if s is None: s = rr(256)
    if v is None: v = rr(256)
    return(h, s, v)