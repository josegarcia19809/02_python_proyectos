from turtle import Turtle, Screen

mi_tortuga = Turtle()
mi_tortuga.shape('turtle')
mi_tortuga.color('red')

for _ in range(4):
    mi_tortuga.forward(100)
    mi_tortuga.right(90)

screen = Screen()
screen.exitonclick()