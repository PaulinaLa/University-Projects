from math import*

def liczba_pierwsza(n):
    for e in range(2,int(sqrt(n))): # sqrt zmniejsza czas działania programu poprzez zmniejszenie przedziału
        if (n% e)==0:
            return False
    return True

Liczba=0
def hiper(n,k):
    for i in range(10**n-1, 10**(n-1), -1):
        if (str(i).find(k*"7") >=0):
            for j in range(2, int(sqrt(i))):
                if liczba_pierwsza(j) :
                    break
            Liczba = i
            break
    return Liczba


print(hiper(10,7))


