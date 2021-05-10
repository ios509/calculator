
from tkinter import *

win = Tk()
win.geometry('350x400+250+200')
win.title('Nasser')


num = StringVar()
ope = ''


def cleck_butt(number):
    global ope
    ope += (str(number))
    num.set(ope)
def re():
    global ope
    res = str(eval(ope))
    num.set(res)
    ope = res
def clear():
    global ope
    ope = ''
    num.set('')

text = Entry(win,width=25,font=('Time', 16,'bold'),textvariable=num).place(x=30 ,y=50)

b7 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(7),font=('Times',12,'bold'),text='7',bd=4,bg='#CEECF5',fg='black').place(x=30,y=105)
b8 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(8),font=('Times',12,'bold'),text='8',bd=4,bg='#CEECF5',fg='black').place(x=110,y=105)
b9 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(9),font=('Times',12,'bold'),text='9',bd=4,bg='#CEECF5',fg='black').place(x=190,y=105)

b4 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(4),font=('Times',12,'bold'),text='4',bd=4,bg='#CEECF5',fg='black').place(x=30,y=170)
b5 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(5),font=('Times',12,'bold'),text='5',bd=4,bg='#CEECF5',fg='black').place(x=110,y=170)
b6 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(6),font=('Times',12,'bold'),text='6',bd=4,bg='#CEECF5',fg='black').place(x=190,y=170)

b1 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(1),font=('Times',12,'bold'),text='1',bd=4,bg='#CEECF5',fg='black').place(x=30,y=235)
b2 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(2),font=('Times',12,'bold'),text='2',bd=4,bg='#CEECF5',fg='black').place(x=110,y=235)
b3 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(3),font=('Times',12,'bold'),text='3',bd=4,bg='#CEECF5',fg='black').place(x=190,y=235)

b0 = Button(win,padx=10,pady=2,width=4,height=2,command=lambda :cleck_butt(0),font=('Times',12,'bold'),text='0',bd=4,bg='#CEECF5',fg='black').place(x=110,y=300)

z = Button(win,padx=4,pady=2,font=('Times',10,'bold'),command=lambda :cleck_butt('+'),width=2,bd=2,bg='orange',text='+').place(x=270,y=105)
d = Button(win,padx=4,pady=2,font=('Times',10,'bold'),command=lambda :cleck_butt('-'),width=2,bd=2,bg='orange',text='-').place(x=270,y=140)
q = Button(win,padx=4,pady=2,font=('Times',10,'bold'),command=lambda :cleck_butt('/'),width=2,bd=2,bg='orange',text='/').place(x=270,y=175)
t = Button(win,padx=4,pady=2,font=('Times',10,'bold'),command=lambda :cleck_butt('*'),width=2,bd=2,bg='orange',text='x').place(x=270,y=210)

eq = Button(win,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='C',bd=4,bg='orange',fg='black',command=clear).place(x=30,y=300)
b0 = Button(win,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='=',bd=4,bg='orange',fg='black',command=re).place(x=190,y=300)

win.mainloop()