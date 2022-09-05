from tkinter import*
import random
import sys
a=Tk()
a.geometry('880x600')
a.title('Game-3')
WIDTH=600
HEIGHT=600
COLOR1='blue'
COLOR2='red'
COLOR3='#00af0e'
COLOR4='#ffd700'
c = Canvas(a, width=WIDTH, height=HEIGHT, bg='white')
c.focus_set()
c.place(x=0, y=0)
i=0
step=20
score1=0
score2=0
score3=0
score4=0
InGameB=0
InGameR=0
InGameG=0
InGameY=0
Ingame=0
g=0
k=0
LL1=[]
LLB=[]   #массив возможных клеток Данного прямоугольника
LLR=[]
LLG=[]
LLY=[]
LLLB=[[-20, 0]]    #массив клеток Данного цвета 
LLLR=[[-20, 580]]
LLLY=[[600, 0]]    #массив клеток Данного цвета 
LLLG=[[600, 580]] 


L1=Label(a, text=score1, font='Arial 12')
L2=Label(a, text=score2, font='Arial 12')
L3=Label(a, text=score3, font='Arial 12')
L4=Label(a, text=score4, font='Arial 12')
L1.place(x=610, y=30)
L2.place(x=670, y=30)
L3.place(x=730, y=30)
L4.place(x=800, y=30)
    
while i!=WIDTH:
    c.create_line(0, i, WIDTH, i)
    c.create_line(i, 0, i, HEIGHT)
    i=i+step


def StartGame():
    
    global Rect, WidthRect, HeightRect, step, COLOR1, COLOR2, COLOR3, COLOR4, score1, score2, score3, score4, g, LL1, LLLB, LLLR, LLLY, LLLG, k, InGameB, InGameR, InGameG, InGameY, L1, L2, L3, L4 
    WidthRect=random.randrange(0, step*6, step)
    HeightRect=random.randrange(0, step*6, step)
    while WidthRect==0 or HeightRect==0:
        WidthRect=random.randrange(0, step*6, step)
        HeightRect=random.randrange(0, step*6, step)
    
    Rect=c.create_rectangle(0, 0, WidthRect, HeightRect, outline='black', fill=COLOR1)
    
    BLabel=Label(a, text='Blue', fg='blue', font='Arial 12')
    RLabel=Label(a, text='Red', fg='red', font='Arial 12')
    GLabel=Label(a, text='Green', fg='#00af0e', font='Arial 12')
    YLabel=Label(a, text='Yellow', fg='#ffd700', font='Arial 12')
    BLabel.place(x=610, y=10)
    RLabel.place(x=670, y=10)
    GLabel.place(x=730, y=10)
    YLabel.place(x=800, y=10)
    L1.destroy()
    L2.destroy()
    L3.destroy()
    L4.destroy()
    
    L1=Label(a, text=score1, font='Arial 12')
    L2=Label(a, text=score2, font='Arial 12')
    L3=Label(a, text=score3, font='Arial 12')
    L4=Label(a, text=score4, font='Arial 12')
    L1.place(x=610, y=30)
    L2.place(x=670, y=30)
    L3.place(x=730, y=30)
    L4.place(x=800, y=30)
    
    def Pass():
        global Rect, COLOR1, COLOR2, COLOR3, COLOR4, score1, score2, score3, score4
        #print(InGameB, InGameR, InGameG, InGameY)      
        if g==0:
            c.delete(Rect)
            L1.destroy()
            L2.destroy()
            L3.destroy()
            L4.destroy()
            if COLOR1=='blue':
                if InGameB==0:
                    score1=score1-10
            if COLOR1=='red':
                if InGameR==0:
                    score2=score2-10
            if COLOR1=='#00af0e':
                if InGameG==0:
                    score3=score3-10
            if COLOR1=='#ffd700':
                if InGameY==0:
                    score4=score4-10
            COLOR1, COLOR2, COLOR3, COLOR4 = COLOR2, COLOR3, COLOR4, COLOR1
            if InGameB+InGameR+InGameG+InGameY==3:
                #print (111)
                GameOver()
            StartGame()
        
    but=Button(a, text='Pass', font='Arial 10', command=Pass)
    but.place(x=700, y=60)
   
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
        global Rect, HeightRect, WidthRect, COLOR1, COLOR2, COLOR3, COLOR4, score1, score2, score3, score4, LL1, LLLB, LLLR, LLLG, LLLY, k
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
##########

            LLB=[]   #массив возможных клеток Данного прямоугольника
            LLR=[]
            LLG=[]
            LLY=[]
            y2=yPutRect-HeightRect-step
            x2=xPutRect-WidthRect-step
            peremenLLB=0
            peremenLLR=0
            peremenLLG=0
            peremenLLY=0
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
                    if COLOR1=='#00af0e':
                        if l2 not in LLG:
                            LLG.append(l2)
                            peremenLLG=peremenLLG+1
                    if COLOR1=='#ffd700':
                        if l2 not in LLY:
                            LLY.append(l2)
                            peremenLLY=peremenLLY+1
                    x2=x2+step
                y2=y2+step
                x2=xPutRect-WidthRect-step
            # создали массив возможных клеток.
            #print (LLB)   # массив правильный


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

            if COLOR1=='#00af0e':
                if LLG!=0:
                    del LLG[0]
                    u=len(LLG) -1
                    #print(LLG)
                    #print (u)
                    del LLG[u]
                    u=0
                    u=int(WidthRect/step)
                    del LLG[u]
                    u=0
                    u=int(len(LLG)-WidthRect/step)-1
                    del LLG[u]
                    u=0

            if COLOR1=='#ffd700':
                if LLY!=0:
                    del LLY[0]
                    u=len(LLY) -1
                    #print(LLY)
                    #print (u)
                    del LLY[u]
                    u=0
                    u=int(WidthRect/step)
                    del LLY[u]
                    u=0
                    u=int(len(LLY)-WidthRect/step)-1
                    del LLY[u]
                    u=0

            
            if 1==1:
                i=0
                j=0
                LL2=[]
                if COLOR1=='blue':
                    LL2=LLB
                if COLOR1=='red':
                    LL2=LLR
                if COLOR1=='#00af0e':
                    LL2=LLG
                if COLOR1=='#ffd700':
                    LL2=LLY
                while i!=len(LL2):
                    if COLOR1=='blue':
                        if LLB[i] in LLLB:
                            j=j+1
                    if COLOR1=='red':
                        if LLR[i] in LLLR:
                            j=j+1
                    if COLOR1=='#00af0e':
                        if LLG[i] in LLLG:
                            j=j+1
                    if COLOR1=='#ffd700':
                        if LLY[i] in LLLY:
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
                    if COLOR1=='#00af0e':
                        while peremenLLG!=4:
                            LLG.pop()
                            peremenLLG=peremenLLG-1
                    if COLOR1=='#ffd700':
                        while peremenLLY!=4:
                            LLY.pop()
                            peremenLLY=peremenLLY-1
