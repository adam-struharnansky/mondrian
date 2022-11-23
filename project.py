from myTurtle_A import *
from myColor import *
import turtle

from mondrian_color import *
from recursive_mondrian import *

t = MyTurtle_A()
t.speed(0)
tracer(1)
delay(0)

t.width(5)

recursive_mondrian(t, 400, 400, -200, -200)

turtle.done()
