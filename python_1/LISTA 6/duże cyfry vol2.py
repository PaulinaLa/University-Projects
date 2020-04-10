"""W zadaniu wracamy do rysowania liczb. Napisz funkcję, która za pomocą modułu
turtle rysuje liczbę n, korzystając z „definicji czcionek” (w module duze_cyfry). Oczywiście
zamias znaków * lub # teraz powinieneś używać wypełnionych kwadracików. Żeby wyglądało to
ładniej, każda cyfra powinna być w losowo wybranym kolorze.
"""

from duze_cyfry import *
from turtle import *
from math import*
from random import*
speed('fastest')

bok=30
kolory=['gold', 'chocolate','dodgerblue','violet','firebrick','coral','salmon','tomato', 'hotpink', 'mediumseagreen', 'royalblue', 'darkturquoise','plum','fuchsia','pink','green','yellow','blue','light green', 'purple','light yellow', 'indigo', 'magenta']

def kwadrat(bok): #kolor)
  #fillcolor(kolor)
  #begin_fill()
  for i in range(4):
    fd(bok)
    rt(90)
  #end_fill()
  pu()
  fd(bok)
  pd()

def nie_kwadrat(bok):
  pu()
  fd(bok)
  pd()


def rysowanki(n):
    f=len(str(n))
    p=str(n)
    for i in p:
        #kolor=choice(kolory)
        d=dajCyfre(int(i))
        s=bok
        x=0
        for j in range(5):
            for m in range(5):
                if d[j][m]=="#":
                    kwadrat(bok)#, kolor)
                else:
                  pu()
                  nie_kwadrat(bok)
                  pd()
                  
            pu()
            rt(90)
            fd(bok)
            rt(90)
            fd(bok*5)
            lt(180)
            pd()
        pu()
        fd(bok*6)
        lt(90)
        fd(5*bok)
        rt(90)
        pd()

 



rysowanki(5)



        

