from turtle import Turtle

STRATING_POSINTION = (0,-280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        
    def go_up(self) -> None:
        x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x, new_y)
    
    def go_to_start(self) -> None:
        self.goto(STRATING_POSINTION)
        
    def is_at_finish_line(self) -> bool:
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False