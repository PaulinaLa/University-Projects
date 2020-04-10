""" Łamigłówką arytmetyczną jest zadanie, w którym należy literom przyporządkować (różne) cyfry w ten sposób,
by będące treścią zadania dodawianie było prawdziwe. Przykładowe zadania to:
SEND                     CIACHO
+ MORE                 + CIACHO
-------                 ---------
MONEY                    NADWAGA

Napisz program, który rozwiązuje łamigłówki arytmetyczne. W programie powinna być funkcja, której argumentem jest
napis przedstawiający zagadkę (przykładowo "send + more = money", a wynikiem słownik kodujący (jakieś)rozwiązanie.
Gdy rozwiązanie nie istnieje, funkcja powinna zwracać pusty słownik (ew. wartość None).
"""

import itertools

def lamiglowka(napis):
    litery = set(napis)-set('+=') #odsiewam znak + i = 
    if len(litery)>10 or len(litery)==0: # >10 bo mam cyfry 0-9 czyli 9 cyfr
        return None # rozw nie istnieje 
    else:
        lewa, prawa = napis.split('=') #dzieli napis na listę ze wzgl na = 
        lewa = lewa.split('+') # z lewej robię osobną listę ze względu na +
    
        cyfry = range(10) # bo 0-9                          #wszystkie możliwe uporządkowania,krotki długości len(litery)
        for permutacja in itertools.permutations(cyfry, len(litery)):#brak powtarzających się elementów
            rozwiazanie = dict(zip(litery, permutacja))  # zip łączy wiele list w jedną cyzli robi mi value-key
                    #dla każdego słowa z lewej str sumuje jego wartośc i sprawdzam czy jest równe prawej
            if sum(wartosc(slowo, rozwiazanie) for slowo in lewa) == wartosc(prawa, rozwiazanie):
                return rozwiazanie
        return None
    
def wartosc(slowo, zamiennik):
    s = 0
    lit = 1
    for litera in reversed(slowo): # bo liczby musza być w dobrym porządku 
        s += lit * zamiennik[litera] # nie 001 tylko 100
        lit *= 10
    return s
                
print(lamiglowka('matma+studia=sukces'))
