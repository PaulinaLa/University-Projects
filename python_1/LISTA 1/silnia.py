def silnia(n):
    if n>0:
        res= n*silnia(n-1)
    else:
        res=1
    return res

for i in range(4,213):
    p=len(str(silnia(i)))
    if (p//10)%10==1:  
        print (i,"! ma", p, "cyfr")
    elif p%10==2 or p%10==3 or p%10==4:
        print(i,"! ma",p," cyfry")
    else:
        print(i,"! ma",p," cyfr")
    
