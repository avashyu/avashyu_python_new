import turtle

canvas = turtle.Screen()
canvas.setup(420, 420)
canvas.bgcolor("black")
# end of creating canvas

a_turtle = turtle.Turtle()
a_turtle.pencolor('white')
a_turtle.width(10)
a_turtle.shape("turtle")
radius=int(input('what is the radius'))

a_turtle.circle(radius)
a_turtle.penup()
a_turtle.goto(0,-100)
avashyu_style= ('courier',25,'bold')
a_turtle.write('the radius is' + str(radius),font= avashyu_style,align='center')
