import time
import turtle

def usun_nawiasy(s):
  while '(' in s:
    a = s.index('(')
    b = s.index(')')
    s = s[:a] + s[b+1:]

  return s

napis = "Ala ma kota (perskiego) i 2 (2!) kanarki."
  
print (usun_nawiasy(napis)) 

def testuj_un(N):
  s = N * '(x)'
  t0 = time.time()
  usun_nawiasy(s)
  t1 = time.time()
  return t1 - t0
  
czasy = []

for i in range(1,100):
  czasy.append(testuj_un(i * 1000))   
  
for i in range(len(czasy)):
  turtle.goto(i * 3, 200 * czasy[i])   
  
