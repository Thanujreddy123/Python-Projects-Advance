import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# Setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create player object
player = Player()
car = CarManager()
screen.onkey(player.move, "Up")
Scoreboard = Scoreboard()
# Define key binding

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False

    if player.finish_line():
        player.gotostart()
        Scoreboard.level_up()
        car.level_up()
    if Scoreboard.level > 1:
        Scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
