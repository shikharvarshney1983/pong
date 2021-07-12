from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1
        
    def bounce_from_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9
        
    def reset(self):
        self.setpos(0,0)
        self.ball_speed = 0.1
        self.bounce_from_paddle()