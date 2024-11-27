import random
from turtle import Turtle, Screen

mi_tortuga = Turtle()
mi_tortuga.shape('turtle')
mi_tortuga.color('red')

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for no_sides in range(3, 8):
    mi_tortuga.color(random.choice(colours))
    for _ in range(no_sides):
        angle=360/no_sides
        mi_tortuga.forward(100)
        mi_tortuga.right(angle)

screen = Screen()
screen.exitonclick()