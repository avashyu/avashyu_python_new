import turtle

a_turtle = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("white")

rainbow = ("blue","red","green", "pink", "brown", "indigo", "violet", "white")

size = 240

a_turtle.penup()
a_turtle.goto(0,-360)
a_turtle.pendown()


for color in rainbow:
    a_turtle.color(color)
    a_turtle.fillcolor(color)
    size=size-20


    a_turtle.begin_fill()
    a_turtle.circle(size)
    a_turtle.end_fill(),





