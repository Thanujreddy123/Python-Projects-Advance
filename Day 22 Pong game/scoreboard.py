from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.goto(-100,200)
        self.write(self.lscore,align="center",font=("courier",80,"normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("courier", 80, "normal"))

    def leftupdate(self):
        self.clear()
        self.lscore = self.lscore + 1
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("courier", 80, "normal"))

    def rightupdate(self):
        self.clear()
        self.rscore = self.rscore + 1
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("courier", 80, "normal"))

    def increase_score(self):
        self.clear()
        self.rscore=self.rscore+1
        self.write(self.rscore, align="center", font=("courier", 80, "normal"))
