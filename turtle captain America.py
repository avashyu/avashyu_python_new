import turtle# Write your code here :-)
import turtle

canvas = turtle.Screen()
canvas.setup(420, 420)
canvas.bgcolor("crimson")
# end of creating canvas
circle_size_position=200
a_turtle = turtle.Turtle()
a_turtle.width(10)
a_turtle.shape("turtle")
colors=('white','crimson','white','crimson')

for c in colors:

    a_turtle.penup()
    a_turtle.goto(0,-circle_size_position)
    a_turtle.pendown()

    a_turtle.pencolor(c)
    a_turtle.fillcolor(c)

    a_turtle.begin_fill()
    a_turtle.circle(circle_size_position)
    a_turtle.end_fill()

    circle_size_position = circle_size_position-35

a_turtle.penup()
a_turtle.goto(0,-circle_size_position)
a_turtle.pendown()

a_turtle.pencolor('darkblue')
a_turtle.fillcolor('darkblue')

a_turtle.begin_fill()
a_turtle.circle(circle_size_position)
a_turtle.end_fill()

a_turtle.penup()
a_turtle.goto(0,50)
a_turtle.pendown()

a_turtle.pencolor('white')
a_turtle.fillcolor('white')


a_turtle.begin_fill()
a_turtle.right(75)
a_turtle.forward(100)


for s in range(4):
    a_turtle.right(144)
    a_turtle.forward(100)
a_turtle.end_fill()

