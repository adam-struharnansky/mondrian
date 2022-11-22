from turtle import *
from myColor import *
from random import randrange as rr, randint as ri, choice as rch, shuffle
from math import cos, radians
import math

colormode(255)
delay(0)

class MyTurtle_A(Turtle):
    def __init__(self, x=0, y=0, h=90):
        super().__init__()
        self.ht()
        self.x, self.y, self.h = x, y, h
        self.state = list()
        self.speed(0)
        self.home()

    def home(self):
        p = self.pen()
        self.pu()
        self.setpos(self.x, self.y)
        self.seth(self.h)
        self.pen(p)

    def getState(self):
        self.state.append((self.pos(), self.heading()))

    def restoreState(self):
        p = self.pen()
        self.pu()
        s = self.state.pop()
        self.setpos(s[0])
        self.setheading(s[1])
        self.pen(p)

    def reset(self):
        visible = self.isvisible()
        super().reset()
        self.home()
        if not visible:
            self.ht()
            
    def myFd(self, col1, col2, dist, w, angle=0, step=1):
        """ col1 a col2 su objekty triedy MyColor"""
        p = self.pen()
        self.pensize(2)
        delta = (col2 - col1) / (dist - 1)
        self.lt(90)
        for _ in range(dist // step):
            self.color(col1)
            self.jump_fd(-w / 2)
            self.fd(w)
            self.jump_fd(-w / 2)
            col1 += delta * step
            self.sideway(step)
            self.rt(angle * step)
        self.rt(90)
        self.pen(p)

    def myFd2(self, col1, col2, dist, w, angle=0, step=1):
        """ col1 a col2 su objekty triedy MyColor"""
        p = self.pen()
        self.pensize(2)
        delta = (col2 - col1) / (w - 1)
        self.sideway(w / 2)
        for _ in range(w // step):
            self.color(col1)
            self.fd(dist)
            self.jump_fd(-dist)
            col1 += delta * step
            self.sideway(-step)
            self.rt(angle * step)
        self.sideway(w / 2)
        self.pen(p)
        
    def myFd33(self, col1, col2, w):
        deltaC = (col2 - col1) / (w - 1)
        self.jump_fd(-w / 2)
        for _ in range(w):
            self.color(col1)
            self.fd(1)
            col1 += deltaC
        self.jump_fd(-w / 2)

    def myFd3(self, col1, col2, dist, w1, w2, angle=0, step=1):
        p = self.pen()
        self.pensize(2)
        deltaW = (w2 - w1) / (dist - 1)
        self.lt(90)
        for _ in range(dist // step):
            self.myFd33(col1, col2, int(w1))
            self.sideway(step)
            w1 += deltaW * step
            self.rt(angle * step)
        self.rt(90)
        self.pen(p)

    def myFd4(self, colR1, colR2, colL1, colL2, dist, w1, w2, angle=0, step=1):
        p = self.pen()
        self.pensize(2)
        deltaW = (w2 - w1) if dist < 2 else (w2 - w1) / (dist - 1)
        deltaCR = (colR2 - colR1) / (dist - 1)
        deltaCL = (colL2 - colL1) / (dist - 1)
        self.lt(90)
        for _ in range(dist // step):
            self.myFd33(colR1, colL1, int(w1))
            self.sideway(step)
            self.rt(angle * step)
            w1 += deltaW * step
            colR1 += deltaCR * step
            colL1 += deltaCL * step
        self.rt(90)
        self.pen(p)

    def colCNGon(self, n, rad, rimCol='red3', fillCol='light gray', rimSize=1, fill=True):
        p = self.pen()
        self.pu()
        self.color(rimCol, fillCol)
        self.pensize(rimSize)
        alpha = 360 / n
        beta = 90 - 180 / n
        side = 2 * rad * cos(radians(beta))
        self.jump_fd(rad)
        self.pd()
        self.rt(alpha + beta)
        if fill:
            self.begin_fill()
        for _ in range(n):
            self.fd(side)
            self.rt(alpha)
        if fill:
            self.end_fill()
        self.lt(alpha + beta)
        self.jump_fd(-rad)
        self.pen(p)

    def myCanvas(self, ll_corner=None, wd=220, ht=320, rimCol='gray20', fillCol='gray80'):
        p = self.pen()
        if ll_corner == None:
            ll_corner = self.pos()
        self.color(rimCol, fillCol)
        self.ll_corner, self.wd, self.ht = ll_corner, wd, ht
        self.jump_to(ll_corner)
        self.seth(90)
        self.pd()
        self.begin_fill()
        for _ in range(2):
            self.fd(ht)
            self.rt(90)
            self.fd(wd)
            self.rt(90)
        self.end_fill()
        self.pen(p)

    def colNGon(self, n, side, rimCol='red3', fillCol='light gray', rimSize=2, fill=True):
        self.color(rimCol, fillCol)
        self.pensize(rimSize)
        angle = 360 / n
        if fill:
            self.begin_fill()
        for _ in range(n):
            self.fd(side)
            self.rt(angle)
        if fill:
            self.end_fill()

    def colNGonErr(self, n, side, err, rimCol='red3', fillCol='light gray', rimSize=1, fill=True):
        p0 = self.pos()
        self.color(rimCol, fillCol)
        self.pensize(rimSize)
        e = Vec2D(err, 0)
        pts = [p + e.rotate(rr(360)) for p in self.nGonCollectPts(n, side)[:-1]]
        pts.append(pts[0])
        if fill:
            self.begin_fill()
        self.pu()
        for point in pts:
            self.setpos(p0 + point)
            self.pd()
        if fill:
            self.end_fill()

    def nGonCollectPts(self, n, side):
        p = self.pen()
        self.pu()
        self.begin_poly()
        for _ in range(n):
            self.fd(side)
            self.rt(360 / n)
        self.end_poly()
        self.pen(p)
        return [p - self.pos() for p in self.get_poly()]

    def polygon(self, n, side, angle, fill=True):
        if fill:
            self.begin_fill()
        for _ in range(n):
            self.fd(side)
            self.rt(angle)
        if fill:
            self.end_fill()

    def jump_to(self, x=0, y=0):
        if isinstance(x, tuple):
            x, y = x
        p = self.pen()
        self.pu()
        self.setpos(x, y)
        self.pen(p)

    def jump_by(self, dx=0, dy=0):
        p = self.pen()
        self.pu()
        self.setpos(self.xcor() + dx, self.ycor() + dy)
        self.pen(p)

    def jump_fd(self, d):
        p = self.pen()
        self.pu()
        self.fd(d)
        self.pen(p)

    def sideway(self, d):
        self.rt(90)
        self.jump_fd(d)
        self.lt(90)

    def rectangle(self, a, b, rimCol, fillCol):
        self.color(rimCol, fillCol)
        self.begin_fill()
        for _ in range(2):
            self.fd(a)
            self.rt(90)
            self.fd(b)
            self.rt(90)
        self.end_fill()

    def triangle(self, side, angle, rimCol, fillCol):
        self.color(rimCol, fillCol)
        radians = (math.pi*angle)/180
        other_side = math.sqrt(2*(side**2) - 2*(side**2)*cos(radians))

        self.begin_fill()
        self.fd(side)
        self.rt(180 - (180 - angle)/2)
        self.fd(other_side)
        self.rt(180 - (180 - angle)/2 )
        self.fd(side)
        self.rt((180 - angle))
        self.end_fill()


def rch_P(l1, l2):
    r = []
    for i in range(min(len(l1), len(l2))):
        r += [l1[i]] * l2[i]
    return r

def rp(x, p):
    x *= 100
    return ri(int(x - x * p), int(x + x * p)) / 100
