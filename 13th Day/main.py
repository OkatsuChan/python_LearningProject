from turtle import Screen
# from turtle import * no advisable
import random

import turtle as t
tim = t.Turtle()
tim.speed("fastest")
screen = t.Screen()

screen.colormode(255)
tim.pensize(1)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spiralgraph(size_of_gap):
    for index in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spiralgraph(5)




screen.exitonclick()