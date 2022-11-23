from myTurtle_A import *
from myColor import *
import turtle

from mondrian_color import *
from recursive_mondrian import *
from non_recursive_modrian import *

t = MyTurtle_A()
t.speed(0)
tracer(1)
delay(0)

t.width(5)
t.color(mondrian_black())

# recursive_mondrian_filling(t, 400, 400, -200, -200, True)
for_mondrian(t)

turtle.done()
