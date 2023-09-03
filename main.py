import time
from turtle import Screen
from player import Player
from car import Car
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Creating all the objects
player = Player()
car = Car()
score = Score()

screen.listen()
screen.onkey(key='Up', fun=player.move_up)
screen.onkey(key='Down', fun=player.move_down)


should_continue = True
while should_continue:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    """
    To detect if player collides with a car
    Have to check the distance between player and car
    If player hits car then game should stop and display GAME OVER
    """
    for i in car.all_cars:
        if i.distance(player) < 20:
            should_continue = False
            score.game_over()
    """
    To see if player has reached the finish line
    If has reached top then car speed should increase and level should be incremented
    If car not reached finish line then it would have collided with car 
    """
    if player.finish_line():
        player.reset_position()
        car.level_up()
        score.increase_level()

screen.exitonclick()