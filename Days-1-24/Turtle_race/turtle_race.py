import turtle as t
import random

screen = t.Screen()
screen.setup(height=500, width=500)

is_race_on = False
colors = ["black", "red", "green", "blue", "orange", "purple", "pink"]   
all_turtles = []

for i in range (6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -230, y= -100 + i*50)
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
    
user_bet = screen.textinput(title="Bet", prompt="Which turtle is your Bet?: ")

if user_bet:
    is_race_on = True
    
while is_race_on:
    random_movment = random.randint(0,20)
    random_turtle = all_turtles[random.randint(0,5)]
    random_turtle.forward(random_movment)    
    if random_turtle.xcor() > 230:
        is_race_on = False
        winner_turtle = random_turtle.pencolor()
        if winner_turtle == user_bet:
            print(f"You win! the winner is the {winner_turtle} Turtle")
        else:
            print(f"You lose! the winner Turtle is {winner_turtle}")

screen.exitonclick()