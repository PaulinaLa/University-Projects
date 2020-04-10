# bezpośrednio:

def wiel(P,x):
    f=len(P)
    licznik = 0
    for i in range(f):
        y = (P[i]*x**(f-1))
        i=i+1
        f=f-1
        licznik = licznik+y
    return licznik

print("zwykłe zliczanie daje wynik:",wiel([1,0,-1.5,2],2))

def horner(P,x):
    wynik=0
    for e in P:
        wynik=wynik*x + e
    return wynik

#print("schemat hornera daje wynik:",horner([1,0,-1.5,2],2))

def pole(a,b):
    if a*b >0:
        P=a*b
    else:
        P=a*b*(-1)
    return P


def surf(p,xs,xf,dx):
    licznik=0
    while xs<xf:
        m = wiel(p,xs)
        k = pole(m,dx)
        licznik = licznik + k
        xs = xs + dx
    return licznik


        
#print(surf([1,0,3],0,3,0.0001))


assert (0 < 1), "The world has ended!"
assert (1 < 0), "Math's not broken... yet!"
