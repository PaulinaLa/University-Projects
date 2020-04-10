import math

def zdubluj(x):
    return 2*x

#zdubluj("trzy")
#wynik:'trzytrzy'
# można dublować listy, liczby, napisy
#gdy zdubluj('trzy')[4] wynik: 't' dubluje 5ty element licząc od zera
>> "abrakadabra"[1:6]
'braka'
>>> "abrakadabra" [1:100:2]
'baaar'
'arbadakarb'
>>> "abrakadabra"[::1]
'abrakadabra'
>>> #odwracam listę


>>> A=[1,2,3,4,5]
>>> B=A
>>> B[3]=999
>>> A
[1, 2, 3, 999, 5]
>>> #A patrzy an ten sam element w liście co B dlatego zamiana elem b zamienia el b
>>> C=[1,2,3,4,5,6]
>>> A=C
>>> B[3]=777
>>> A
[1, 2, 3, 4, 5, 6]
>>> C
[1, 2, 3, 4, 5, 6]
>>> B
[1, 2, 3, 777, 5]
>>> B=C
>>> B[3]=777
>>> A
[1, 2, 3, 777, 5, 6]
>>> B
[1, 2, 3, 777, 5, 6]
>>> C
[1, 2, 3, 777, 5, 6]
>>> B=A[:]
>>> A
[1, 2, 3, 777, 5, 6]
>>> B
[1, 2, 3, 777, 5, 6]
>>> A=[1,2,3,4,5,6]
>>> B=A[:] #tworzenie kopii
>>> B
[1, 2, 3, 4, 5, 6]
>>> A
[1, 2, 3, 4, 5, 6]
>>> 
