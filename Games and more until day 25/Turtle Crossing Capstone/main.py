from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car_maneger import CarManeger
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Capstone")
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()
car_maneger = CarManeger()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    
    car_maneger.create_car()
    car_maneger.cars_move()
    
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_maneger.increament_speed()
  
    for car in car_maneger.cars:
        # if player.distance(car) < 20:
        if (player.xcor() - 10 < car.xcor() + 20 and
            player.xcor() + 10 > car.xcor() - 10 and
            player.ycor() - 10 < car.ycor() + 20 and
            player.ycor() + 10 > car.ycor() - 10):
            game_is_on = False
            scoreboard.game_over()
            
screen.exitonclick()