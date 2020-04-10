#Funkcja only_one pozwala na omijanie powtarzających się elementów z listy

def only_one(L):
    poprawa = []
    for i in L:
        if i not  in poprawa :
            poprawa.append(i)
    return poprawa


print (only_one([1,2,3,1,2,3,5,6,9,1,2,111]))

