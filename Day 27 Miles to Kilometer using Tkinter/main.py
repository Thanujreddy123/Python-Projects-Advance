import tkinter
import math
window=tkinter.Tk()
window.title("Miles To KM")
window.minsize(300,300)
label=tkinter.Label(text="Enter the Miles")
label.pack()

input=tkinter.Entry()
input.pack()

def convert():
    result=round(int(input.get())*1.6)
    label["text"]=str(input.get())+" miles is equal to"+str(result)

button=tkinter.Button(text="Calculate",command=convert)
button.pack()



window.mainloop()
