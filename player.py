from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def move_down(self):
        self.bk(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


