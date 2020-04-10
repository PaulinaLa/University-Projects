"""Szyfr przestawieniowy to taki szyfr, w którym każdej literce z polskiego alfabetu
przypisana jest inna literka (konsekwentnie, w ramach całego komunikatu). W tym i kolejnym
zadaniu, będziemy łamać takie szyfry (czyli pisać programy, które znajdują komunikat, w sytuacji,
gdy mamy znamy jedynie szyfrogram). Będziemy zakładać, że słowa w szyfrogramie oddzielone
są spacjami i (dla zwiększenia czytelności komunikatu), między nimi czasami znajdują się znaki
interpunkcyjne (niezaszyfrowane, otoczone spacjami). Zakładamy również, że wszystkie słowa w
komunikacie występują w słowniku (z polskimi słowami z jednej z poprzednich list) i że nie mamy
żadnych dodatkowych informacji o języku (np. o częstościach liter, czy wyrazów).
Napisz program, który umie rozszyfrować dwa pierwsze szyfrogramy ze SKOS-u. Uwaga: w obu
tych szyfrogramach wszystkie słowa mają unikalną permutacyjną postać normalną (to znaczy, że
znajomość tejże postaci pozwala jednoznacznie wybrać słowo). Uwaga2: każdy szyfrogram jest w
osobnym wierszu, każdy był też szyfrowany osobną permutacją
"""

slowa=open('slowa.txt', encoding = "utf8").read().split()
napis1='fulfolfu ćtąśśótą tlźlźltą'
napis2='udhufńfd ąuąuęąę yrrożdśś śdśsdtsć'

def deszyfruj(napis):
    wynik = []
    napis = napis.split() # dzielę na wyrazy bo spacje się nie zmieniają
    kandydaci = []
    for słowo in napis:
        postac_normalna = ppn(słowo) # zamieniam na postać permutacyjną
        dł = len(słowo) # liczę bo liczba liter się nie zmienia w szyfrze
        for wyraz in slowa: # szukam słowa w pliku o takiej długości
            if len(wyraz) == dł:
                if ppn(wyraz) == postac_normalna: # jeśli postaci się zgadzają to + wynik
                    wynik.append(wyraz)
                    break
    return " ".join(wynik)

def ppn(s): # funkcja z zadania szyfr liczbowy
    slownik={}
    rez=1
    wynik=[]
    for litera in s:
        if litera not in slownik:
            slownik[litera]=rez
            rez+=1
        wynik.append(slownik[litera])
    return "-".join(str(x) for x in wynik) 

print(deszyfruj(napis1))
print(deszyfruj(napis2))
        
