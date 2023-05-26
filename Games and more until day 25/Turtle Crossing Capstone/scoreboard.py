from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

class ScoreBoard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-220,260)
        self.update_score_board()
        self.hideturtle()
        
    def update_score_board(self) -> None:
        self.clear()
        self.write(f"Level: {self.level}", font= FONT, align= ALIGNMENT)
    
    def game_over(self) -> None:
        self.goto(0, 0)
        self.write(f"Game Over", font= FONT, align= ALIGNMENT)
        
    def increase_level(self) -> None:
        self.clear()
        self.level += 1
        self.color("black")
        self.update_score_board()