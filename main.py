from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def check():
    if var.get() == 0:
        messagebox.showinfo('', 'ответ на первый вопрос правильный')
    else:
        messagebox.showinfo('', 'ответ на первый вопрос не правильный')

    if var2.get() == 2:
        messagebox.showinfo('', 'ответ на второй вопрос правильный')
    else:
        messagebox.showinfo('', 'ответ на второй вопрос не правильный')


win = Tk()
win['background'] = 'red'
win.geometry('400x400')

lable = Label(win, text='Какой сейчас год?')
lable.place(x=50, y=50)


lable2 = Label(win, text='Какой год был до этого?')
lable2.place(x=200, y=50)

var = IntVar()
var.set(0)
rbtn1 = Radiobutton(win, text='2021', variable=var, value=1)
rbtn1.place(x=100, y=100)


rbtn2 = Radiobutton(win, text='2022', variable=var, value=2)
rbtn2.place(x=100, y=150)


rbtn3 = Radiobutton(win, text='2023', variable=var, value=0)
rbtn3.place(x=100, y=200)

rbtn4 = Radiobutton(win, text='2024', variable=var, value=3)
rbtn4.place(x=100, y=250)

var2 = IntVar()
rbtn5 = Radiobutton(win, text='2021', variable=var2, value=1)
rbtn5.place(x=200, y=100)


rbtn6 = Radiobutton(win, text='2022', variable=var2, value=2)
rbtn6.place(x=200, y=150)


rbtn7 = Radiobutton(win, text='2023', variable=var2, value=0)
rbtn7.place(x=200, y=200)

rbtn8 = Radiobutton(win, text='2024', variable=var2, value=3)
rbtn8.place(x=200, y=250)

btn1 = Button(win, text='Проверить', command=check)
btn1.place(x=100, y=300)


win.mainloop()