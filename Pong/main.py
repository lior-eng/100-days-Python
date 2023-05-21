from turtle import Screen
from paddles import Paddle
from ball import Ball
import time

RIGHT_STRATING_POSINTIONS = (350,0)
LEFT_STRATING_POSINTIONS = (-350,0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(RIGHT_STRATING_POSINTIONS)
l_paddle = Paddle(LEFT_STRATING_POSINTIONS)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    ball.move()


screen.exitonclick()