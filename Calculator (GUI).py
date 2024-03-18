from tkinter import *
root=Tk()
root.title("Simple Calculator")
root.geometry("482x555+100+200")
root.resizable(False,False)
root.configure(bg="black")

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    label_result.config(text=result)        

label_result=Label(root,width=20,height=2,text="",font=("arial",30))
label_result.pack()

Button(root,text="*",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("*")).place(x=10,y=105)
Button(root,text="/",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("/")).place(x=128,y=105)
Button(root,text="%",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("%")).place(x=245,y=105)
Button(root,text=".",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show(".")).place(x=364,y=105)

Button(root,text="7",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("7")).place(x=10,y=195)
Button(root,text="8",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("8")).place(x=128,y=195)
Button(root,text="9",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("9")).place(x=245,y=195)
Button(root,text="-",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("-")).place(x=364,y=195)

Button(root,text="4",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("4")).place(x=10,y=285)
Button(root,text="5",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("5")).place(x=128,y=285)
Button(root,text="6",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("6")).place(x=245,y=285)
Button(root,text="+",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("+")).place(x=364,y=285)

Button(root,text="1",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("1")).place(x=10,y=375)
Button(root,text="2",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("2")).place(x=128,y=375)
Button(root,text="3",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("3")).place(x=245,y=375)
Button(root,text="C",width=9,height=1,font=("arial 28 bold"),bd=4,fg="black",bg="sky blue",command=lambda:clear()).place(x=128,y=465)

Button(root,text="0",width=4,height=1,font=("arial 28 bold"),bd=1,fg="white",bg="black",command=lambda:show("0")).place(x=10,y=465)
Button(root,text="=",width=4,height=3,font=("arial 28 bold"),bd=6,fg="black",bg="grey",command=lambda:calculate()).place(x=364,y=375)


root.mainloop()
                   
