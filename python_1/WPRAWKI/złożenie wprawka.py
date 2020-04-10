""" Złożeniem funkcji f i g nazywamy funkcję zdefiniowaną jako x ↦ f(g(x)).
 Zdefiniuj funkcję compose(f, g) implementującą złożenie funkcji.

"""
x=2
def g1(x):
    return x*2

def f1(x):
    return x +1

def compose2(f, g):
    return lambda x: f(g(x))

def compose(f,g):
    def gf(x):
        return f(g(x))
    return gf
   


def f(x):
    return x+1

def f0(x):
    return x

def repeated(f,n): # pożera funckję i ile razy ma zrobić złożenie
    p = f0
    for i in range(n):
        p = compose(f,p) #p to funkcja f(f(n)) czyli jednokrotne złożenie
        
    return p

print("f złożone 4 razy dla x == 2: ",repeated(f,4)(2))
print ("g złożone 4 razy dla x == 2: ",repeated(g1,4)(2))
print("f złożone 7 razy dla x == 2: ",repeated(f,7)(2))

