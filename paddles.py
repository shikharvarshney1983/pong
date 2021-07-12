from turtle import *

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)
    
    def up(self):
        self.setpos(self.xcor(),self.ycor() + 20)

    def down(self):
        self.setpos(self.xcor(),self.ycor() - 20)