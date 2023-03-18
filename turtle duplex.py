import turtle
import random

a_turtle = turtle.Turtle()

g_turtle = turtle.Turtle()

x_turtle = turtle.Turtle()

a_turtle.setheading(180)
g_turtle.setheading(180)
g_turtle.pencolor('red')
a_turtle.pencolor('blue')
x_turtle.setheading(45)

a_turtle.width(random.randint(1,10))
g_turtle.width(random.randint(5,10))


screen = turtle.Screen()
screen.bgcolor("white")# Write your code here :-)
def turtle_one():
    a_turtle.left(63)
    a_turtle.backward(100)
    turtle.ontimer(turtle_one,100)

def turtle_two():
    g_turtle.right(57)
    g_turtle.forward(100)
    turtle.ontimer(turtle_two,100)

def turtle_three():
    x_turtle.circle(50)
    turtle.ontimer(turtle_three,100)

turtle.ontimer(turtle_one,100)
turtle.ontimer(turtle_two,100)
turtle.ontimer(turtle_three,100)
