#random walk with RGB random color
from turtle import Turtle, Screen
import turtle as t
import random

#to visualize the screen
my_screen = Screen()
my_screen.colormode(255)
tim = t.Turtle()
tim.pensize(15)
tim.speed("fastest")
tim.hideturtle()

direction = [0, 90, 180, 270]

#function to make a random colors
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)   
    return random_color

for _ in range(400):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(direction))

#  close screen by mouse click
my_screen.exitonclick()

