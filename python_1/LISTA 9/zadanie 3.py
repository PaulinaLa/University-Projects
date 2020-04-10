wiersze_pliku= open('slowa.txt', encoding='utf8').read().split('\n') #podział na wyrazy
magazyn = dict()

for x in wiersze_pliku: #open(wiersze_pliku): #'slowa.txt').read().split('\n'):
    magazyn[(''.join(sorted(x)))] = x  # dodaje słowa do słownika

def układanka(s): #zlicza mi wystapienie danej literki w słowie tworząc słownik: literka=klucz
    thorking = dict()
    lokiprince = list(s)
    for i in s: 
        if i not in thorking.keys(): # jak klucz się nie powtarza
            thorking[i] = 1
        else:
            thorking[i]+=1
    return thorking


def zagadka2(x):
