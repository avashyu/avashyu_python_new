import turtle

canvas = turtle.Screen()
canvas.setup(420, 420)
canvas.bgcolor("black")
# end of creating canvas

a_turtle = turtle.Turtle()
a_turtle.width(10)
a_turtle.shape("turtle")
a_turtle.fillcolor("white")
# end of creating turtle

a_turtle.begin_fill()
a_turtle.pencolor("white")
a_turtle.penup()
width = canvas.window_width()
height = canvas.window_width()
a_turtle.goto(-width // 2, height // 2)
a_turtle.pendown()
a_turtle.forward(width)
a_turtle.right(90)
a_turtle.forward(height)
a_turtle.right(90)
a_turtle.forward(width)
a_turtle.right(90)
a_turtle.forward(height)
a_turtle.end_fill()
# end of square(white)

radius = 65
a_turtle.penup()
a_turtle.goto(65, -radius // 6)
a_turtle.pendown()
a_turtle.begin_fill()
a_turtle.pencolor("red")
a_turtle.circle(radius)
a_turtle.fillcolor("red")
a_turtle.end_fill()
# end of circle (red)
# end of japan flag
