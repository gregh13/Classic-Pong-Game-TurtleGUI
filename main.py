from turtle import Screen
from draw_screen import DrawLine
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

WIDTH = 1000
HEIGHT = 500
GAME_SPEED_START = 0.011

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# Objects being created
dashed_line = DrawLine(HEIGHT)
paddle_left = Paddle(x_coor=((WIDTH - 50) / -2), HEIGHT=HEIGHT)
paddle_right = Paddle(x_coor=((WIDTH - 50) / 2), HEIGHT=HEIGHT)
ball = Ball()
scoreboard = Scoreboard(HEIGHT)
screen.update()

screen.onkey(fun=paddle_left.up, key="w")
screen.onkey(fun=paddle_left.down, key="s")
screen.onkey(fun=paddle_left.up, key="a")
screen.onkey(fun=paddle_left.down, key="d")

screen.onkey(fun=paddle_right.up, key="Up")
screen.onkey(fun=paddle_right.down, key="Down")
screen.onkey(fun=paddle_right.up, key="Right")
screen.onkey(fun=paddle_right.down, key="Left")

screen.textinput("     Let's Play Pong!", "\n\n  Left side uses 'A/W/S/D'                   Right side uses Arrows"
                                          "\n\n\n\n                             Click any button to begin")

screen.listen()

time.sleep(1)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED_START)
    ball.ball_moving()
    hit_already = False

    # Detect collision with Paddle

    # Left Paddle Side Positions Hit Detection
    for parts in paddle_left.paddle_position[:2]:
        if ball.distance(parts) < 20 and 90 < ball.heading() < 270 and ball.xcor() > paddle_left.xcor():
            hit_already = True
            if ball.heading() <= 180:
                ball.setheading((180 - ball.heading()) + random.randint(10, 30))
                # ball.forward(5)
                if GAME_SPEED_START >= 0.003:
                    GAME_SPEED_START -= 0.002
                break
            elif ball.heading() >= 180:
                ball.setheading((180 - ball.heading()) + random.randint(-30, -10))
                # ball.forward(5)
                if GAME_SPEED_START >= 0.003:
                    GAME_SPEED_START -= 0.002
                break

    # Left Paddle Middle Position Hit Detection
    if not hit_already:
        if ball.distance(
                paddle_left.paddle_position[2]) < 20 and 90 < ball.heading() < 270 and ball.xcor() > paddle_left.xcor():
            ball.setheading((180 - ball.heading()) + random.randint(-5, 5))
            # ball.forward(5)
            if GAME_SPEED_START < 0.011:
                GAME_SPEED_START += 0.002

    # Right Paddle Side Positions Hit Detection
    for parts in paddle_right.paddle_position[:2]:
        if ball.distance(parts) < 20 and (
                0 <= ball.heading() < 90 or 270 < ball.heading() <= 360) and ball.xcor() < paddle_right.xcor():
            hit_already = True
            if ball.heading() <= 180:
                ball.setheading((180 - ball.heading()) + random.randint(10, 30))
                # ball.forward(5)
                if GAME_SPEED_START >= 0.003:
                    GAME_SPEED_START -= 0.002
                break
            elif ball.heading() >= 180:
                ball.setheading((180 - ball.heading()) + random.randint(-30, -10))
                # ball.forward(5)
                if GAME_SPEED_START >= 0.003:
                    GAME_SPEED_START -= 0.002
                break

    # Right Paddle Middle Position Hit Detection
    if not hit_already:
        if ball.distance(paddle_right.paddle_position[2]) < 20 and (
                0 <= ball.heading() < 90 or 270 < ball.heading() <= 360) and ball.xcor() < paddle_right.xcor():
            ball.setheading((180 - ball.heading()) + random.randint(-5, 5))
            # ball.forward(5)
            if GAME_SPEED_START < 0.011:
                GAME_SPEED_START += 0.002

    # Detect collision with Wall
    if ball.ycor() <= (HEIGHT - 40) / -2 or ball.ycor() >= (HEIGHT - 10) / 2:
        ball.setheading(360 - ball.heading())

    # Detect a score:
    if ball.xcor() < (WIDTH / -2):
        scoreboard.add_point_right()
        if scoreboard.right_score == 5:
            game_is_on = False
            dashed_line.goto((WIDTH / 4), 0)
            dashed_line.write("WINNER", align="center", font=("Courier", 40, "bold"))
        else:
            ball.ball_reset()
            paddle_left.paddle_reset()
            paddle_right.paddle_reset()
            time.sleep(1)
            screen.update()
            GAME_SPEED_START = 0.011
            time.sleep(1)

    if ball.xcor() > (WIDTH / 2):
        scoreboard.add_point_left()
        if scoreboard.left_score == 5:
            game_is_on = False
            dashed_line.goto((WIDTH / -4), 0)
            dashed_line.write("WINNER", align="center", font=("Courier", 40, "bold"))
        else:
            ball.ball_reset()
            paddle_left.paddle_reset()
            paddle_right.paddle_reset()
            time.sleep(1)
            screen.update()
            GAME_SPEED_START = 0.011
            time.sleep(1)

screen.exitonclick()
