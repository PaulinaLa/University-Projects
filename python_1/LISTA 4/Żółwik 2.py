from turtle import *
import random

def kwadrat(bok, kolor):
  fillcolor(kolor)
  begin_fill()
  for i in range(4):
    fd(bok)
    rt(90)
  end_fill()

def mieszanka(a, k1, k2):
  r1,g1,b1 = k1
  r2,g2,b2 = k2
  
  return ( a * r1 + (1-a) * r2, 
           a * g1 + (1-a) * g2, 
           a * b1 + (1-a) * b2 ) 
  
k1 = (1,0,1)
k2 = (1,1,0)

bok=30
speed('fastest')
n=16

for i in range(n):
    a = i * 0.05
    kwadrat(bok, mieszanka(a, k1, k2))
    lt(90)
    fd(bok)
    rt(90)
kwadrat(bok, mieszanka(a, k1, k2))
lt(90)
for j in range(18):
  a = i * 0.05
  for i in range(n):
      kwadrat(bok, mieszanka(a, k1, k2))
      lt(90)
      fd(bok)
      rt(90)
  kwadrat(bok, mieszanka(a, k1, k2))
  lt(90)
  n = n-1