#################
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
                            if COLOR1=='#00af0e':
                                LLLG.append(l1)
                            if COLOR1=='#ffd700':
                                LLLY.append(l1)
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
                                if COLOR1=='#00af0e':
                                    LLLG.pop()
                                if COLOR1=='#ffd700':
                                    LLLY.pop()
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
            
            if o==0:
                ######################################################################################
                
                        
                #######################################################################################
                if j!=0:  #если есть хотя бы одна возможная клетка
                    c.delete(Rect)
                    c.create_rectangle((xPutRect-WidthRect), (yPutRect-HeightRect), xPutRect, yPutRect, outline='black', fill=COLOR1)
                    L1.destroy()
                    L2.destroy()
                    L3.destroy()
                    L4.destroy()
                    if COLOR1=='blue':
                        score1=int(score1+(HeightRect/step)*(WidthRect/step))
                    if COLOR1=='red':
                        score2=int(score2+(HeightRect/step)*(WidthRect/step))
                    if COLOR1=='#00af0e':
                        score3=int(score3+(HeightRect/step)*(WidthRect/step))
                    if COLOR1=='#ffd700':
                        score4=int(score4+(HeightRect/step)*(WidthRect/step))
                    COLOR1, COLOR2, COLOR3, COLOR4 = COLOR2, COLOR3, COLOR4, COLOR1
                    StartGame()
                

    def GameOver():
        global Rect, score1, score2, score3, score4, g, COLOR1, InGameB, InGameR, InGameG, InGameY, Ingame
        c.delete(Rect)
        #print('gameover')
        g=g+1
        if score1>score2 and score1>score3 and score1>score4:
            Mes='Blue win!'
            COLOR1='blue'
        elif score2>score1 and score2>score3 and score2>score4:
            Mes='Red win!'
            COLOR1='red'
        elif score3>score1 and score3>score2 and score3>score4:
            Mes='Green win!'
            COLOR1='#00af0e'
        elif score4>score1 and score4>score2 and score4>score3:
            Mes='Yellow win!'
            COLOR1='#ffd700'
        else:
            Mes='Draw!'
            COLOR1='black'
        LMes=Label(a, text=Mes, fg=COLOR1, font='Arial 12')
        LMes.place(x=684, y=200)
        if g==2:
            a.destroy()
            sys.exit()
       
    butWin=Button(a, text='End Game', font='Arial 10', command=GameOver)
    butWin.place(x=684, y=110)
    #if InGameB+InGameR+InGameG+InGameY==3:
        #Ingame=1
        #GameOver()
    if score1<0:
        InGameB=1
        if COLOR1=='blue':
            Pass()


    if score2<0:
        InGameR=1
        if COLOR1=='red':
            Pass()

            
    if score3<0:
        InGameG=1
        if COLOR1=='#00af0e':
            Pass()

            
    if score4<0:
        InGameY=1
        if COLOR1=='#ffd700':
            Pass()

    if g==0:    
        if InGameB+InGameR+InGameG+InGameY==3:
            GameOver()
    elif k==(WIDTH/step)*(HEIGHT/step):
        GameOver()
    c.bind('<Motion>', MouseMove)
    c.bind('<Button-3>', RightClick)
    c.bind('<1>', PutRect)
    
StartGame()
