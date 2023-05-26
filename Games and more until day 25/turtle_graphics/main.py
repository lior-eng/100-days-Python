# from turtle import Turtle, Screen, colormode
import turtle as t
import random

tomy = t.Turtle()
t.colormode(255)
tomy.shape("turtle")

   ### Square movement ###
# for _ in range (4):
#     tomy.forward(100)
#     tomy.left(90)

   ### Dashed line ###
# for i in range (10):
#     if i % 2 == 0:
#         tomy.pendown()
#     else:
#         tomy.penup()
#     tomy.forward(20)

   ### Create shapes in loop ###
   
colors = ["wheat", "black", "gray", "red", "green", "blue", "orange", "purple", "pink"]   
tomy.pensize(8)
tomy.speed("fast")

def random_color() -> tuple:
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)
    

# def draw_shape(number_of_sides: int, start_sides: int = 3) -> None:
#     for i in range (number_of_sides):
#         for _ in range (i + start_sides):
#             tomy.color(colors[i])
#             tomy.forward(50)
#             tomy.right(360/(i + start_sides))    
# draw_shape(6)

   ### Ramndom move ###

# for _ in range (40):
#     tomy.color(random_color())
#     tomy.forward(30)
#     tomy.left(random.randint(0,360))

   ### Draw spirograph
   
tomy.pensize(0)
tomy.speed("fastest")

def Draw_spirograph(size_of_gap: int) -> None:
    print(size_of_gap)
    for _ in range (360 // size_of_gap):
        tomy.color(random_color())
        tomy.circle(100)
        tomy.setheading(tomy.heading() + size_of_gap) 
Draw_spirograph(7)

screen = t.Screen()
screen.exitonclick()