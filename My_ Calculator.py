from tkinter import *
import tkinter.messagebox
from tkinter import messagebox

# CREATING GUI WINDOW
root = Tk()
root.title("My calculator")
root.iconbitmap('favicon.ico')

entfield=Entry(root, width = 45, borderwidth = 5, )
entfield.grid(row=0, column = 0, columnspan=4, padx=10, pady = 10)
entfield.insert(0,'Clear and Start your calculation')

# DEFINING FUNCTIONS

def button_click(number):
    #entfield.delete(0,END)
    current=entfield.get()
    entfield.delete(0, END)
    entfield.insert(0, str(current)+str(number))

def clear():
    entfield.delete(0, END)

def empty():
    num1 = entfield.get()
    global f_num
    global math
    math = 'none'
    f_num = num1
    entfield.delete(0, END)

def plus():
    num1=entfield.get()
    global f_num
    global math
    math = 'addition'
    f_num = num1
    entfield.delete(0,END)

def minus():
    num1 = entfield.get()
    global f_num
    global math
    math = 'minus'
    f_num = num1
    entfield.delete(0, END)

def multiply():
    num1 = entfield.get()
    global f_num
    global math
    math = 'multiply'
    f_num = num1
    entfield.delete(0, END)

def devide():
    num1 = entfield.get()
    global f_num
    global math
    math = 'devide'
    f_num = num1
    entfield.delete(0, END)

def sqrt():
    num1 = entfield.get()
    global f_num
    global math
    math = 'sqrt'
    f_num = num1
    entfield.delete(0, END)

def percent():
    num1 = entfield.get()
    global f_num
    global math
    math = 'percent'
    f_num = num1
    entfield.delete(0, END)

def equal():
    sec_num = entfield.get()
    entfield.delete(0, END)
    if math == 'none':
        try:
            raise NameError('HiThere')
        except NameError:
            tkinter.messagebox.showwarning('Wrong data', 'Required fields are not completed')
            print('An exception flew by!')
            entfield.delete(0, END)
            raise
    elif math == 'addition':
        float_num=float(f_num)
        entfield.insert(0, float_num + float(sec_num))
    elif math == 'minus':
        float_num=float(f_num)
        entfield.insert(0, float_num - float(sec_num))
    elif math == 'multiply':
        float_num=float(f_num)
        entfield.insert(0, float_num * float(sec_num))
    elif math == 'devide':
        float_num=float(f_num)
        entfield.insert(0, float_num / float(sec_num))
    elif math == 'sqrt':
        float_num=float(f_num)
        entfield.insert(0, float_num ** float(sec_num))
    elif math == 'percent':
        float_num=float(f_num)
        entfield.insert(0, (float_num/100) * float(sec_num))

def exit():
    response = messagebox.askyesno('Exit the Calculator', ' You really want to leave?')
    if response == 1:
        root.destroy()
    else:
        clear()


# CREATING BUTTONS
button_1 = Button(root, text="1", padx=40, pady=20, command = lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command = lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command = lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command = lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command = lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command = lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command = lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command = lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command = lambda: button_click(9))

button_clear = Button(root, text="CLEAR", padx=25.5, pady=20, command = clear)
button_equal = Button(root, text="=", padx=40, pady=20, command = equal)
button_0 = Button(root, text="0", padx=40, pady=20, command = lambda: button_click(0))
button_decimels = Button(root, text=".", padx=41.4, pady=20, command = lambda: button_click('.'))

button_plus = Button(root, text="+", padx=40, pady=20, command = plus)
button_minus = Button(root, text="-", padx=40, pady=20, command = minus)
button_multiply = Button(root, text="*", padx=40, pady=20, command = multiply)
button_devide = Button(root, text="/", padx=40, pady=20, command = devide)
button_quit = Button(root, text = 'QUIT', padx=29, pady=20, command = exit)
button_sqrt = Button (root, text='sqrt', padx=33, pady=20, command = sqrt)
button_percent = Button(root, text='%', padx = 38 , pady = 20 , command = percent)



# ADDING BUTTONS ON THE GUI SCREEN
button_plus.grid(row = 4, column= 3)
button_minus.grid(row = 3, column= 3)
button_multiply.grid(row = 2, column= 3)
button_devide.grid(row = 1, column= 3)
button_quit.grid(row = 1, column= 0)
button_sqrt.grid(row=1, column=1)
button_percent.grid(row=1, column=2)

button_7.grid(row = 2, column= 0)
button_8.grid(row = 2, column= 1)
button_9.grid(row = 2, column= 2)

button_4.grid(row = 3, column= 0)
button_5.grid(row = 3, column= 1)
button_6.grid(row = 3, column= 2)

button_1.grid(row = 4, column= 0)
button_2.grid(row = 4, column= 1)
button_3.grid(row = 4, column= 2)

button_0.grid(row = 5, column= 0)
button_decimels.grid(row = 5, column= 1, columnspan=1)
button_clear.grid(row = 5, column= 2, columnspan = 1)
button_equal.grid(row = 5, column= 3, columnspan = 3)



root.mainloop()