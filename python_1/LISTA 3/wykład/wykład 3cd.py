#piszemy program z wykorzystaniem wiadomości o listach:
#modyfikacja list i funkcja appand 

x=1
y=[1,2,3]
a=b=0
def pisz():
    print('x,y=', x, y)


def f(a,b):
    a+=1 #równoważne a= a+1
    b+=['nowy'] #równoważne b.expand(['nowy'])
    print(a,b)

def f2(a,b):
    a+=1 
    b = b+['nowy'] 
    print(a,b)


#f(x,y); pisz()
f2(x,y); pisz()


print('globalne a,b=', a,b)

#ala ma 33 koty-> ala ma ** koty

def usun_cyfry(s):
    wynik = []
    for i in s:
        if '0' <=a <='9':
            wynik.append('*')
        else:
            wynik.append(a)
        return '' .join(wynik)
def usun_cyfry0(s):
    L= list(s)
    for i in range(Len(L)):
        if L[i] >= '0' and L[i] <= '9':
            L[i] = '*'
        return '' .join(L)

def usun_cyfry1(s):
    s=list(s)
    for i in range(len(s)):
        if s[i] >= '0' and s[i]<= '9':
            s[i]='*'
        return ''.join(s)




print (usun_cyfry('ala ma 33 koty i 56 kanarków.'))
       









from turtle import fd, bk, lt, rt, speed


def kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(90)

kwadrat(100)




















