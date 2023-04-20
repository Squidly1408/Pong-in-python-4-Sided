from turtle import Turtle

class LeftAndRightPaddle(Turtle):
    
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)
    
    
    def GoRight(self):
        newX = self.xcor() + 20
        self.goto(newX, self.ycor())

    def GoLeft(self):
        newX = self.xcor() - 20
        self.goto(newX, self.ycor())

    