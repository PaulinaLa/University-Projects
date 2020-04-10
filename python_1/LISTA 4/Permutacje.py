from random import *

def randperm(n):
  P=[]
  z=n
  while len(P)<n:
    x=randint(0,z-1)
    if x not in P:
      P.append(x)
  return P



print(randperm(10))
