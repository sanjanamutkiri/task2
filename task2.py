from tkinter import *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Syntax Error"
        scvalue.set(value)
        screen.update()
    elif text=="AC":
        scvalue.set("")
        screen.update()
    elif text=="x":
        scvalue.remove()
        screen.update()
    
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
root=Tk()
root.geometry("500x500")
root['background']="yellow"
root.title("CALCULATOR")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="arial 20 bold")
screen.pack(fill=X,ipadx=20,pady=20,padx=20)

f=Frame(root,bg="grey")
b=Button(f,text="/",padx=12,pady=12,font="arial 11 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="+",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=12,pady=11,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="7",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="9",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text=".",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="4",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="6",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="x",padx=9,pady=9,font="arial 11 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="1",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="2",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="3",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text=" ",padx=10,pady=10,font="arial 12 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="AC",padx=10,pady=10,font="arial 10 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="0",padx=10,pady=10,font="arial 10 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="%",padx=10,pady=10,font="arial 10 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=10,pady=10,font="arial 10 bold")
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()

        