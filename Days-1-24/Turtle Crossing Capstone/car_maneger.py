from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'pink', 'purple', 'black']
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10

class CarManeger:
    
    def __init__(self) -> None:
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self) -> None:
        car_creation_delay = random.randint(0,5)
        if car_creation_delay == 2:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            self.cars.append(new_car)
        
    def cars_move(self) -> None:
        for car in self.cars:
            # car.backward(self.car_speed)
            car.forward(self.car_speed)
    
    def increament_speed(self) -> None:
        self.car_speed += MOVE_INCREMENT
    