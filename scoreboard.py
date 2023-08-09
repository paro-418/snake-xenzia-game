from turtle import Turtle

FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.goto(0, 368)
        self.write(f"score: {self.score} highscore: {self.high_score}  press e to exit", align='center', font=("Arial", 24, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score}  highscore: {self.high_score}", align='center', font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
