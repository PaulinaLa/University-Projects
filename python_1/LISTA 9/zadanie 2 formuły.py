import re
#narzedzia do znakow regularnych

def ciagi_binarne(N):
  if N == 0:
    return [ [] ]
  return [ [b] + c for b in [True, False] for c in ciagi_binarne(N-1)]
#ciagi_binarne konstruuje wszystkie mozliwe wartosciowania dla N zmiennych
    
# 2 --> [ [False, False], [False, True], [True, False], [True, True] ]    


def wartosciowania(zmienne):
  cb = ciagi_binarne(len(zmienne))  
  return [ dict(zip(zmienne, ciag)) for ciag in cb]
#zip robi pary z dwoch tablic
#przyporzadkowywuje wartosciowania dla zmiennych
  
def wartosc_formuly(F, wart):
  F = F.replace('*', ' and ')
  F = F.replace('+', ' or ')
  F = F.replace('-', ' not ')
  F = F.replace('T', 'True') #dodanie stałych
  F = F.replace('F', 'False')
  print (F, wart)
  return eval(F, wart)
#printuje ladniejszy zapis formuly i wartosciowanie
#zwraca to samo ale nie string tylko kod

def tautologia(F):
  #zmienne = set(F) - set('+*()- ')ze zbioru zmiennych usuwa znaki
  zmienne = set(re.findall('\w+', F)) #znajduje slowa dlgosci 1 lub wiecej znakow
  for wart in wartosciowania(zmienne):#dla wartosciowan ktore sa przyporzadkowane zmiennym
    if wartosc_formuly(F, wart) == False:
      return False #jesli jakiekolwiek wartosciowanie jest falszem to wywala falsz
  return True    
  
  
print (tautologia('(-p) + (T)')) #tautologia
print(tautologia('(-p) * (qrherh) + (-r)')) #nie tautologia
