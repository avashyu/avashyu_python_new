import turtle
canvas= turtle.Screen()
canvas.setup(420,420)
# create a turtle charachter
a_turtle= turtle.Turtle()
a_turtle.width(10)
a_turtle.shape("turtle")# Write your code here :-)

width=canvas.window_width()
height=canvas.window_height()
a_turtle.penup()
a_turtle.goto(-width//2,height//2)
a_turtle.pendown()
a_turtle.forward(width)
#a_turtle.goto(width//2,height//2)
radius=65
a_turtle.penup()
a_turtle.goto(0,-radius//2)
a_turtle.pendown()
a_turtle.circle(radius)
