"""Napisz rekurencyjną funkcję, która generuje zbiór wszystkich sum podzbiorów listy liczb L
(czyli jeżeli L była równa [1,2,3,100], to funkcja powinna zwrócić zbiór
set([0,1,2,3,4,5,6, 100, 101, 102, 103, 104, 105, 106])
"""

def wszystkie(L):
 if len(L) == 0:
     return []
 return {L+list((L[i] + reszta) for i in range(len(L)) for reszta in wszystkie(L[:i])+L[i+1:])}

#zwraca mi  for i in range(len(L):
            #for reszta in wszystkie( L[ : i] + L[ i+1 : ]) podziałka ze względu na i, rekurencja
            #return L + list((L[i] + reszta))
 
print(zbiorsum([0,1,2,3,100]))
print(wszystkie([0,1,2,3,100]))
