import turtle
import pandas as pd

sc=turtle.Screen()
sc.title("States program")
image="blank_states_img.gif"
data=pd.read_csv("50_states.csv")
states=list(data["state"])
sc.addshape(image)
turtle.shape(image)

## Keep the window open
resultlist=[]
while len(resultlist)<50:
    s = sc.textinput(title=f"{len(resultlist)}/50 what is the state?", prompt="enter the state").title()
    if s in states:
        resultlist.append(s)
        thanuj=turtle.Turtle()
        thanuj.hideturtle()  # Hide the turtle cursor
        thanuj.penup()  # Lift the pen to move without drawing
        state_data=data[data.state==s]
        thanuj.goto(state_data.x.item(),state_data.y.item())  # Move the turtle to the specified coordinates
        thanuj.write(f"{s}", align="center", font=("Arial", 12, "normal"))
