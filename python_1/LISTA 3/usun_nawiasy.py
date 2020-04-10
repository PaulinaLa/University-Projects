def usun_nawiasy(s):
    L=list(s)
    for i in range(len(L)):
        if L[i] =='(':
            L[i]=''
            for j in range (i, len(L)):
                if L[j]==')':
                    L[j]=''
                    break
                else:
                    L[j]=''
    return ''.join(L)
            
       

print(usun_nawiasy("uksjshssdkjdnbaskzmbgalgb(cokolwiek)hsh(dom)skjbkjsbkjs( perskiego )!"), end='')
         




