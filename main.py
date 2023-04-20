from turtle import Turtle, Screen
from up_and_down_paddle import UpAndDownPaddle
from left_and_right_paddle import LeftAndRightPaddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=700)
screen.title("Pong")
screen.tracer(0)

lPaddle = UpAndDownPaddle((-350, 0))
rPaddle = UpAndDownPaddle((350, 0))
uPaddle = LeftAndRightPaddle((0, 350))
dPaddle = LeftAndRightPaddle((0, -350))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(rPaddle.GoUp, "Up")
screen.onkey(rPaddle.GoDown, "Down")
screen.onkey(lPaddle.GoUp, "w")
screen.onkey(lPaddle.GoDown, "s")
screen.onkey(uPaddle.GoLeft, "a")
screen.onkey(uPaddle.GoRight, "d")
screen.onkey(dPaddle.GoLeft, "Left")
screen.onkey(dPaddle.GoRight, "Right")


gameIsOn = True

while gameIsOn == True:
    time.sleep(0.1)
    screen.update()
    ball.move()
    

    if ball.distance(rPaddle) < 70 and ball.xcor() > 320 or ball.distance(lPaddle) < 70 and ball.xcor() < -320:
        ball.xBounce()

    if ball.distance(uPaddle) < 70 and ball.ycor() > 320 or ball.distance(dPaddle) < 70 and ball.ycor() < -320:
        ball.yBounce()

    if ball.xcor() > 380:
        ball.resetPos()
        scoreboard.lPoint()

    if ball.xcor() < -380:
        ball.resetPos()
        scoreboard.rPoint()

    if ball.ycor() > 380:
        ball.resetPos()
        scoreboard.lPoint()

    if ball.ycor() < -380:
        ball.resetPos()
        scoreboard.rPoint()


screen.exitonclick()