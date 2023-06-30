import turtle as t

tomy = t.Turtle(shape="turtle")
tomy.color("black")

def move_forward():
    tomy.forward(20)
    
def move_backwards():
    tomy.backward(20)
    
def turn_left():
    tomy.left(10)

def turn_right():
    tomy.right(10)
    
def clear_screen():
    tomy.penup()
    tomy.clear()
    tomy.home()
    tomy.pendown()
    
t.listen()
t.onkeypress(move_forward, "w")
t.onkeypress(move_backwards, "s")
t.onkeypress(turn_left, "a")
t.onkeypress(turn_right, "d")
t.onkey(clear_screen, "c")

screen = t.Screen()
screen.exitonclick()