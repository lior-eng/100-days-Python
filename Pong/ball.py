from turtle import Turtle

BALL_MOVEMENT = 10

class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        
    def move(self) -> None:
        new_x = self.xcor() + BALL_MOVEMENT
        new_y = self.ycor() + BALL_MOVEMENT
        self.goto(new_x, new_y)
        
    # def change_direction(self) -> None:
    #     if self.xcor() >= 0 and self.ycor() == 280:
    #         self.move()