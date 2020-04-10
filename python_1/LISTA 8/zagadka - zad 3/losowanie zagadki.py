import random
wiersze_pliku= open('slowa.txt', encoding='utf8').read().split('\n') #podział na wyrazy
magazyn = dict()

for x in wiersze_pliku: #open(wiersze_pliku): #'slowa.txt').read().split('\n'):
    magazyn[(''.join(sorted(x)))] = x  # dodaje słowa do słownika

def zagadka(x):
    x = x.lower() # tylko małe literki
    słowo = []
    for i in x:
        if i!= " ":
            słowo += i # przeskakuje do kolejnego słowa
    while True:
        random.shuffle(słowo)
        dług = random.randrange(3, len(słowo) - 3) # element losowo wybrany z zakresu
        imię = ''.join(sorted(słowo[0:dług])) # żeby był podział na 2 słowa to najpierw od 0 do dług
        nazwisko = ''.join(sorted(słowo[dług:]))# od dług do końca
        if imię in magazyn.keys(): # jeśli imię jest w kluczach w słowniku
            if nazwisko in magazyn.keys():
                imię = magazyn[imię] # odczytuje wartośc
                nazwisko = magazyn[nazwisko]
                break
    return str(imię) + " " + str(nazwisko)


print(zagadka("Anna Kot"))

#słownik w którym klucze to literki a wartości to lista słów układalnych


    
