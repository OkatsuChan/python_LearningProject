from turtle import Screen
# from turtle import * no advisable
import random

import turtle as t
tim = t.Turtle()
tim.speed(1)
screen = t.Screen()
screen.colormode(255)

def make_square():
    for key in range(4):
        tim.forward(100)
        tim.right(90)

def make_triangle():
    for key in range(3):
        tim.forward(100)
        tim.right(120)

def make_pentagon():
    for key in range(5):
        tim.forward(100)
        tim.right(72)

def make_hexagon():
    for key in range(6):
        tim.forward(100)
        tim.right(60)

def make_heptagon():
    for key in range(7):
        tim.forward(100)
        tim.right(51.42857142857143)

def make_octagon():
    for key in range(8):
        tim.forward(100)
        tim.right(45)

def make_nonagon():
    for key in range(9):
        tim.forward(100)
        tim.right(40)

def make_decagon():
    for key in range(10):
        tim.forward(100)
        tim.right(36)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.shape("turtle")

tim.color("red")

# dash line
# for _ in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

make_triangle()
tim.color(random_color())
make_square()
tim.color(random_color())
make_pentagon()
tim.color(random_color())
make_hexagon()
tim.color(random_color())
make_heptagon()
tim.color(random_color())
make_octagon()
tim.color(random_color())
make_nonagon()
tim.color(random_color())
make_decagon()


import heroes
print(heroes.gen())














screen.exitonclick()