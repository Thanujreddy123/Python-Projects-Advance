import string
import random
import tkinter
from tkinter import *

window=Tk()
window.title("password generator")
window.config(padx=20,pady=20)
window.minsize(400,400)
label=Label(text="password Generattor",fg="green",bg="yellow",font={"Arial",20,"bold"})
label.grid(column=0,row=0)

canvas=Canvas(width=200,height=200)
image=PhotoImage(file="lockpasswordimage.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=0,row=1)

emaillabel=Label(text="Email",fg="black")
emaillabel.grid(column=0,row=2)

emailinput=Entry()
emailinput.grid(column=1,row=2)

entryvar=StringVar()
entryvar.set("")

passwordlabel=Label(text="Password",fg="black")
passwordlabel.grid(column=0,row=3)

passwordinput=Entry(textvariable=entryvar)
passwordinput.grid(column=1,row=3)

def printout():
    print(emailinput.get(),passwordinput.get())
    with open("output.txt","w") as t:
        t.write(f"email:{emailinput.get()},password:{passwordinput.get()}")

def checkfields():
    if not emailinput.get():
        print("enter the fields please first")
    else:
        generate()

def generate(length=12):
    characters=string.ascii_letters+string.digits+string.punctuation;
    pasword=''.join(random.choice(characters) for _ in range(length))
    entryvar.set(pasword)


button=Button(text="Generate Password",command=checkfields)
button.grid(column=2,row=3)


submit=Button(text="submit",command=printout)
submit.grid(columns=1,row=4)

window.mainloop()