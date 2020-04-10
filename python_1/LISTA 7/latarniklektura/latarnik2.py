alfabet=['A','a','Ą','ą','B','b','C','c','Ć','ć','D','d','E','e','Ę','ę','F','f','G','g','H','h','I','i','J','j','K','k','L','l','Ł','ł','M','m','N','n','Ń','ń','O','o','Ó','ó','P','p','Q','q','R','r','S','s','Ś','ś','T','t','U','u','W','w','Y','y','Z','z','Ź','ź','Ż','ż']

def najdluzszy(s):
    maxi= len(s[0])
    pop=[]
    czysto=[]
    słowa=[]
    #słowa=list(wyrki)
    for x in open(('hrabia.txt')):
        wyrazy = x.split()
    for i in range(len (wyrazy)):
        słowa.append(wyrazy[i])
    print (słowa)
    #słowa=list(wyrazy)
    for e in range (len(słowa)):
        a = słowa[e]
        if len(a)> len(maxi):
            maxi=a      #pętla znalazła mi najdłuższe słowo
            print (maxi)
    for e in słowa:
        if len(a)>= len(maxi)-4 : # tworzę liste tych najdłuższych
            pop.append(a) # 4 bo jakby jakieś znaki interpunkcyjne
    for element in pop:
        for litera in element:
            if litera not in alfabet:
                element = element.replace(litera,'')
    for element in pop:
        element = maxi
        if len(element)> len(maxi):
            maxi=element
    for element in pop:
        if len(element)==len(maxi):
            czysto.append(maxi)
    return czysto
 
            
 
    


print(najdluzszy())
            

