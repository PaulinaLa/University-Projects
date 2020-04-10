


def sgn(n):
    if n>0:
        return 1
    elif n==0:
        return 0
    else:
        return -1

    
def plus1(x):
    return x+1

def pomoc(P,horner):
        def horner(P,x):
            wynik=0
            for e in P:
                wynik=wynik*x + e
            return wynik
    return horner(P,x)

def bisect(f,x,y):#horner obliczy mi wartość wielomianu w danym punkcie
    e = 2**(-32)
    S=0
    assert (sgn(x) != sgn(y)),"Funkcja nie ma miejsca zerowego na podanym przedziale"
    p = f(x)
    if abs(p) <e:
        return x
    S =(x+y)/2
    if abs(f(S))< e:
        return S
    elif sgn(f(S)*f(x)) >0:
       return bisect(f,S, y)
    else:
       return bisect(f,x,S)

print(bisect(plus1,-2,2))


        
              
    
