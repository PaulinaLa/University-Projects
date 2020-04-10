from random import randint
#definiuje ciągi wykorzystywane w grze-te które spodobają się smokowi
def ciag5():
    a=0
    rzut=100 #bo 100 rzutów kostką
    liczby=[]#tworzę pustą listę w której będę gromadzić liczby podejrzane o bycie 5el ciągiem
    
    while(rzut!=0):
        x=randint(1,6) # jakakolwiek liczba od 1-6
        liczby.append(x) # dodaje x do listy liczby
        #print("Rzucam kością, a oto Twój wynik:",liczby[a])
        if(liczby[a]>liczby[a-1]>liczby[a-2]>liczby[a-3]>liczby[a-4]): #ciąg 5cio el rosnący
            return 1    
        rzut=rzut-1
        a=a+1
    return 0
       
def ciag6():
    a=0
    rzut=100
    liczby=[]
    while(rzut!=0):
        x=randint(1,6)
        liczby.append(x)
        #print(liczby[a])
        if((a>6) and (liczby[a]>=liczby[a-1]>=liczby[a-2]>=liczby[a-3]>=liczby[a-4]>=liczby[a-5])):
            return 1
            #print("Zwycięstwo! Możesz przejść...")
        rzut=rzut-1
        a=a+1
    return 0

#p=input("Jam jest smok Wykidajło, od wieków strzegę tej jaskini! Przejdziesz tylko jeśli rzucając sto razy kością, uda Ci się wyrzucić pięcioelementowy ciąg rosnący, lub sześcioelementowy ciąg niemalejący. Aby wybrać pierwszy wpisz '1' lub '2', aby wybrać drugi. Powodzenia!")
"""
if int(p)==1:
    ciag5()
else:
    ciag6()
    """

def testuj5():
    wygrane = 0
    for i in range(10 ** 5):
        wygrane += ciag5()
    return(wygrane / i)

print("Prawdopodobieństwo wyrzucenia ciągu 5-elementowego:",testuj5())

def testuj6():
    wygrane=0
    for i in range(10**5):
        wygrane = wygrane +ciag6()
    return (wygrane/i)

print("Prawdopodobieństwo wyrzucenia ciągu 6-elementowego:", testuj6())
    
