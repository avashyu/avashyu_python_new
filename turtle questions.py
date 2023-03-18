import turtle

canvas = turtle.Screen()
canvas.setup(420, 420)
canvas.bgcolor("black")
# end of creating canvas
a_turtle = turtle.Turtle()
a_turtle.width(10)
a_turtle.shape("turtle")# Write your code here :-)
a_turtle.pencolor('white')

question= input('do you want to draw a circle')
if question=='yes':
    a_turtle.circle(50)



elif question=='no':
    a_turtle.forward(100)
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.right(90)
    a_turtle.forward(100)



