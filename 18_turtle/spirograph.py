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

# mi_tortuga.pensize(5)
mi_tortuga.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        mi_tortuga.color(random_colour())
        mi_tortuga.circle(100)
        mi_tortuga.setheading(mi_tortuga.heading() + size_of_gap)

draw_spirograph(15)

screen = Screen()
screen.exitonclick()
