import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500,400)

user_bet =screen.textinput("Make your bet", "Which tutle will win the race? Enter a color:")

color = ["red","orange","purple","yellow","green","blue"]
y_position = [-70,-40,-10,20,50,80]
turtles = []

for index in range(6):
    turtle = Turtle(shape ="turtle")
    turtle.color(color[index])
    turtle.penup()
    turtle.goto(x = -230, y = y_position[index])
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_turtle = turtle.pencolor()
            if win_turtle == user_bet:
                print(f"You've won! the {win_turtle} turtle is the winner")
            else:
                print(f"You've lost! the {win_turtle} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()