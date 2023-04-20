from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lScore = 0
        self.rScore = 0
        self.ScoreboardUpdate()
    
    def ScoreboardUpdate(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lScore, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.rScore, align="center", font=("Courier", 50, "normal"))

    def lPoint(self):
        self.lScore += 1
        self.ScoreboardUpdate()

    def rPoint(self):
        self.rScore += 1
        self.ScoreboardUpdate()