from turtle import *
from duze_cyfry import dajCyfre
import random
BOK = 15

speed('fastest')

def kwadrat(SX,SY,x, y, kolor): #funkcja kwadrat z goto
  fillcolor(kolor)
  pu()
  goto(SX + x * BOK, SY + y * BOK)#przesuwam się w odpowiednie miejsce
  pd()
  begin_fill()
  for i in range(4):
    fd(BOK)
    rt(90)
  end_fill() 

kolory=['red','green','cyan','magenta','yellow','orange','pink','purple','black','gold','indigo']


def rysowanki(used,SX,SY,n,kolor):
  liczba=dajCyfre(n) # Sprawdzam czy nie mam współrzędnych w used
  for i in range(len(liczba)):
      for j in range(len(liczba[0])):
          if liczba[i][j]=="#":
             if (SX+j*BOK,SY-i*BOK) in used:
                 return False
  for i in range(len(liczba)): # gdy nie mam to będę rysować
       for j in range(len(liczba[0])):
           if liczba[i][j]=="#":
              kwadrat(SX,SY,j,-i,kolor)
              used.add((SX+j*BOK,SY-i*BOK))
  


used = set()
while len(used)/12<25: # najwięcej cyfr to 12*25
   
    kolor=kolory[random.randint(1,len(kolory)-1)]
    liczba=(random.randint(0,9)) #losowanie cyfry którą użyję
    X = random.randrange(-200,200,15) #losowanie wspłż X
    Y = random.randrange(-200,200,15) #losowanie współź Y
    rysowanki(used,X,Y,int(liczba),kolor)

input()
