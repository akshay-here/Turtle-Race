from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        But too many cars are generated So have to create random chance of car being generated
        So if random_no selected between 1 and 6 is same then only car created
        This will reduce the number of cars being created
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250, 250)
            new_car.goto(x=300, y=new_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

