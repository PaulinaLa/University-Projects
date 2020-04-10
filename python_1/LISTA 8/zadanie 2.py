"""Mówimy, że jakieś słowo jest układalne z drugiego, jeżeli da się z tego drugiego
wybrać pewne (może wszystkie) literki i ułożyć to pierwsze (być może zmieniając kolejność).
Przykładowo aktyw, kot, motyl są układalne z lokomotywa, a żak i kotka nie są (bo lokomotywa
nie ma w sobie ż i ma tylko jedno k.
Napisz funkcję, która sprawdza, czy jakieś słowo jest układalne z drugiego. Twoja funkcja powinna
wykorzystywać inną funkcję, która zamienia słowo s na słownik, mówiący ile razy w s występuje
dana literka.
"""

def układanka(s): #zlicza mi wystapienie danej literki w słowie tworząc słownik: literka=klucz
    thorking = dict()
    lokiprince = list(s)
    for i in s: 
        if i not in thorking.keys(): # jak klucz się nie powtarza
            thorking[i] = 1
        else:
            thorking[i]+=1
    return thorking

def czyułoży(s,t): # o t się pytam
    kylo = "Nie da się ułożyć " + t + " z " + s
    Rey = "Da się ułożyć " + t + " z "+ s
    leia = układanka(s)
    han = układanka(t)
    for key in han.keys(): # poruszam się po słowniku który mi zwrociło
        if key in leia.keys(): # jeśli element z t pojawia się w s
              if han[key]>leia[key]:
                  return kylo
        else:
            return kylo 
    return Rey


print(czyułoży('wafel','wafelek'))
      
    
    
    
