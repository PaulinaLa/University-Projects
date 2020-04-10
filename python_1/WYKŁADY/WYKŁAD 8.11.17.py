# program który redukuje powtarzające się elementy w liście
# np z listy która ma [1,2,3,1,2,3,5,8] robię listę [1,2,3,5,8]

def tylko_jeden(L):
    wynik=[]
    for e in L:
        if not e in wynik :# e not in wynik jeżeli elementy e nie znajduje się na liście wynik
            wynik.append(e)
    return wynik


print (tylko_jeden([1,2,3,1,2,3,5,6,9,1,2,111]))

dluga_lista= list(range(10000))
tylko_jeden(dluga_lista)

print(len(tylko_jeden(dluga_lista + dluga_lista)))
print('Skończyłem')

###################################################################################
#Zbiory:
A={1,2,3,4,5,5,5}
B={5,6,7,8,3}
C={3,3,3,3,5,6,8,7} #zbiór ma gdzieś czy element się powtarza, trkatuje go jak 1 element


print(A,B)
print(B==C)

print('A-B=', A-B)
print('A*B=', A&B)
print('A+B=', A|B)
print('A^B=', A^B)# wszystkie elementy które są w jednym ze zbiorów, jesli się powtarza el to go nie wypisze

print('posortowane A=',sorted(A))
print('maksimum A=',max(A))
print('minimum A=',min(A))
print('suma el zb A=',sum(A))
print('długość sumy A+B=',len(A|B))
print(12 in A) # czy 12 nalezy do A? False
print(A<=B) # czy A jest podzbiorem B ?

zbior1 =set('ala ma kota i dwa kanarki')
zbior2 =set(['ala', 'ma','kota'])


print(zbior1)
print(zbior2)
