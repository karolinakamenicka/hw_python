from turtle import forward, left, right, exitonclick, pos, setposition
import math
s = 10 
tp = (0,0)
for a in range(10):
    setposition(tp)
    odm =math.sqrt(2)
    forward(s)
    left(135)
    forward(s*odm)
    right(135)
    forward(s)
    right(135)
    forward(s*odm)
    right(135)
    forward(s)
    right(45)
    forward(s/2*odm)
    right(90)
    forward(s/2*odm)
    right(45)
    forward(s)
    left(90)
    forward(s/2)
    tp = pos()

exitonclick()

