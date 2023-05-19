from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "bold")

class ScoreBoard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score_board()
        self.hideturtle()
        
    def update_score_board(self) -> None:
        self.write(f"Score: {self.score}", font= FONT, align= ALIGNMENT)
    
    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(f"Game Over", font= FONT, align= ALIGNMENT)
        
    def increase_score(self) -> None:
        self.clear()
        self.score += 1
        self.color("white")
        self.update_score_board()