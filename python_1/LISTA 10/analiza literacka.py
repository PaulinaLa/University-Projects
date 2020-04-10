"""Wybierz jedno zadanie z Analizy Literackiej (pojawią się na SKOS)
i zaprezentuj jego rozwiązanie. Zadanie 1.
Jesteś osobą projektującą okładki do książek.
Otrzymałeś zlecenie na okładkę do Lalki Bolesława Prusa, przy czym zleceniodawca chciałby,
żeby na tylnej części okładki znalazł się jakiś ciekawy fragment tej książki (to Ty masz wybrać, jaki dokładnie).
Gdy ukończyłeś projekt, zdałeś sobie sprawę, że wybrana przez Ciebie czcionka nie ma polskich liter.
Szczęśliwie na stronie tytyłowej ich nie było (B. Prus, Lalka, Wydawnictwo: Nasze Lektury, Radomsko 2011),
ale co zrobić z zachęcającym do zakupu tekstem?
Napisz program, który dla zadanego pliku z tekstem książki znajduje najdłuższy spójny fragment
(żeby uczynić obserwacje programu ciekawszym, możesz wypisywać aktualnie najdłuższy znaleziony fragment),
w którym nie występują żadne polskie znaki diakrytyczne (czyli litery z ogonkami i kreskami).
Nie wolno przecinać wyrazów, długość tekstu mierzymy jako sumę długości poszczególnych wyrazów
(czyli nie liczą się spacje i znaki przestankowe). Wszystkie wyrazy tekstu powinny być wyrazami polskimi
(na poprzedniej liście była lista polskich słów)."""

import re #Regular expression operations

lalka = open('C:\\Users\\user\\Desktop\\Python\\LISTA 10\\analiza literacka\\lalka.txt').read()

def spojny(S):
    F = [] #lista na fragmenty
    F = re.findall('[^ąęółźśćżń]+', S)#wyrazenie takie ze nie zawiera wymienionych znakow dluzsze niz 1
    maxi = 0
    for e in F: #szuka najdluzszego fragmentu
        if len(e) > maxi:
            maxi = len(e)
    for e in F: #printuje najdluzszy fragment
        if len(e) == maxi:
            print(e)

spojny(lalka)
