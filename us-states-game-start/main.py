import turtle as t
import pandas as pd

STATES = 50

data = pd.read_csv("./us-states-game-start/50_states.csv")

screen = t.Screen()
screen.title("USA - States - Game")
image = "./us-states-game-start/blank_states_img.gif"
screen.addshape(image)
t.shape(image)

all_states = data.state.to_list()
guessed_states = []
correct_guesses = 0

gameison = True
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_guesses}/{STATES} Guess the state", prompt="what's another state's name? ").title()
    
    if answer_state == "Exit":
        break
    
    if answer_state in all_states:
        all_states.remove(answer_state)
        new_state = t.Turtle()
        new_state.hideturtle()
        new_state.penup()
        state_data = data[data.state == answer_state]
        new_state.goto(int(state_data.x),int(state_data.y))
        new_state.write(answer_state)
        correct_guesses += 1
        
guessed_states_dataframe = pd.DataFrame(all_states)
guessed_states_dataframe_csv = guessed_states_dataframe.to_csv("./us-states-game-start/states_to_learn.csv")