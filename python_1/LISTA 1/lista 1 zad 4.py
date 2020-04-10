from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
   haslo = ""
   while True: #wykonaj dopóki nie zobaczysz breake 
      has1 = losuj_fragment()

      if n - len(has1) >=0 and n - len(has1) !=1:
         n = n - len(has1)
         haslo = haslo + has1 
         #print(has1, end="")
         if n==0:
            return haslo
         
for i in range(0,10):
   print(losuj_haslo(10))

from turtle import*        

def koch(poziom, dlugosc):
  if poziom == 0:
    fd(dlugosc)
  else:
    dlugosc = dlugosc / 3
    koch(poziom-1, dlugosc)
    lt(60)
    koch(poziom-1, dlugosc)
    rt(120)
    koch(poziom-1, dlugosc)
    lt(60)
    koch(poziom-1, dlugosc)

for i in range(3):
  koch(5, 500)
  rt(120)

input() 
