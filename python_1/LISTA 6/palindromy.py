"""Parę wyrazów nazwiemy wzajemnie odwrotnymi, jeżeli pierwszy z nich jest
równy drugiemu przeczytanemu wspak. Przykładowo: zakop oraz pokaz. Na stronie wykładu jest
plik z polskimi słowami, Twoim zadaniem jest napisać program, który wypisuje wszystkie wzajemnie
odwrotne pary słów. Każda para powinna być wypisana raz (czyli jeżeli wypisałeś parę zakoppokaz,
to nie powinieneś wypisywać pary pokaz-zakop). Uwaga: program powinien działać szybko,
zastanów się jak uniknąć pętli w pętli (do generowania wszystkich par słów).
"""


wiersze_pliku= open('slowa.txt', encoding='utf8').read().split() #podział na wyrazy

s = set(wiersze_pliku) 

def wzaj_odwrt(s):
    L = [] #tworzę listę ogólną słów
    U = [] #lista która gromadzi mi zużyte słowa żeby palindromy się nie powtarzały przy wypisaniu
    for element in s:
        paltuple = () # tuple gromadzi mi 2 słowa wzajemnie odwrotne
        test = () #testowa krotka
        revers = str(element[::-1]) #odwraca kolejnosc danego słowa ze zb s
        if revers in s:
            test = (element, revers) #w testowej krotce e i rev sa w innej kolejnosci niz w krotce palindrom
            if test not in U: #sprawdzam czy testowa jest na liscie juz uzytych, jak nie to ok
                paltuple = (revers, element) 
                L.append(paltuple) #dodaje palindrom do ogolnej
                U.append(paltuple) #i dodaje do zuzytych zeby potem sprawdzac, zeby tylko raz wywalalo
    return L
    
print (wzaj_odwrt(s))
