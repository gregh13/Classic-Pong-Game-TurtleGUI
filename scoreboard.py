from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self, HEIGHT):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, (HEIGHT / 2) - 80)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"{self.left_score}    {self.right_score}", align=ALIGNMENT, font=FONT)

    def add_point_left(self):
        self.left_score += 1
        self.show_score()

    def add_point_right(self):
        self.right_score += 1
        self.show_score()
