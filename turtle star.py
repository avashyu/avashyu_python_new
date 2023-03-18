import turtle
# creating a canvas
canvas= turtle.Screen()
canvas.setup(400,400)
# create a turtle charachter
a_turtle= turtle.Turtle()
a_turtle.shape("turtle")
a_turtle.pencolor('blue')
a_turtle.fillcolor('blue')
a_turtle.begin_fill()
a_turtle.right(75)
a_turtle.forward(100)
for s in range(4):
    a_turtle.right(144)
    a_turtle.forward(100)
a_turtle.end_fill()
