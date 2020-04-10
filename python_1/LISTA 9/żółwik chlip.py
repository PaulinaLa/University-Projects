from turtle import *
import random
speed('fastest')

def koch(k, l):
    color = random.choice(["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"])
    pencolor(color)
    if k == 0:
        fd(l)
    else:
        koch(k - 1, l/3)
        left(60)
        koch(k - 1, l/3)
        right(120)
        koch(k - 1, l/3)
        left(60)
        koch(k - 1, l/3)
pu()
goto(-300,50)
pd()
begin_fill()
color('green')
koch(4, 600)
goto(-300,50)
end_fill()
begin_fill()
color('pink')
koch(3, 600)
goto(-300,50)
end_fill()
begin_fill()
color('red')
koch(2, 600)
goto(-300,50)
end_fill()
begin_fill()
color('gold')
koch(1, 600)
goto(-300,50)
end_fill()



input()

