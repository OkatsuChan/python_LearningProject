import time
import turtle
from turtle import Turtle,Screen
from turtledemo.penrose import start

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")


screen.tracer(0)
starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []


for positions in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(positions)
    segments.append(new_segment)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    for seg_num in range(len(segments)-1,0 ,-1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].right(90)

screen.exitonclick()
