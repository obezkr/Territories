from tkinter import*
import random
import sys
a=Tk()
a.geometry('800x600')
a.title('Game-3')
WIDTH=600
HEIGHT=600
COLOR1='blue'
COLOR2='red'
c = Canvas(a, width=WIDTH, height=HEIGHT, bg='white')
c.focus_set()
c.place(x=0, y=0)
i=0
step=20
GameWin1=0
GameWin2=0
score1=0
score2=0
g=0
k=0
LL1=[]

LLB=[]   #массив возможных клеток Данного прямоугольника
LLR=[]

LLLB=[[-20, 0]]    #массив клеток Данного цвета 
LLLR=[[600, 580]]  

while i!=WIDTH:
    c.create_line(0, i, WIDTH, i)
    c.create_line(i, 0, i, HEIGHT)
    i=i+step


def StartGame():
    
    global Rect, WidthRect, HeightRect, step, COLOR1, COLOR2, score1, score2, g, LL1, LLLB, LLLR, k
    WidthRect=random.randrange(0, step*6, step)
    HeightRect=random.randrange(0, step*6, step)
    while WidthRect==0 or HeightRect==0:
        WidthRect=random.randrange(0, step*6, step)
        HeightRect=random.randrange(0, step*6, step)
    
    Rect=c.create_rectangle(0, 0, WidthRect, HeightRect, outline='black', fill=COLOR1)
    
    
    BLabel=Label(a, text='Blue', fg='blue', font='Arial 12')
    RLabel=Label(a, text='Red', fg='red', font='Arial 12')
    BLabel.place(x=620, y=10)
    RLabel.place(x=730, y=10)
    L1=Label(a, text=score1, font='Arial 12')
    L2=Label(a, text=score2, font='Arial 12')
    L1.place(x=620, y=30)
    L2.place(x=730, y=30)
    
    def Pass():
        global Rect, COLOR1, COLOR2, score1, score2
        if g==0:
            c.delete(Rect)
            L1.destroy()
            L2.destroy()
            if COLOR1=='blue':
                score1=score1-10
            else:
                score2=score2-10
            COLOR1, COLOR2 = COLOR2, COLOR1
            StartGame()
        
    but=Button(a, text='Pass', font='Arial 10', command=Pass)
    but.place(x=670, y=10)
   
    def MouseMove(event):
        global Rect, g
        if g==0:
            x=event.x
            y=event.y
            xR=c.coords(Rect)[2]
            yR=c.coords(Rect)[3]
            c.move(Rect, (x-xR), (y-yR))
    
    def RightClick(event):
        global Rect, HeightRect, WidthRect
        if g==0:
            c.delete(Rect)
            x=event.x
            y=event.y
            HeightRect, WidthRect = WidthRect, HeightRect
            Rect=c.create_rectangle(x-WidthRect, y-HeightRect, x, y, outline='black', fill=COLOR1)
    
    def PutRect(event):
        global Rect, HeightRect, WidthRect, COLOR1, COLOR2, score1, score2, LL1, LLLB, LLLR, k
        if g==0: 
            x=event.x
            y=event.y
            xPutRect=0
            yPutRect=0
            e=0
            while e<x:
                e=e+step
                if (e-x)<(step/2):
                    xPutRect=e
                else:
                    xPutRuct=(e-step)
            
            e=0
            while e<y:
                e=e+step
                if (e-y)<(step/2):
                    yPutRect=e
                else:
                    yPutRuct=(e-step)
            #<check>
            y1=yPutRect-HeightRect
            x1=xPutRect-WidthRect
            o=0
            m=0
            # проверка на вылезание из поля
            if xPutRect<=WIDTH and xPutRect-WidthRect>=0 and yPutRect<=HEIGHT and yPutRect-HeightRect>=0:
                o=0
                y1=yPutRect-HeightRect
                x1=xPutRect-WidthRect
            else:
                o=1
                y1=yPutRect
                x1=xPutRect


            LLB=[]   #массив возможных клеток Данного прямоугольника
            LLR=[]
            y2=yPutRect-HeightRect-step
            x2=xPutRect-WidthRect-step
            peremenLLB=0
            peremenLLR=0
            while y2<yPutRect+step:
                while x2<xPutRect+step:
                    l2=[x2, y2]                     ### ошибка в удалении ненужных елементов массива, и, возможно, проверке ###
                    if COLOR1=='blue':
                        if l2 not in LLB:
                            LLB.append(l2)
                            peremenLLB=peremenLLB+1
                            
                    if COLOR1=='red':
                        if l2 not in LLR:
                            LLR.append(l2)
                            peremenLLR=peremenLLR+1
                    x2=x2+step
                y2=y2+step
                x2=xPutRect-WidthRect-step
            # создали массив возможных клеток.
            #print (LLB)   # массив правильный
            
