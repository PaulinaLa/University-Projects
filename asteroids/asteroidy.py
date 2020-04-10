import pygame
import random
import sys
import os
import math
import datetime


#Funkcje pomocnicze

def laduj_obraz(nazwa): #ładuje określony przez nazwę "nazwa" obraz i odpowiednio konwertuje
    return pygame.image.load(os.path.join('obrazy', nazwa)).convert_alpha()

def rysuj(powierzchnia1, powierzchnia2, pozycja):
    rect = powierzchnia1.get_rect()
    rect = rect.move(pozycja[0] - rect.width//2, pozycja[1] - rect.height//2)
    powierzchnia2.blit(powierzchnia1, rect)

def laduj_dzwiek(nazwa):  #ładuje dźwięk w podobny sposób jak obrazy
    return pygame.mixer.Sound(os.path.join('dzwieki', nazwa))


def obracaj(obraz, rect, angle): #obraca podany obraz 
    obracaj_obraz = pygame.transform.rotate(obraz, angle)
    obracaj_rect = obracaj_obraz.get_rect(center = rect.center)
    return obracaj_obraz, obracaj_rect


def dystans(x, y): #pomaga określić odległośc pomiędzy dwoma punktami 
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


#Główne klasy

class Obiekt_Gry(object): #wszystkie obiekty w grze mają swoją pozycję i obraz
    def __init__(self, pozycja, obraz, speed=0):
        self.obraz = obraz
        self.pozycja = list(pozycja[:])
        self.speed = speed

    def narysuj(self, ekran):
        rysuj(self.obraz, ekran, self.pozycja)

    def rozmiar(self):
        return max(self.obraz.get_height(), self.image.get_width())

    def promien(self):
        return self.obraz.get_width()/2


class Plansza(Obiekt_Gry):  #tutaj ustalamy tło 

    def __init__(self, obraz, lokacja):
        self.obraz = laduj_obraz(obraz)
        self.pozycja = lokacja



class Tekst(object):
    def __init__(self, napis, kolor):
        self.napis = napis
        self.kolor = kolor
        self.maly_napis = pygame.font.SysFont(None, 25)
        self.sredni_napis = pygame.font.SysFont(None, 50)
        self.duzy_napis = pygame.font.SysFont(None, 100)
        



    
class Statek(Obiekt_Gry): #tworząc statek kosmiczny nadajemy mu pozcję
                          #dodatkowo dodajemy listę pocisków na ekranie
    def __init__(self, pozycja):
        super(Statek, self).__init__(pozycja, laduj_obraz('statek1.png'))

        self.obraz_2 = laduj_obraz('statek2.png')
        self.kierunek = [0, -1]
        self.jest_zaplon = False
        self.angle = 0
        self.obecne_pociski = []

    def narysuj(self, ekran): #rysuje taki statek na ekranie (w zależności od tego czy zapłon jest czy go nie ma)
        if self.jest_zaplon:
            nowy_obraz, rect = obracaj(self.obraz_2, self.obraz_2.get_rect(), self.angle)
        else:
            nowy_obraz, rect = obracaj(self.obraz, self.obraz.get_rect(), self.angle)

        rysuj(nowy_obraz, ekran, self.pozycja)

    def ruch(self):
        self.kierunek[0] = math.sin(-math.radians(self.angle)) #kierunek jest obliczany na podstawie kątów
        self.kierunek[1] = -math.cos(math.radians(self.angle))
        self.pozycja[0] += self.kierunek[0]*self.speed #pozycję określamy przez złożenie kierunku i szybkości               
        self.pozycja[1] += self.kierunek[1]*self.speed

    def strzelanie(self): #określamy startową pozycje pocisku na podstawie kąta przechylenia statku, tak żeby zachować odpowiedni kierunek strzału
        start = [0, 0]
        start[0] = math.sin(-math.radians(self.angle))*self.obraz.get_width()
        start[1] = -math.cos(math.radians(self.angle))*self.obraz.get_height()
        nowy_pocisk = Pocisk((self.pozycja[0] + start[0], self.pozycja[1] + start[1]/2), self.angle)
        self.obecne_pociski.append(nowy_pocisk) #używając obliczonej startowej pozycji tworzymy nowy pocisk


class Pocisk(Obiekt_Gry):
    def __init__(self, pozycja, angle, speed = 15):
        super(Pocisk, self).__init__(pozycja, laduj_obraz('missile.png'))
        self.angle = angle
        self.kierunek = [0, 0]
        self.speed = speed

    def ruch(self):   #podobnie jak w przypadku statku określamy parametry kierunku i pozycji pocisku
        self.kierunek[0] = math.sin(-math.radians(self.angle)) 
        self.kierunek[1] = -math.cos(math.radians(self.angle))
        self.pozycja[0] += self.kierunek[0]*self.speed
        self.pozycja[1] += self.kierunek[1]*self.speed



class Asteroida(Obiekt_Gry):
    def __init__(self, pozycja, rozmiar, speed = 4):
        if rozmiar in {"big", "normal", "small"}:
            str_nazwa = "rock-" + str(rozmiar) + ".png"
            super(Asteroida, self).__init__(pozycja, laduj_obraz(str_nazwa))
            self.rozmiar = rozmiar
        else:  #jeśli rozmiar nie jest określony
            return None

        self.pozycja = list(pozycja)
        self.speed = speed

        if bool(random.getrandbits(1)): #tworzymy losowość poruszania się asteroid
            losuj_x = random.random()* -1
        else:
            losuj_x = random.random()

        if bool(random.getrandbits(1)):
            losuj_y = random.random()* -1
        else:
            losuj_y = random.random()

        self.kierunek = [losuj_x, losuj_y]

    def ruch(self):
        self.pozycja[0] += self.kierunek[0]*self.speed
        self.pozycja[1] += self.kierunek[1]*self.speed



class Gra(object):
    GRANIE, UMIERANIE, KONIEC_GRY, STARTOWANIE, POWITANIE = range(5)

    ODSWIEZ, START, RESTART = range(pygame.USEREVENT, pygame.USEREVENT+3)

    def __init__(self): #uruchamianie nowej rozgrywki
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        self.szerokosc = 1024 #ustawiamy ekran o domyślnej wartości 1024x800
        self.wysokosc = 800
        self.ekran = pygame.display.set_mode((self.szerokosc, self.wysokosc))

        self.dzwiek = laduj_dzwiek('soundtrack.wav') #ładujemy ścieżkę dźwiękową
        self.dzwiek.set_volume(.3)

        self.dzwiek_umierania = laduj_dzwiek('die.wav') #ładujemy pozostawłe dźwięki
        self.dzwiek_koniec_gry = laduj_dzwiek('game_over.wav')
        self.dzwiek_pocisku = laduj_dzwiek('fire.wav')

        
        Napis3 = Tekst("KONIEC GRY", (255, 0, 0))
        self.koniec_gry_napis = Napis3.duzy_napis.render(Napis3.napis, True, Napis3.kolor) #koniec gry będzie czerwony w kodzie RGB

        self.zycia_obraz = laduj_obraz('statek2.png') #pokazuje dostępną ilość żyć

        self.FPS = 30 #ilość klatek na sekundę, a jakiej odświeżamy wyświetlany obraz
        pygame.time.set_timer(self.ODSWIEZ, 1000//self.FPS)

        self.granica_asteroid = {"big":90, "normal":65, "small":40} #ustalamy granicę w jakiej asteroidy będą "atakowały"
        self.powitaj()
        self.czas_strzelania = datetime.datetime.now() #aby nie pozwolić na wystrzelenie w jednym czasie zbyt dużej ilości pocisków
        self.tlo = Plansza('gwiazdy.png', [0, 0]) # za pomocą klasy Plansza generujemy tło
        self.tlo_koniec = Plansza('grzyb.png', [0, 0]) #tutaj generujemy tło w momencie końca gry


    def powitaj(self):
        self.stan = Gra.POWITANIE #przechodzi do stanu powitania

        Napis1 = Tekst("Asteroidy", (255, 200, 0))
        Napis2 = Tekst("Wciśnij[Enter] aby rozpocząć!", (35, 107, 142))

        self.powitanie_asteroidy = Napis1.duzy_napis.render(Napis1.napis, True, Napis1.kolor)
        self.powitanie_panel = Napis2.sredni_napis.render(Napis2.napis, True, Napis2.kolor)

       

    def rozpocznij(self):
        self.asteroidy = [] #tu będziemy trzymać asteroidy

        self.minimalny_dystans = 350 #określamy minimalny dystans w jakim tworzą się nowe asteroidy w odległości od statku
        self.start()

        for i in range(4):
            self.tworz_asteroide()

        self.zycia = 3 #ustawiamy licznik żyć, wyniku punktowego i czasu
        self.wynik = 0
        self.licznik = 0

    def tworz_asteroide(self, rozmiar = "big", x = None):
        min_margines = 200

        if x == None: #żadna pozycja nie została zajęta, tworzymy losową pozycję
            losuj_x = random.randint(min_margines, self.szerokosc-min_margines)
            losuj_y = random.randint(min_margines, self.wysokosc-min_margines)
            while dystans((losuj_x, losuj_y), self.statek.pozycja) < self.minimalny_dystans: #jeśli dystans pomiędzy współrzędnymi a statkiem jest za mały to wygeneruj inny
                losuj_x = random.randint(0, self.szerokosc)
                losuj_y = random.randint(0, self.wysokosc)

            obecna_asteroida = Asteroida((losuj_x, losuj_y), rozmiar)

        else:
            obecna_asteroida = Asteroida(x, rozmiar) #pozycja, którą dostaliśmy dzięki argumenom 

        self.asteroidy.append(obecna_asteroida) #dodajemy nowo stworzoną asteroidę do listy
        
    def start(self): #ustawiamy statek na środku
        self.statek = Statek((self.szerokosc//2, self.wysokosc//2))
        self.pociski = []

        self.dzwiek.play(-1, 0, 1000) #uruchamiamy ścieżkę dźwiękową
        self.stan = Gra.GRANIE

    def uruchom(self):
        x = True
        while x:
            rozgrywka = pygame.event.wait()

            if rozgrywka.type == pygame.QUIT:
                x = False
            elif rozgrywka.type == Gra.ODSWIEZ:
                
                if self.stan != Gra.POWITANIE:
                    klawisz = pygame.key.get_pressed()

                    if klawisz[pygame.K_SPACE]:
                        nowy_czas = datetime.datetime.now()
                        if nowy_czas - self.czas_strzelania > datetime.timedelta(seconds = 0.2): #czas pomiędzy strzałami będzie wynosił 0.2 s
                            self.statek.strzelanie() #oddajemy strzał
                            self.dzwiek_pocisku.play() #dodajemy odpowiedni dźwięk
                            self.czas_strzelania = nowy_czas #zapisujemy obecny czas strzału
                    if self.stan == Gra.GRANIE: #jeśli gra jest uruchomiona

                        if klawisz[pygame.K_RIGHT]:
                            self.statek.angle -= 10  #po naciśnięciu strzałki w prawo obracamy statek o 10 stopni w prawo
                            self.statek.angle %= 360

                        if klawisz[pygame.K_LEFT]: #to samo tylko w lewo
                            self.statek.angle += 10
                            self.statek.angle %= 360

                        if klawisz[pygame.K_UP]: #gdy wciśnięta jest strzałka w lewo to przyspieszamy
                            self.statek.jest_zaplon = True

                            if self.statek.speed < 20:
                                self.statek.speed += 1 #zwiększamy prędkość
                
                        if klawisz[pygame.K_DOWN]: #hamujemy przez wciśnięcie strzałki w dół
                            self.statek.jest_zaplon = False

                            if self.statek.speed > 0:
                                self.statek.speed -= 1
                                
                        if len(self.statek.obecne_pociski) > 0: #jeśli są jakieś pociski to trzeba uruchomić ich poruszanie
                            self.pociski_fizyka()

                        if len(self.asteroidy) > 0: #jeśli są jakieś asteroidy uruchom ich fizykę
                            self.dzwiek_pocisku
                            self.asteroidy_fizyka()

                        self.fizyka() #fizyka statku

                self.wyswietl()    #wyświetl wszystko

            elif rozgrywka.type == Gra.START:
                pygame.time.set_timer(Gra.START, 0) #wyłączamy licznik

                if self.zycia < 1:
                    self.koniec_gry()

                else:
                    self.asteroidy = [] #zaczynamy od nowa
                    for i in range(4):
                        self.tworz_asteroide()
                    self.start()

            elif rozgrywka.type == Gra.RESTART: #rozpoczynamy grę od nowa
                pygame.time.set_timer(Gra.RESTART, 0)
                self.stan = Gra.STARTOWANIE

            elif rozgrywka.type == pygame.MOUSEBUTTONDOWN and (self.stan == Gra.STARTOWANIE or self.stan == Gra.POWITANIE):
                self.rozpocznij()

            elif rozgrywka.type == pygame.KEYDOWN and rozgrywka.key == pygame.K_RETURN and (self.stan == Gra.STARTOWANIE or self.stan == Gra.POWITANIE):
                self.rozpocznij()

            else:
                pass

    def koniec_gry(self):
        self.dzwiek.stop()
        self.stan = Gra.KONIEC_GRY
        self.dzwiek_koniec_gry.play()
        przedluzenie = int((self.dzwiek_koniec_gry.get_length() + 1) * 1000)
        pygame.time.set_timer(Gra.RESTART, przedluzenie)

    def smierc(self):
        self.dzwiek.stop()
        self.zycia -= 1
        self.licznik = 0        
        self.stan = Gra.UMIERANIE
        self.dzwiek_umierania.play()
        przedluzenie = int((self.dzwiek_koniec_gry.get_length() + 1) * 1000)
        pygame.time.set_timer(Gra.START, przedluzenie)

    def fizyka(self):

        if self.stan == Gra.GRANIE:

            self.statek.ruch()

    def pociski_fizyka(self):

        if len(self.statek.obecne_pociski) > 0: #jeśli są jakieś aktywne pociski
            for pocisk in self.statek.obecne_pociski:
                pocisk.ruch() #wprawiamy je w ruch

                for asteroida in self.asteroidy: #warunki na kolizje pocisków z asteroidami
                    if asteroida.rozmiar == "big":
                        if dystans(pocisk.pozycja, asteroida.pozycja) < 80:
                            self.asteroidy.remove(asteroida)
                            if pocisk in self.statek.obecne_pociski:
                                self.statek.obecne_pociski.remove(pocisk)
                            self.tworz_asteroide("normal", (asteroida.pozycja[0] + 10, asteroida.pozycja[1]))
                            self.tworz_asteroide("normal", (asteroida.pozycja[0] - 10, asteroida.pozycja[1]))
                            self.wynik += 20

                    elif asteroida.rozmiar == "normal":
                        if dystans(pocisk.pozycja, asteroida.pozycja) < 55:
                            self.asteroidy.remove(asteroida)
                            if pocisk in self.statek.obecne_pociski:
                                self.statek.obecne_pociski.remove(pocisk)
                            self.tworz_asteroide("small", (asteroida.pozycja[0] + 10, asteroida.pozycja[1]))
                            self.tworz_asteroide("small", (asteroida.pozycja[0] - 10, asteroida.pozycja[1]))
                            self.wynik += 50

                    else:
                        if dystans(pocisk.pozycja, asteroida.pozycja) < 30:
                            self.asteroidy.remove(asteroida)
                            if pocisk in self.statek.obecne_pociski:
                                self.statek.obecne_pociski.remove(pocisk)

                            if len(self.asteroidy) < 10:
                                self.tworz_asteroide()

                            self.wynik += 100

    def asteroidy_fizyka(self):

        if len(self.asteroidy) > 0:
            for asteroida in self.asteroidy:
                asteroida.ruch()
                #jeśli statek uderzy w asteroidę to umiera
                if dystans(asteroida.pozycja, self.statek.pozycja) < self.granica_asteroid[asteroida.rozmiar]:
                    self.smierc()

                elif dystans(asteroida.pozycja, (self.szerokosc/2, self.wysokosc/2)) > math.sqrt((self.szerokosc/2)**2 + (self.wysokosc/2)**2):
                    self.asteroidy.remove(asteroida)

                    if len(self.asteroidy) < 10:
                        self.tworz_asteroide(asteroida.rozmiar)

    def wyswietl(self):
        
        
        self.ekran.fill([255, 255, 255])
        self.ekran.blit(self.tlo.obraz, self.tlo.pozycja)

        if self.stan != Gra.POWITANIE:
            self.statek.narysuj(self.ekran)

            if len(self.statek.obecne_pociski) > 0:
                for pocisk in self.statek.obecne_pociski:
                    pocisk.narysuj(self.ekran)

            if len(self.asteroidy) > 0:
                for asteroida in self.asteroidy:
                    asteroida.narysuj(self.ekran)

            if self.stan == Gra.GRANIE:
                self.licznik += 1

                if self.licznik == 20 * self.FPS: #po 20 s zwiększamy trudność

                    if len(self.asteroidy) < 15: #dodajemy nową asteroidę
                        self.tworz_asteroide()

                    if self.minimalny_dystans < 200: #ogranicz obszar powstawania asteroid
                        self.minimalny_dystans -= 50

                    self.licznik = 0
                    
            Napis4 = Tekst(str(self.wynik), (0, 155, 0))
            pole_wyniku = Napis4.sredni_napis.render(Napis4.napis, True, Napis4.kolor)

            rysuj(pole_wyniku, self.ekran, (self.szerokosc-pole_wyniku.get_width(), pole_wyniku.get_height() + 10))

            if self.stan == Gra.KONIEC_GRY or self.stan == Gra.STARTOWANIE:
                self.ekran.fill([255, 255, 255])
                self.ekran.blit(self.tlo_koniec.obraz, self.tlo_koniec.pozycja)
                rysuj(self.koniec_gry_napis, self.ekran, (self.szerokosc//2, self.wysokosc//2))
            
            for i in range(self.zycia):
                rysuj(self.zycia_obraz, self.ekran, (self.zycia_obraz.get_width() * i * 1.2 + 40, self.zycia_obraz.get_height() //2))

        else:
            rysuj(self.powitanie_asteroidy, self.ekran, (self.szerokosc//2, self.wysokosc//2-self.powitanie_asteroidy.get_height()))

            rysuj(self.powitanie_panel, self.ekran, (self.szerokosc//2, self.wysokosc//2+self.powitanie_panel.get_height()))
                
        pygame.display.flip()

Gra().uruchom()
pygame.quit()
sys.exit()
                    
                    

        
                                                
    

    
        
        
        
        

        
                                     
                                     
        
