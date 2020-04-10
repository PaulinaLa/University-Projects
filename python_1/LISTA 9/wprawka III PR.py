'''Napisz funkcję reprezentant(L), która dla niepustej listy liczb
całkowitych dodatnich L znajduje najmniejszą liczbę k-cyfrową,
gdzie k jest liczbą cyfr największej liczby.
Przykładowo:
>>> reprezentant([1,2,3,4])
1
>>> reprezentant([1,2,3,44,55])
44
>>> reprezentant([1,2,3,4,5,6,7,8,9,10])
10
'''

L1 = [1,2,3,4]
L2 = [1,2,3,44,55]
L3 = [1,2,3,4,5,6,7,8,9,10]

def reprezentant(L):
    maxlen = 0
    for e in L: #szukamy maksymalnej dlugosci liczby
        if len(str(e)) > maxlen:
            maxlen = len(str(e))
    minnum = int('9'*maxlen)
    for e in L: #szukamy najmniejszej liczby o takiej dlugosci
        if len(str(e)) == maxlen:
            if e < minnum:
                minnum = e
    return minnum

print(reprezentant(L1))
print(reprezentant(L2))
print(reprezentant(L3))
