from flask import Flask
import random

random_number = random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def game_title() -> None:
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src = 'https://media.giphy.com/media/XTryHBP13zwz0GeKWZ/giphy.gif'/>"

@app.route("/<int:number>")
def guess_number(number: int) -> None:
    
    if number > random_number:
        return "<h1 style= color:red>Too High, Try Again</h1>" \
                "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
                
    elif number < random_number:
        return "<h1 style= color:blue>Too Low, Try Again</h1>" \
                "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
                
    else:
        return "<h1 style= color:green>Bingo!</h1>" \
                "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == '__main__':
    app.run(debug= True)