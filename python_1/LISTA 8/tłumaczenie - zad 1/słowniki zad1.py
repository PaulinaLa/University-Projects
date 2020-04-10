alfabet=['A','a','Ą','ą','B','b','C','c','Ć','ć','D','d','E','e','Ę','ę','F','f','G','g','H','h','I','i','J','j','K','k','L','l','Ł','ł','M','m','N','n','Ń','ń','O','o','Ó','ó','P','p','Q','q','R','r','S','s','Ś','ś','T','t','U','u','W','w','Y','y','Z','z','Ź','ź','Ż','ż']
def ktory(X):
    ilosc=[]
    for i in range(len(X)):
        licznik=0
        for e in open('Brown.txt'):
            e = e.split()
            for j in range(len(e)):
                if e[j]==X[i]:
                    licznik+=1
        ilosc.append((licznik,X[i]))
    ilosc.sort()
    ilosc = [(b) for a,b in ilosc]
    ok = ilosc[len(ilosc)-1]
    return ok

def tlumacz(zdanie):
    wynik=[]
    for p in zdanie.split(): # dla każdego wyrazu w zdaniu
        if p in pol_ang: # jeśli ten wyraz jest w słowniku
            kandydaci = pol_ang[p] # zmienna kandydaci= aktualne tłumaczenie
            if len(kandydaci)>1: # jeśli mam więcej niż jedno tłumaczenie
                wynik.append(ktory(kandydaci)) # sprawdzony kandydat do wyniku
            else:
                # gdy mam tylko jedno tłumczenie danego słowa
                wynik.append(pol_ang[p][0])
                #k = pol_ang[p] # jednowyrazowa lista która nie miesza w wyniku
                #k1 = k[0] # jedyny element tej listy
                #wynik.append(k1)
        else:
           wynik.append('?' + p)
    return ' '.join(wynik)
    

pol_ang = {} 

for x in open('pol_ang.txt', encoding='utf8'):
  x = x.strip() # usuwa początkowe i końcowe białe znaki
  L = x.split('=') # dzieli ze względu na =
  if len(L) != 2:
    continue
  pol, ang = L
  
  if pol not in pol_ang:
    pol_ang[pol] = [ang]
  else:  
    pol_ang[pol].append(ang)

zdanie1='Paweł idzie do szkoły'
zdanie='ja być zły i zmęczony'
print(tlumacz(zdanie1))


