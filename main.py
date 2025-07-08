import turtle
from paddle import Paddle
from ball import  Ball
from scoreboard import ScoreBoard
import time

screen=turtle.Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
my_ball=Ball()
my_score=ScoreBoard()

screen.listen()
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down,"Down")
screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(my_ball.move_speed)
    screen.update()
    my_ball.move()

    #Detects collision with walls
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()

    #Detects collision  with paddle
    if my_ball.distance(right_paddle) < 50 and my_ball.xcor() > 320 or my_ball.distance(left_paddle) < 50 and my_ball.xcor() > -320:
        my_ball.bounce_x()

    #Detects right paddle miss
    if my_ball.xcor()>380:
        my_ball.reset_position()
        my_score.increase_lscore()

    # Detects left paddle miss
    if my_ball.xcor()<-380:
        my_ball.reset_position()
        my_score.increase_rscore()


screen.exitonclick()
