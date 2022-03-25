import pygame
from pygame.locals import *
import time
from collections import deque
import random
import string
pygame.init()
bild = pygame.display.set_mode((500, 600))
bild.fill((255,255,255))
pygame.display.set_caption("Snake!")
pygame.display.update()  
run=False
lange=3
richtung=1
farbe1=(31,31,208)
farbe2=(0,0,0)
mode=1
x=1
y=1
zeit=0
fehler=0
snakex=deque([1])
snakey=deque([1])
apfely=[random.randint(1,48),random.randint(1,48),random.randint(1,48)]
apfelx=[random.randint(1,48),random.randint(1,48),random.randint(1,48)]
img= pygame.Surface((10, 10))
Aufgaben=[]
worter=[]
fortschritt=0
aufgabe=0
def new_letters(l):
    global worter_mix
    str=''
    for n in string.ascii_lowercase:
        if l!=n:
            str=str+n
    worter_mix=[random.choice(str),random.choice(str),worter[aufgabe][fortschritt]]
def pixel(x,y):  
    try:
        img.fill((127,255,0))
        bild.blit(img,(x*10,y*10))
    except:
        pass
def apfel(x,y,i):
    font_big = pygame.font.Font(None, 30)
    lett=font_big.render(worter_mix[i], True, farbe1)
    pix=lett.get_rect(center=(x*10+2,y*10-2))
    try:
        bild.blit(lett,pix)
    except:
        pass
def new():
    global apfely
    global apfelx
    global lange
    global fortschritt
    global worter_mix
    global aufgabe
    fortschritt=fortschritt+1
    try:
        new_letters(worter[aufgabe][fortschritt])
    except:
        aufgabe=aufgabe+1
        fortschritt=0
    new_letters(worter[aufgabe][fortschritt])
    for v in range(3):
        apfely[v]=random.randint(1,48)
        apfelx[v]=random.randint(1,48)
    lange=lange+1
def text_display(txt, pos):
    font_big = pygame.font.Font(None, 40)
    text=font_big.render(txt, True, (31,31,208))
    rechteck=text.get_rect(center=(pos))
    bild.blit(text, rechteck)
def start():
    global snakex
    global snakey
    global run
    global x
    global y
    global richtung
    global lange
    global mode
    global worter
    global Aufgaben
    global fortschritt
    global aufgabe
    global fehler
    richtung=1
    x=1
    y=1
    for i in range(len(snakex)):
        snakex.pop()
        snakey.pop()
    while not run:
        bild.fill((0,0,0))
        text_display("Letzter Score: "+str(lange-3), (250, 50))
        text_display("Suche die passenden Verben",(250,100))
        text_display("Suche die passenden Adjektive",(250,150))
        text_display("Suche die passenden Nomen",(250,200))
        text_display("Start",(250,400))
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_m=pygame.mouse.get_pos() [0]
                y_m=pygame.mouse.get_pos() [1]
                if x_m>200 and x_m<300 and y_m>390 and y_m<420:
                    run=True
                if x_m>100 and x_m<400 and y_m>90 and y_m<120:
                    mode=1
                if x_m>100 and x_m<400 and y_m>140 and y_m<170:
                    mode=2
                if x_m>100 and x_m<400 and y_m>190 and y_m<220:
                    mode=3
        if mode==1:
            pixel(1,10)
        if mode==2:
            pixel(1,15)
        if mode==3:
            pixel(1,20)
        pygame.display.update()
    lange=3
    if mode==3:
        worter=['ager','caput','corpus','domus','femina','filia','frater','homo','labor','magister',]
        Aufgaben=['Acker/Feld','Kopf','Koerper','Haus','Frau','Tochter','Bruder','Mensch','Arbeit','Lehrer']
    if mode==2:
        worter=['bonus','celer','certus','clarus','dignus','fortis','gravis','liber','malus','novis']
        Aufgaben=['gut','schnell','sicher','hell','wuerdig','mutig','schwer','frei','schlecht','neu']
    if mode==1:
        worter=['necare','capere','esse','accedere','agere','dare','defendere','facere','ostendere','reliquere','scribere']
        Aufgaben=['toeten','erobern','sein','hingehen','tun/betreiben','geben','verteidigen','tun','zeigen','verlassen','schreiben']
    aufgabe=0
    fortschritt=0
    fehler=0
    new_letters(worter[aufgabe][fortschritt])

start()


while run:
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP and not richtung==2:
                richtung=0
            if event.key == pygame.K_DOWN and not richtung==0:
                richtung=2
            if event.key == pygame.K_RIGHT and not richtung==3:
                richtung=1
            if event.key == pygame.K_LEFT and not richtung==1:
                richtung=3
        if event.type == pygame.QUIT:
            run= False
    if y==50:
        y=0
    elif y==-1:
        y=49
    if x==50:
        x=0
    elif x==-1:
        x=49
    if not int(time.time()*10)==zeit:
        bild.fill((255,255,255))
        if richtung==0:
                y=y-1
        if richtung==1:
                x=x+1
        if richtung==2:
                y=y+1
        if richtung==3:
                x=x-1
        for i in range(3):
            if x==apfelx[i] and y==apfely[i] or x==apfelx[i] and y==apfely[i]-1 or x==apfelx[i]-1 and y==apfely[i]:
                if i==2:
                    new()
                    lange=lange+1
                else:
                    fehler=fehler+1
        snakex.append(x)
        snakey.append(y)
        if lange<len(snakex):
            snakex.popleft()
            snakey.popleft()       
        zeit=int(time.time()*10)
    for i in range(3):
        apfel(apfelx[i],apfely[i],i)
    for i in range(len(snakex)):
        pixel(snakex[i],snakey[i])
    for i in range(len(snakex)):
        try:
            if snakex[len(snakex)-1]==snakex[i] and snakey[len(snakex)-1]==snakey[i] and not i==len(snakex)-1 :
                run=False
                start()
        except:
            pass
    font_big = pygame.font.Font(None, 30)
    Fehler_t=font_big.render("Fehler: "+str(fehler), True, farbe2)
    Aufgabe_t=font_big.render(str(aufgabe+1)+". Aufgabe: Ueberstze "+Aufgaben[aufgabe], True, farbe2)
    if fortschritt==0 and aufgabe>0:
        text=font_big.render(worter[aufgabe-1], True, farbe2)
        bild.blit(text,(200,520))
    else:
        for c in range(fortschritt):
            text=font_big.render(worter[aufgabe][c], True, farbe2)
            bild.blit(text,(200+c*12,520))
    pygame.draw.rect(bild,farbe2,(0,510, 498,88),4)
    
    bild.blit(Fehler_t, (20,520))
    bild.blit(Aufgabe_t, (20,550))
    pygame.display.update()
    bild.fill((255,255,255))