from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 36, "bold")

class ScoreBoard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_score_board()
        self.hideturtle()
    
    def update_score_board(self) -> None:
        self.clear()
        self.goto(-120,240)
        self.write(f"{self.l_score}", font= FONT, align= ALIGNMENT)
        self.goto(120,240)
        self.write(f"{self.r_score}", font= FONT, align= ALIGNMENT)
        
    def increase_left_score(self) -> None:
        self.l_score += 1
        self.update_score_board()
    
    def increase_right_score(self) -> None:
        self.r_score += 1
        self.update_score_board()