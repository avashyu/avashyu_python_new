import turtle

a_turtle = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("white")

def square(y):
    for x in range(4):
        a_turtle.forward(y)
        a_turtle.right(90)
square(200)

def circle(a):
    a_turtle.circle(a)
circle(a=100)
