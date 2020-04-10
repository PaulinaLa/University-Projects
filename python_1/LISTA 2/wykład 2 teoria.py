#from random import randint #funkcja związana z losowością

#def kostka():
 #   return randint(1,6)

#licznik = 0

#k1=k2=0
#k1,k2 = 0,0

#while True: # nieskończona pętla (pozornie)
 #   licznik += 1 #licznik = licznik+1
  #  k1= kostka()
   # k2 = kostka ()
    #print(licznik, k1, k2)
    #if k1 + k2 == 12:
     #   break # zakończ działanie pętli

#print(40*"-")

#LISTY
#programy działające na listach: definiuję listę :L=[1,4,6,7,34]
#mogę dodawać listy: L+L
#mogę mnożyć listy: 2*L
# L += [8,8,8]

import time
import sys
sys.setrecursionlimit(11000)

def rev1(L):#próbujemy odwrócić listę, rev bo reverse
    L0 = L[:] #kopiowanie listy
    for i in range(len(L)//2):
        j= len(L) - 1 - i
        L0[i], L0[j] = L0[j], L0[i]
    return L0

def rev2(L):
    wynik=[]
    for i in range(len(L)):
        wynik.append( L[len(L) - i -1]) #dodaję kolejne elementy do pamięci, czyli rozszerzam wynik o wartość w nawiasie
    return wynik

def rev3(L):
    wynik = []
    for e in L: #sposób przeglądania listy, for (zmienna) in (coś co generuje):
        wynik = [e] + wynik # e to konkretna wartość zmiennej 
    return wynik


# wycinki list: każdy element listy ma przypisany numerek, mozliwe jest
# wycięcie fragmnetu listy (zdublowanie)pisząc odpowiedni numer
# przypisany danemu elementowi gdy
# L=['ala', 'ma', 'kota', 'i', 'dwa', 'kanarki']
# L[1:4] podaj elementy od 1 do 4, L[1.67] podaje elementy do samego końca
# L[:5]podaj elementy do 5tego
# L[2:3] ['wielkiego', 'tłustego', 'kota'] - wkłada zamiast drugiego elementu 

def rev4(L):
    if len(L) == 0:
        return []
    return rev4(L[1:]) +[L[0]]

def rev5(L):
    L= L[:]#wycinanie kawałka listy
    L.reverse()
    return L

def rev6(L):
    return L[::-1]
#napiszmy funkcję, która testuje fujkcje rev

def testuj(rev,N):
    L = list(range(N))
    T0= time.time()
    rev(L)
    print (rev, time.time()-T0)
    
for rev in [rev1, rev2, rev3, rev4]:
    testuj(rev,15000)



                      








