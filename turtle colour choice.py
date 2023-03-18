import turtle
import random
canvas = turtle.Screen()
canvas.setup(420, 420)
canvas.bgcolor("black")
# end of creating canvas

a_turtle = turtle.Turtle()
a_turtle.width(10)
a_turtle.shape("turtle")# Write your code here :-)
a_turtle.pencolor('red')
hex='abcdef0123456789'


turtle.speed(-15)

for c in range(300):
    pos1=random.choice(hex)
    pos2=random.choice(hex)
    pos3=random.choice(hex)
    pos4=random.choice(hex)
    pos5=random.choice(hex)
    pos6=random.choice(hex)
    hex_color='#'+pos1+pos2+pos3+pos4+pos5+pos6
    a_turtle.pencolor(hex_color)
    a_turtle.right(90)
    a_turtle.forward(c)


