import random
import turtle
from turtle import Turtle, Screen

mi_tortuga = Turtle()
mi_tortuga.shape('turtle')
mi_tortuga.color('red')
turtle.colormode(255) # Importante añadir


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


directions = [0, 90, 180, 270]
mi_tortuga.pensize(5)
mi_tortuga.speed("fastest")

for _ in range(200):
    mi_tortuga.color(random_colour())
    mi_tortuga.forward(30)
    mi_tortuga.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
