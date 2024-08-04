import tkinter
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 



# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
reps=0



# ---------------------------- UI SETUP ------------------------------- #

window=tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


label=tkinter.Label(text="Timer",fg=GREEN,bg=YELLOW,font=("Time News Roman",20,"bold"))
label.grid(column=1,row=0)




canvas=tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photo=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo)
timer_text=canvas.create_text(100,125,text="00:00",fill="white",font=("Times New Roman",20,"bold"))
canvas.grid(column=1,row=1)

def reset():
    label.config(text="Timer",fg=GREEN,bg=YELLOW,font=("Time News Roman",20,"bold"))
    canvas.itemconfig(timer_text,text="00:00",fill="white",font=("Times New Roman",20,"bold"))
    rightmarklabel.config(text="")
    window.after_cancel(timer)
def countfun(count):
    global timer
    min=math.floor(count/60)
    seconds=count%60
    canvas.itemconfig(timer_text,text=str(min)+":"+str(seconds))
    if count>0:
        timer=window.after(1000,countfun,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(reps//2):
            mark+="✔"
        rightmarklabel.config(text=mark,fg=GREEN,font=("Time New Roman",20,"bold"))


def breaktime(count):
    min = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=str(min) + ":" + str(seconds))
    if count > 0:
        window.after(1000, countfun, count - 1)

def start_timer():
    global reps
    reps+=1
    if reps==8:
        label.config(text="Long Break",fg=GREEN,bg=YELLOW,font=("Time News Roman",20,"bold"))
        countfun((LONG_BREAK_MIN*60))
    elif reps%2==0:
        label.config(text="Short Break", fg=GREEN, bg=YELLOW, font=("Time News Roman", 20, "bold"))
        countfun((SHORT_BREAK_MIN*60))
    else:
        label.config(text="Work", fg=GREEN, bg=YELLOW, font=("Time News Roman", 20, "bold"))
        countfun((WORK_MIN*60))




buttonstart=tkinter.Button(text="Start",bg=YELLOW,command=start_timer)
buttonreset=tkinter.Button(text="Reset",bg=YELLOW,command=reset)
buttonstart.grid(column=0,row=2)
buttonreset.grid(column=2,row=2)



rightmark=""
rightmarklabel=tkinter.Label(text=rightmark,fg=GREEN,font=("Time New Roman",20,"bold"))
rightmarklabel.grid(column=1,row=3)

window.mainloop()
