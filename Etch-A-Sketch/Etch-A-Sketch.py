import turtle as t

tomy = t.Turtle()
t.colormode(255)
tomy.shape("turtle")
tomy.forward(100)
# tomy.seth(90)
tomy.forward(100)
tomy.seth(180)
tomy.forward(100)

def move_forward():
    tomy.forward(10)

def move_backwards():
    tomy.seth(180)

def counter_clockwise():
    t.left(90)

t.listen()
t.onkey(counter_clockwise, "a")

screen = t.Screen()
screen.exitonclick()