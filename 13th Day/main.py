from turtle import Screen
# from turtle import * no advisable
import random

import turtle as t
tim = t.Turtle()
tim.speed(5)
screen = t.Screen()
screen.colormode(255)

tim.pensize(20)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)



for index in range(100):
    color = random_color()
    tim.color(color)
    tim.pencolor(color)
    tim.forward(40)
    tim.setheading(random.choice([0, 90, 180, 270]))






screen.exitonclick()