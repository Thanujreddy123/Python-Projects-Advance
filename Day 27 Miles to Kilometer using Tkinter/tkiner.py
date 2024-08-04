import tkinter
#this is for the window screen
window=tkinter.Tk()
window.title("my first gui program")
window.minsize(400,600)

#this is for the label
label=tkinter.Label(text="I am a label",font=("Arial",30,"bold"))
label.pack()#this pack is a layout manger to update what you wrote before

#this is like input field you can give input from here
input=tkinter.Entry()
input.pack()
def clickbutton():
    label["text"]=input.get()

#this is a button
button=tkinter.Button(text="new",command=clickbutton)
button.pack()

#this is text input
textinput=tkinter.Text(height=5,width=30)
textinput.focus()
textinput.insert(tkinter.END,"i have to insert some statements")
textinput.pack()


#this is spinbox that is used to the give like coutner
def spinget():
    print(spin.get())
spin=tkinter.Spinbox(from_=0,to=20,width=5,command=spinget)
spin.pack()


#scale

def scaleused(value):
    print(value)

scale=tkinter.Scale(from_=0,to=20,width=5,command=scaleused)
scale.get()
scale.pack()


#check box

checkedstate=tkinter.IntVar()
checkbox=tkinter.Checkbutton(text="is on?",variable=checkedstate)
checkbox.pack()



window.mainloop()

