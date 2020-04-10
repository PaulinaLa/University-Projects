
#analiza Collatza program, który oblicza energię liczby

def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1
    
def zamien(a,b):
    
    if a>b:
        print("Zły format przedziału, naprawię go.")
        c=b
        w=a
        b=w
        a=c
    else:
        print("Dobry przedział, już zabieram się do liczenia.")
    

def ciag(a):
    P=[]
    P.append(a)
    w=F(a)
    P.append(w)
    while w!=1:
            w = F(w)
            P.append(w)
    return P


def srednia(P):
    w=0
    if len(P)==1:
            return len(ciag(e))
    else:
        for e in P:  
         w += e
    Śr= w/len(P)
    return Śr

def media(P):
    L = sorted(P)
    G=[]
    if len(L)%2 == 0:
        G.append(L[len(P)//2])
        G.append(L[len(P)//2]-1)
        return srednia(G)
    else:
        return L[len(P)//2]

def anaco(a,b):
    P=[]
    L=[]
    print("Policzę analizę Collatza dla (",a,",",b,")")
    if a>b:
        c=b
        w=a
        b=w
        a=c
        print("Zły format przedziału, naprawię go. Teraz a=",a,",a b=",b)
    else:
        print("Dobry przedział, już zabieram się do liczenia.")
        
    for i in range(a,b+1):
        P.append(i)
    for i in P:
        ciag(i)
        L.append(len(ciag(i)))
        print("Ciąg Collatza dla liczby",i,"to:",ciag(i))
        print("A energia liczby",i,"to",len(ciag(i)))
        print("-"*80)
    print("Za to średnia energia liczb z tego przedziału =", srednia(L))
    print("Mediana tego przedziału wynosi", media(L))
    print("Maksymalna energia liczby w przedziale (",a,",",b,"), to:", max(L))
    print("Minimalna energia liczby w przedziale (",a,",",b,"), to:", min(L))    
      
    
    
        
print(anaco(7,2))

