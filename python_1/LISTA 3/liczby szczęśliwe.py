from math import*

def liczba_pierwsza(n):
    for e in range(2,int(sqrt(n))): # sqrt zmniejsza czas działania programu poprzez zmniejszenie przedziału
        if (n% e)==0:
            return False
    return True

licznik=0

for n in range(1,100000):
    if (liczba_pierwsza(n)):
        if str(n).find("777") >=0: #jeżeli funkcja find znajdzie taką liczbę to +1
            licznik = 1+ licznik  #zliczanie ilości liczb 
            print(n)
print("Jest dokładnie", licznik, "liczb szczęśliwych w przedziale 1-1000000")
