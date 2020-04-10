"""Bardzo użyteczną metodą dla napisów jest split, która dzieli napis ze względu
na ciągi białych znaków, tak że
" Ala ma kota ".split() == ["Ala", "ma", "kota"]
Zaimplementuj funkcję podziel(s), która dzieli napis na listę napisów tak samo,
jak spit"""

def podziel(s):
    wynik=''
    L=[]
    for i in range(len(s)):
        if s[i] !=" ":
            wynik=wynik+s[i]
        elif len(wynik)>0:
                L.append(wynik)
                wynik=''
    if wynik != '':
        L.append(wynik)
    return L
        

print(podziel("Ala ma kota    psota    "))


def lista(L):
    for e in L:
        L[e] == 1
    return L

print(lista([1,2,3]))
