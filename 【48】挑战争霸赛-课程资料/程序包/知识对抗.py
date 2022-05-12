from tkinter import *
from tkinter.ttk import *
from PIL import Image
import random

def change():
    f1.destroy()
    get_question()

def get_question():
    global f2
    if f2:
        f2.destroy()
    f2 = Canvas(w,width=963,height=750)
    f2.create_image(500,400,image=im1)
    f2.pack()
    temp = random.choice(ques)[:-1].split(' ')
    t1 = Label(f2, text=temp[0], font=('微软雅黑', 20))
    t1.configure(background='white')
    t2 = Label(f2, text='A. '+temp[1], font=('微软雅黑', 20))
    t3 = Label(f2,text='B. '+temp[2],font=('微软雅黑',20))
    t4 = Label(f2,text='C. '+temp[3],font=('微软雅黑',20))
    t5 = Label(f2,text='D. '+temp[4],font=('微软雅黑',20))
    b2 = Button(f2, text='下一题', command=get_question)
    t2.configure(background='white')
    t3.configure(background='white')
    t4.configure(background='white')
    t5.configure(background='white')
    t1.pack()
    t2.pack()
    t3.pack()
    t4.pack()
    t5.pack()
    b2.pack()
    f2.create_window(400,100,window=t1)
    f2.create_window(300, 200, window=t2)
    f2.create_window(500, 200, window=t3)
    f2.create_window(300, 300, window=t4)
    f2.create_window(500, 300, window=t5)
    f2.create_window(350, 400, window=b2)


with open('question.txt', 'r', encoding='utf-8') as f:
    ques = f.readlines()
w = Tk()
w.title('题目')
img = PhotoImage(file='1.gif')
im1 = PhotoImage(file='2.gif')
f1 = Canvas(w, width=512, height=250)
f1.create_image(250, 100, image=img)
f1.pack()
f2 = None
# q1 = Label(f1,image=img)
b1 = Button(f1, text='开始', command=change)
# q1.grid(row=0, column=2)
b1.pack()
f1.create_window(250,200,window=b1)
mainloop()

