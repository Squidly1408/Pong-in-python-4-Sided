from turtle import Turtle

class UpAndDownPaddle(Turtle):
    
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
    
    
    def GoUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def GoDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)

    