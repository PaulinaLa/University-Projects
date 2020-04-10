from turtle import *

def kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(-90)

def trójkąt(bok):
    for i in range(3):
        fd(bok)
        rt(120)
        

def gwiazdka(bok):
    for i in range(10):
        trójkąt(bok)
        kwadrat(bok)
        fd(bok)
        rt(36)

gwiazdka(90)


