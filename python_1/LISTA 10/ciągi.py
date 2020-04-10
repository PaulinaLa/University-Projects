"""Napisz rekurencyjną funkcję, która generuje wszystkie ciągi niemalejące
o długości N, zawierające liczby od A do
B.

"""

"""
def lista(a,b):
    L=[]
    for i in range(a,b+1):
        L.append(i)
    return L
"""

def dobryciag(L,n):
     if n==0:
          yield [] # aby funckja stała sie funckją generującą używam yield
     else: 
         for i in range(len(L)):
             for j in dobryciag(L[i+1:],n-1):
                 yield [L[i]]+j # tworzę generator = funckja lista


def ciagi(a,b,n):
    return dobryciag([x for x in range(a,b+1)],n)
 
for x in ciagi(1,4,2): # a = 1, b = 4, N = 2
     print (x)

