#Napisz funkcję, która bierze liczbę i zwraca zbiór jej pierwszych dzielników

from math import *

def pierwsza(n):
    for e in range(2,n):
        if (n% e)==0:
            return False
    return True

def dzielnik(n):
    P = set()
    for i in range(2,n+1):
        if n%i == 0:
            if pierwsza(i):
                P.add(i)
    return P


print("dzielniki pierwsze liczby 578:", dzielnik(578))
            
            

