from turtle import Turtle
import random

STARTING_ANGLES = [10, 15, 20, 340, 345, 350, 170, 165, 160, 180, 190, 195]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(1)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.straight_ahead = True
        random_angle = random.choice(STARTING_ANGLES)
        self.setheading(random_angle)

    def ball_moving(self):
        self.forward(5)

    def ball_reset(self):
        self.hideturtle()
        self.goto(0, 0)
        random_angle = random.choice(STARTING_ANGLES)
        self.setheading(random_angle)
        self.showturtle()