###########
            
            if COLOR1=='blue':
                if LLB!=0:
                    del LLB[0]
                    u=len(LLB) -1
                    #print(LLB)
                    #print (u)
                    del LLB[u]
                    u=0
                    u=int(WidthRect/step)
                    del LLB[u]
                    u=0
                    u=int(len(LLB)-WidthRect/step)-1
                    del LLB[u]
                    u=0
                    
            if COLOR1=='red':
                if LLR!=0:
                    del LLR[0]
                    u=len(LLR) -1
                    #print(LLR)
                    #print (u)
                    del LLR[u]
                    u=0
                    u=int(WidthRect/step)
                    del LLR[u]
                    u=0
                    u=int(len(LLR)-WidthRect/step)-1
                    del LLR[u]
                    u=0
                    
###########            
            if 1==1:
                i=0
                j=0
                LL2=[]
                if COLOR1=='blue':
                    LL2=LLB
                if COLOR1=='red':
                    LL2=LLR
                while i!=len(LL2):
                    if COLOR1=='blue':
                        if LLB[i] in LLLB:
                            j=j+1
                    if COLOR1=='red':
                        if LLR[i] in LLLR:
                            j=j+1
                    i=i+1
                if j==0:
                    if COLOR1=='blue':
                        while peremenLLB!=4:
                            LLB.pop()
                            peremenLLB=peremenLLB-1
                    if COLOR1=='red':
                        while peremenLLR!=4:
                            LLR.pop()
                            peremenLLR=peremenLLR-1

            if j!=0:
                while y1<yPutRect:
                    while x1<xPutRect:
                        l1=[x1, y1]
                        if l1 not in LL1:
                            LL1.append(l1)
                            if COLOR1=='blue':
                                LLLB.append(l1) #LLLB - массив занятых синих клеток
                            if COLOR1=='red':
                                LLLR.append(l1)
                            k=k+1
                            m=m+1
                        else:
                            o=o+1
                            while m!=0:
                                LL1.pop()
                                if COLOR1=='blue':
                                    LLLB.pop()
                                if COLOR1=='red':
                                    LLLR.pop()
                                m=m-1
                                k=k-1
                            x1=xPutRect
                            y1=yPutRect
                        x1=x1+step
                    y1=y1+step
                    x1=xPutRect-WidthRect
                #print(LLLB)  # массив правильный
            #</check>
            # проверка на соединие с соседними клетками - создаем массив возможных клеток вокруг прямоугольника, если в таком массиве будут координаты, значит можно.
            
            if o==0: #если не налезает
                if j!=0:  #если есть хотя бы одна возможная клетка
                    c.delete(Rect)
                    c.create_rectangle((xPutRect-WidthRect), (yPutRect-HeightRect), xPutRect, yPutRect, outline='black', fill=COLOR1)
                    L1.destroy()
                    L2.destroy()
                    if COLOR1=='blue':
                        score1=int(score1+(HeightRect/step)*(WidthRect/step))
                    else:
                        score2=int(score2+(HeightRect/step)*(WidthRect/step))
                    COLOR1, COLOR2 = COLOR2, COLOR1
                    StartGame()
                

    def GameOver():
        global Rect, score1, score2, g, COLOR1
        c.delete(Rect)
        g=g+1
        if score1>score2:
            Mes='Blue win!'
            COLOR1='blue'
        elif score1<score2:
            Mes='Red win!'
            COLOR1='red'
        else:
            Mes='Draw!'
            COLOR1='black'
        L3=Label(a, text=Mes, fg=COLOR1, font='Arial 12')
        L3.place(x=670, y=200)
        if g==2:
            a.destroy()
            sys.exit()
       
    butWin=Button(a, text='End Game', font='Arial 10', command=GameOver)
    butWin.place(x=660, y=70)
    if score1<0:
        GameOver()
    elif score2<0:
        GameOver()
    elif k==(WIDTH/step)*(HEIGHT/step):
        GameOver()
        
    c.bind('<Motion>', MouseMove)
    c.bind('<Button-3>', RightClick)
    c.bind('<1>', PutRect)
    
StartGame()
