import random
from turtle import Turtle, Screen

mi_tortuga = Turtle()
mi_tortuga.shape('turtle')
mi_tortuga.color('red')

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
mi_tortuga.pensize(15)
mi_tortuga.speed("fastest")

for _ in range(200):
    mi_tortuga.color(random.choice(colours))
    mi_tortuga.forward(30)
    mi_tortuga.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
