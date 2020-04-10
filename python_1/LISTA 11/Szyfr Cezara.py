""" Szyfrowanie metodą Cezara polega na tym, że każdą literę danego słowa zamienia
się na literę przesuniętą o k pozycji (zgodnie z porządkiem alfabetycznym, w którym po ostatniej
literze (ż) następuje litera pierwsza (a)). W szyfrze Cezara kluczem umożliwiającym szyfrowanie
(i odszyfrowanie) jest liczba k.
Napisz funkcję ceasar(s,k), która dla danego słowa s i klucza k znajduje wartość szyfrogramu.
Pamiętaj, by używać polskiego alfabetu (aąbcćdeęfghijklłmnńoóprsśtuwyzźż). Zastanów się, jak
można byłoby tu wykorzystać słowniki i funkcję zip do utworzenia zwięźlejszego i eleganckiego
kodu.
"""

def ceasar(s,k):
    wazne='aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    alfabet={k:1 for k in 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'}
    j=0
    for i in wazne:
        if i in alfabet:        #dodaję litery jako klucze, kolejne liczby jako wartości słownika
            alfabet[i] += j
            j += 1
    nowy = alfabet.copy()         #kopia słownika posłuży jako materiał na przesunięty szyfr o k wartości
    for i in wazne:
        if i in nowy:
            nowy[i] += k
            if nowy[i]>32:
                nowy[i] -= 32     #jeśli wychodzi poza zakres, zaczynam od początku
    wynik=[]
    for litera in s:
        wart = nowy[litera] #odczytuję sobie wartość w słowniku
        for j in alfabet:
            if alfabet[j] == wart:
                wynik.append(j) #tworzę ostateczny wynik
    return ''.join(wynik)
       
print(ceasar('szaleństwo',7))

#Funkcja zip() tworzy za to listę tupli z podanych elementów

    
