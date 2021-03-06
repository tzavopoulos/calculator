from tkinter import *

your_mum = Tk()
your_mum.title('Recap')
your_mum.geometry('272x225')
your_mum.resizable(False, False)
your_mum.configure(bg='#FFE4E1')

equation = StringVar()
result = ""

correct = PhotoImage(master=your_mum, file="ssss.png")





def clear():
    global result
    result = ""
    equation.set("")

def press(num):
    global result
    result = result + str(num)
    equation.set(result)

def equal():
    global result
    global result
    global correct
    result = str(eval(result))
    equation.set(result)


    if res_txt.get() == '6969':
        global correct
        your_mum.forget
        your_mum.geometry('460x460')
        lbl = Label(your_mum, image=correct)
        lbl.grid(column=0, row=0)




res_txt = Entry(your_mum,text=equation,width=40)
res_txt.grid(column=0, row=0, columnspan=4)


__9_btn = Button(your_mum, text='9', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(9))
__8_btn = Button(your_mum, text='8', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(8))
__7_btn = Button(your_mum, text='7', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(7))
__6_btn = Button(your_mum, text='6', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(6))
__5_btn = Button(your_mum, text='5', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(5))
__4_btn = Button(your_mum, text='4', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(4))
__3_btn = Button(your_mum, text='3', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(3))
__2_btn = Button(your_mum, text='2', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(2))
__1_btn = Button(your_mum, text='1', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(1))
__0_btn = Button(your_mum, text='0', height=2, width=18, bg='black', foreground='white', font=('Arial 9 bold'),  command =lambda:press(0))

__9_btn.grid(column=2, row=2)
__8_btn.grid(column=1, row=2)
__7_btn.grid(column=0, row=2)
__6_btn.grid(column=2, row=3)
__5_btn.grid(column=1, row=3)
__4_btn.grid(column=0, row=3)
__3_btn.grid(column=2, row=4)
__2_btn.grid(column=1, row=4)
__1_btn.grid(column=0, row=4)
__0_btn.grid(column=0, row=5, columnspan=2)

C_btn = Button(your_mum, text='C', height=2, width=28, bg='#2E2E2E', foreground='white', font=('Arial 9 bold'), command=clear)
C_btn.grid(column=0, row=1, columnspan=3)

multi_btn = Button(your_mum, text='*', height=2, width=8, bg='#2E2E2E', foreground='white', font=('Arial 9 bold'),  command =lambda:press("*"))
div_btn = Button(your_mum, text='/', height=2, width=8, bg='#2E2E2E', foreground='white', font=('Arial 9 bold'),  command =lambda:press("/"))
plus_btn = Button(your_mum, text='+', height=2, width=8, bg='#2E2E2E', foreground='white', font=('Arial 9 bold'),  command =lambda:press("+"))
minus_btn = Button(your_mum, text='-', height=2, width=8, bg='#2E2E2E', foreground='white', font=('Arial 9 bold'),  command =lambda:press('-'))
equals_btn = Button(your_mum, text='=', height=2, width=8, bg='#7B68EE', foreground='white', font=('Arial 9 bold'),  command =equal)

multi_btn.grid(column=3, row=1)
div_btn.grid(column=3, row=2)
plus_btn.grid(column=3, row=3)
minus_btn.grid(column=3, row=4)
equals_btn.grid(column=3, row=5)

dot_btn = Button(your_mum, text='.', height=2, width=8, bg='black', foreground='white', font=('Arial 9 bold'), command = lambda:press("."))

dot_btn.grid(column=2, row=5)


your_mum.mainloop()
