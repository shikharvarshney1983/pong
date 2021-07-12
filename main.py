import turtle as t
from paddles import Paddle
from ball import Ball
from score import Score
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()
    score.update_scoreboard()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_from_paddle()
    elif ball.xcor() > 330: 
        ball.setpos(0,0)
        ball.bounce_from_paddle()
        score.l_point()        
    elif ball.xcor() < -330:
        ball.setpos(0,0)
        ball.bounce_from_paddle()
        score.r_point()

    if score.l_score >= 10 or score.r_score >= 10:
        score.game_over()
        is_game_on = False

screen.exitonclick()