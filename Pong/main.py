from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

RIGHT_STRATING_POSINTION = (350,0)
LEFT_STRATING_POSINTION = (-350,0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(RIGHT_STRATING_POSINTION)
l_paddle = Paddle(LEFT_STRATING_POSINTION)
scoreboard = ScoreBoard()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() < -280:
        ball.y_bounce()
        
    if (ball.distance(r_paddle) < 40 and ball.xcor() > 320) or (ball.distance(l_paddle) < 40 and ball.xcor() < -320):
        ball.x_bounce()
                    
    elif ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            scoreboard.increase_left_score()
        elif ball.xcor() < -380:
            scoreboard.increase_right_score()
        ball.reset_position()  
            
screen.exitonclick()