"""Zdefinujmy następujące przekształcenie na słowach (nazwiemy je permutacyjną
postacią normalną): zamieniamy litery na liczby, w ten sposób, że:
1. Tym samym literom przypisane są równe liczby, różnym literom – różne liczby.
2. Liczby przypisywane są po kolei, licząc od lewej strony.
Otrzymane liczby sklejamy w jeden napis, wstawiając na przykład znak "-" jako
separator. Przykładowe pary słowo i wartość przekształcenia:
tak: 1-2-3,
nie: 1-2-3,
tata: 1-2-1-2,
indianin: 1-2-3-1-4-2-1-2. Napisz funkcję, która zwraca w wyniku wartość
opisanego przekształcenia.
"""

def ppn(s):
    slownik={}
    rez=1
    wynik=[]
    for litera in s:
        if litera not in slownik:
            slownik[litera]=rez #przyporządkowuje kolejnym literom słownika, kolejne wartości liczbowe
            rez+=1
        wynik.append(slownik[litera])
    return "-".join(str(x) for x in wynik) #zamieniam na string, aby działała funkcja join

        
print(ppn("indianin"))
print(ppn("tak"))
print(ppn("nie"))
print(ppn("tata"))

