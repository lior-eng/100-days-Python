from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class ScoreBoard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('SnakeGame\data.txt', mode= 'r') as data:
            self.high_score =  int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_score_board()
        self.hideturtle()
        
    def update_score_board(self) -> None:
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", font= FONT, align= ALIGNMENT)
    
    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            with open('SnakeGame\data.txt', mode='w') as data:
                data.write(f" {self.high_score}")
        self.score = 0
        self.update_score_board()

    def increase_score(self) -> None:
        self.score += 1
        self.update_score_board()