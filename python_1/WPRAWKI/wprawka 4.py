
def n(i):
    return 1

def d(i):
    return i+2

def cont_frac(n,d,k):
    p = 0 #aby gromadzić mi dany poziom
    while k >=0: #tak duzo jak dużo mam poziomów
        r = d(k)+p
        p = n(k)/r
        k = k-1
    return p
        
        
     
         

def tan_cf(x,k):
    cont_frac(n,d,k)
    


    
print (cont_frac(n,d,1))
        
#liczba eulera-2
def deul(i):
    if (i+2)%3 ==0:
        return (2*(i+2))/3
    else:
        return 1


def cont_frac1(n,deul,k):
    p = 0 #aby gromadzić mi dany poziom
    while k >=0: #tak duzo jak dużo mam poziomów
        r = deul(k)+p
        p = n(k)/r
        k = k-1
    return p

print("Przybliżenie e-2 =",cont_frac1(n,deul,100))


#dla tangensa:



def n(i):
    if i==0:
        return i
    else:
        return -1*(i*i)
    

def d(i):
    if i==0:
        return 1
    else:
        return d(i)==d(i-1)+2

print(d(2))

    



























        
