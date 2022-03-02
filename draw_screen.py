from turtle import Turtle


class DrawLine(Turtle):
    def __init__(self, HEIGHT):
        super().__init__()
        self.screen_height = HEIGHT
        self.hideturtle()
        self.pensize(5)
        self.color("white")
        self.penup()
        self.goto(0, (HEIGHT / 2))
        self.setheading(270)
        self.draw()

    def draw(self):
        while self.ycor() > ((self.screen_height / -2) + (self.screen_height * 0.1)):
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()
