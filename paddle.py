from turtle import Turtle

STEP = 40


class Paddle(Turtle):
    def __init__(self, x_coor, HEIGHT):
        super().__init__()
        self.screen_height = HEIGHT
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setheading(90)
        self.goto(x_coor, 0)
        self.paddle_position = [(self.xcor(), (self.ycor() + 20)), (self.xcor(), (self.ycor() - 20)),
                                (self.xcor(), self.ycor())]
        self.speed("fastest")

    def up(self):
        if self.distance(self.xcor(), (self.screen_height / 2)) > 20:
            self.forward(STEP)
            self.paddle_position = []
            self.paddle_position = [(self.xcor(), (self.ycor() + 20)), (self.xcor(), (self.ycor() - 20)),
                                    (self.xcor(), self.ycor())]

    def down(self):
        if self.distance(self.xcor(), (self.screen_height / -2)) > 20:
            self.backward(STEP)
            self.paddle_position = []
            self.paddle_position = [(self.xcor(), (self.ycor() + 20)), (self.xcor(), (self.ycor() - 20)),
                                    (self.xcor(), self.ycor())]

    def paddle_reset(self):
        self.sety(0)
        self.paddle_position = [(self.xcor(), (self.ycor() + 20)), (self.xcor(), (self.ycor() - 20)),
                                (self.xcor(), self.ycor())]

    # def move(self):
    #     if self.move_in_front:
    #         if not self.ycor() > 280:
    #             self.forward(10)
    #     else:
    #         if not self.ycor() < -280:
    #             self.backward(10)
