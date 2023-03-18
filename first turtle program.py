# Write your code here :-)
import turtle
# creating a canvas
canvas= turtle.Screen()
canvas.setup(400,400)
# create a turtle charachter
a_turtle= turtle.Turtle()
a_turtle.shape("turtle")
a_turtle.pencolor('blue')
for a in range(10,1250,5):
    a_turtle.forward(a)
   # a_turtle.write(str(a))
    a_turtle.right(90)


