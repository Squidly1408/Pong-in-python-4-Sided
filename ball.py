from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.xMove = 8
        self.yMove = 8
    
    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)
    
    def yBounce(self):
        self.yMove *= -1
    
    
    def xBounce(self):
        self.xMove *= -1

    def resetPos(self):
        self.goto(0, 0)
        self.xBounce()