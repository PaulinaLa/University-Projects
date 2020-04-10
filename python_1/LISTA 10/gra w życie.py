# Gra w życie (wersja graficzna)
##########################################

import kwadrat

kwadrat.tracer(0,10)

kolonia_txt = """
...............................
...............................
...............................
............############.......
...............................
...............................
...###.........................
...#............###.....###....
....#.............###..........
...............................
"""

T = [list(w) for w in kolonia_txt.split()]

def rysuj(T):
  kwadrat.clear()
  for y in range(len(T)):
    for x in range(len(T[y])):
      if T[y][x] == '#':
        kolor = 'magenta'
      else:
        kolor = 'yellow'
      kwadrat.kwadrat(x, y, kolor)
  kwadrat.update()    

def sasiedzi(x,y):
  wynik = []
  for dx,dy in [ (-1,-1), (-1, 1), (1,-1), (1,1), (0,-1), (0,1), (1,0), (-1,0)]:
    nx = (x + dx) % MX
    ny = (y + dy) % MY
    wynik.append( (nx, ny) )
  return wynik
      
MY = len(T)    
MX = len(T[0])
    
def pusta_tablica():
  return [ MX * ['.'] for i in range(MY)]

def nowe_pokolenie(T):
  P = pusta_tablica()
  for y in range(MY):
    for x in range(MX):
      liczba_sasiadow = 0
      for nx,ny in sasiedzi(x,y):
        if T[ny][nx] == '#':
          liczba_sasiadow += 1
      if T[y][x] == '#' and liczba_sasiadow in [2,3]:
        P[y][x] = '#'
      elif T[y][x] == '.' and liczba_sasiadow == 3:
        P[y][x] = '#'       
  return P 

licznik = 0
historia = set()  
  
while True:
  licznik += 1
  rysuj(T)
  T = nowe_pokolenie(T)
  if str(T) in historia:
    print ('koniec:', licznik)
    break
  historia.add(str(T))  
