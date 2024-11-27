from turtle import Turtle, Screen

mi_tortuga = Turtle()
mi_tortuga.shape('turtle')
mi_tortuga.color('red')

for _ in range(15):
    mi_tortuga.forward(10)
    mi_tortuga.penup()
    mi_tortuga.forward(10)
    mi_tortuga.pendown()

screen = Screen()
screen.exitonclick()