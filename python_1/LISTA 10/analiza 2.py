"""Zadanie 1.

Wydawca kolekcjonerskiej edycji Lalki Bolesław Prusa zatrudnił Cię do znalezienia odpowiedniego
fragmentu książki na tylną część okładki. Ponieważ format książki nie jest jeszcze znany,
rozważa się także kilka wersji "sprofilowanych" pod kątem ulubionych bohaterów dla czytelnika,
warunki "odpowiedniości" fragmentu nie są jednoznaczne i musisz być przygotowany na każdą ewentualność.
Wiesz jednak, że zostaniesz poproszony o znalezienie fragmentu składającego się maksymalnie z pewnej
określonej liczby wyrazów który zawiera jak najwięcej odwołań do podanego bohatera powieści. Wydawca
może Cię poprosić np. o 120 wyrazowy fragment w którym jak najczęściej wspominany jest Wokulski
(taki fragment istnieje i Wokulski jest w nim wspominany 8 razy). Napisz program, który pozwoli Ci
wypełnić zadanie postawione przez wydawcę bez potrzeby pisania za każdym razem nowego kodu.
Wskazówka: Poszukaj w bibliotece standardowej funkcji dla stringów która zrzuci z ciebie obowiązek
ręcznego sprawdzania wszystkich możliwych odmian poszukiwanego wyrazu.
"""


tekst=open('C:\\Users\\user\\Desktop\\Python\\LISTA 10\\analizka lizka\\lalka.txt').read().split()
stop = len(tekst)
indeksy = []
szukane = 'Wokuls' # żeby znaleźc w odmianie przez przyapadki
n=120
for i in range(len(tekst)):
    if tekst[i].startswith(szukane): #czy dany wyraz zaczyna się od Wokuls
        indeksy.append(i)
aktualne = 0
początek = 0
koniec = 0
for i in range(len(indeksy)): # tak dużo jak ich znalazłam
    licznik = 0
    if indeksy[i]+n>stop: # 120 wyrazowy fragment ponad
        break
    for j in range(indeksy[i],indeksy[i]+n): # range żeby było 120
        if tekst[j].startswith(szukane): # jesli tekst zaczyna sie od Wokulsk
            licznik += 1 # zliczam se słowa
    if licznik > aktualne: # poszukuję fragmentu gdzie mam najwięcej
        aktualne = licznik
        początek  = indeksy[i]
        koniec = indeksy[i]+n
tekst = tekst[początek:koniec]
print(*tekst,aktualne)

        
