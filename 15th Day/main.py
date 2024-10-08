import time
import turtle
from turtle import Turtle,Screen
from turtledemo.penrose import start
from snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()


screen.exitonclick()
