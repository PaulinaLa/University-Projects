
slowa = open('C:/Użytkownicy/user/Pulpit/Python/LISTA7/lataniklektura/lektura.txt').read().split()

letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmęóąśłżźćń'
alfabet = list(letters)

def longest(s):
    maks = len(s[0])
    long = []
    for word in s: #szuka maksymalnej dlugosci ogolnie
        if len(word) > maks:
            maks = len(word)
    for word in s:
        if len(word) >= (maks-3): #robi liste z maks - 3 bo niektore moga miec sporo znakow
            long.append(word)
    bezspojnikow = []
    for e in long:
        for l in e:
            if l not in alfabet:
                e = e.replace(l, '')
        bezspojnikow.append(e)
    maks = len(bezspojnikow[0]) #zmienia maks na dlugosc pierwszego wyrazu w liscie bezspojnikow
    for word in bezspojnikow: #szuka maksymalnej dlugosci
        if len(word) > maks:
            maks = len(word)
    lista = [] #ostateczna lista
    for word in bezspojnikow: #wypisuje te ktorych dlugosc rowna sie maks
        if len(word) == maks:
            lista.append(word)
    print(lista)



        
longest(slowa)
