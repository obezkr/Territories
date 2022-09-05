from tkinter import*
import sys
a=Tk()
a.geometry('500x300')
a.title('Game-3')
WIDTH=400
HEIGHT=400

def FourP():
    import Game3For4
    a.destroy()
    sys.exit()
    
def TwoP():
    import Game3For2
    a.destroy()
    sys.exit()
    
L=Label(a, text='Choose number of players:', font='Arial 16')
L.place(x=125, y=10)
b=Button(a, text='4 Players', font='Arial 12', command=FourP)
b.place(x=100, y=70)
d=Button(a, text='2 Players', font='Arial 12', command=TwoP)
d.place(x=300, y=70)

