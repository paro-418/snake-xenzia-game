from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('yellow')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-380, 380), random.randint(-380, 380))
