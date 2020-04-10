from turtle import*

def krzyzyk(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    lt(45)
    fd(bok)
    rt(90)
    fd(bok)
    for i in range(3):   
        lt(90)
        fd(bok)
        rt(90)
        fd(bok)
        rt(90)
        fd(bok)
    lt(90)
    fd(bok)
    end_fill()
        
def mieszanka(a, k1, k2):
  r1,g1,b1 = k1
  r2,g2,b2 = k2
  
  return ( a * r1 + (1-a) * r2, 
           a * g1 + (1-a) * g2, 
           a * b1 + (1-a) * b2 )

  
k1 = (1,0,1)
k2 = (1,1,0)

def mieszanka2(b, p1, p2):
  r1,g1,b1 = p1
  r2,g2,b2 = p2
      
  return ( b * r1 + (1-b) * r2, 
           b * g1 + (1-b) * g2, 
           b * b1 + (1-b) * b2 )

p1 = (0.5,1,0)
p2 = (0.3,0,1)
  

def koleczko(bok):
    speed('fastest')
    a=0.05
    b=0.05
    for i in range(20):
        krzyzyk(bok, mieszanka(a,k1,k2))
        a=i*0.05
        rt(126)
        pu()
        fd(bok*1.8)
        pd()
    for i in range(20):
        krzyzyk(bok, mieszanka2(b,p1,p2))
        b=i*0.05
        rt(126)
        pu()
        fd(bok*1.8)
        pd()



print(koleczko(20))
