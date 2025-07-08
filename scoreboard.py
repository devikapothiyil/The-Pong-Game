from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score=0
        self.right_score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score()

    def score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.left_score, align="center", font=("Arial", 20, "normal"))
        self.goto(100, 200)
        self.write(arg=self.right_score, align="center", font=("Arial", 20, "normal"))

    def increase_lscore(self):
        self.left_score+=1
        self.score()

    def increase_rscore(self):
        self.right_score += 1
        self.score()
