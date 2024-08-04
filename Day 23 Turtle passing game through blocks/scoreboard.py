FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-250,270)
        self.write(f"Level {self.level}", align="center", font="FONT")

    def level_up(self):
        self.clear()
        self.level+=1
        self.write(f"Level {self.level}", align="center", font="FONT")
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font="FONT")