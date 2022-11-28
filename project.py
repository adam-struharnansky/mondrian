from myTurtle_A import *
import turtle
from recursive_mondrian import *
from non_recursive_modrian import *
from grid_mondrian import *
from line_mondrian import *

t = MyTurtle_A()
t.speed(0)
tracer(1)
delay(0)

t.width(5)
t.color(mondrian_black())

# recursive_mondrian_filling(t, 400, 400, -200, -200, True)
# for_mondrian(t, 400, 400, -200, -200)
# recursive_mondrian_filling(t, 400, 400, -200, -200, True)
# grid_mondrian(t, 400, 400, -200, -200, 5, 5)
# advanced_chunk_mondrian(t, 600, 600, -300, -300, depth=4)
# line_mondrian(t, 300, 300, -150, -150, 3, 3)
# diamond_mondrian(t, 600, -300, -300, depth=6, width=10)
# checkerboard(t, 18, 14, 40)
# new_york_city(t, 600, 600, -300, -300, 10, 9)

turtle.done()
