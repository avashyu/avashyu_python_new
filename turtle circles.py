import turtle
# creating a canvas
canvas= turtle.Screen()
canvas.setup(400,400)
# create a turtle charachter
a_turtle= turtle.Turtle()
a_turtle.shape("turtle")
a_turtle.pencolor('blue')
a_turtle.fillcolor('red')
a_turtle.begin_fill()
#a_turtle.circle(45)
a_turtle.forward(100)
a_turtle.right(90)
a_turtle.forward(100)
a_turtle.right(90)
a_turtle.forward(100)
a_turtle.right(90)
a_turtle.forward(100)

a_turtle.end_fill()
