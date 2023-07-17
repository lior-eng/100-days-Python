from flask import Flask
from typing import Callable

app = Flask(__name__)

def make_bold(function: Callable[[], str]) -> Callable[[], str]:
    def wrapper() -> str:
        name = function()
        return f"<b>{name}</b>"
    return wrapper

def make_emphasis(function: Callable[[], str]) -> Callable[[], str]:
    def wrapper() -> str:
        name = function()
        return f"<em>{name}</em>"
    return wrapper

def make_underlined(function: Callable[[], str]) -> Callable[[], str]:
    def wrapper() -> str:
        name = function()
        return f"<u>{name}</u>"
    return wrapper

@app.route('/')
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye() -> str:
    return "Bye!"

if __name__ == '__main__':
    app.run(debug= True)