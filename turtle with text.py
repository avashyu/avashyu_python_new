import turtle

canvas = turtle.Screen()
canvas.setup(420, 420)
canvas.bgcolor("black")
# end of creating canvas

a_turtle = turtle.Turtle()
a_turtle.width(10)
a_turtle.shape("turtle")# Write your code here :-)
a_turtle.pencolor('white')
name= input('what is your name')
print(name)
#setting a styling for the text

avashyu_style= ('courier',25,'bold')
a_turtle.write(name,font=avashyu_style,align='center')
