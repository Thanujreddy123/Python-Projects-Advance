import time
from turtle import Turtle,Screen
import random
from Paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

sc=Screen()
sc.bgcolor("black")
sc.setup(800,600)
sc.title("Pong")
sc.tracer(0)

score=Scoreboard();



left_paddle=Paddle((-350,0))
right_paddle=Paddle((350,0))


sc.listen()
sc.onkey(left_paddle.go_up,"w")
sc.onkey(left_paddle.go_down,"s")

sc.onkey(right_paddle.go_up,"Up")
sc.onkey(right_paddle.go_down,"Down")

ball=Ball()


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    sc.update()
    ball.move()

    if ball.xcor()>380:
        score.leftupdate()
        ball.reset()

    if ball.xcor() < -380:
        score.rightupdate()
        ball.reset()




    #detect collison the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()


    #detect collison with right paddle
    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle) <50 and ball.xcor()<-320:
        ball.bound_x()



#tim.goto(-20,0)



sc.exitonclick()