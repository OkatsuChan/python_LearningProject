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


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()


screen.exitonclick()
