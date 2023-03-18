import turtle

pen = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("white")

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "white"]

size = 240

pen.penup()
pen.goto(0,-360)
pen.pendown()


for color in rainbow:
    if color=='yellow':
        size=size-20
        break
    pen.color(color)
    pen.fillcolor(color)

    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

    size = size - 20# Write your code here :-)
