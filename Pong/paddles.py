from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self) -> None:
        x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x, new_y)
        
    def go_down(self) -> None:
        x = self.xcor()
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(x, new_y)