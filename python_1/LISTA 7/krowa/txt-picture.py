from turtle import *
import random
kwadraty = open('obrazek-tekstowy.txt').readlines()
BOK = 10
#kwadraty jest dlugosci 64, tyle wierszy ma obrazek


def kwadrat(x, y, kolor):
  fillcolor(kolor)
  pu()
  goto(x - 250, 250 + y) # zmiana środka ukł wspłż
  pd()
  begin_fill()
  for i in range(4):
    fd(BOK)
    rt(90)
  end_fill()


def krowa():
    tracer(0,1)
    for i in range(len(kwadraty)): #dla 64 wierszy
        wiersz = kwadraty[i].split() #dzieli wiersz na pojedyncze krotki
        for j in range(len(wiersz)): #dla dlugosci wiersza 
            kolor = eval(wiersz[j]) #eval interpretuje string jako kod(krotke)
            kwadrat(i*BOK,-(j*BOK),(kolor[0]/255,kolor[1]/255,kolor[2]/255))#1 nr kolumny, j nr wiersza



print(krowa())
