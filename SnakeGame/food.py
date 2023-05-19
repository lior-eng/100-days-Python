from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        x_cor = random.randint(-270, 270)
        y_cor = random.randint(-270, 270)
        self.goto(x_cor, y_cor)