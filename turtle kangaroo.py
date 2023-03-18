import turtle# Write your code here :-)
screen = turtle.Screen()
pen = turtle.Turtle()

color_head='#AB723B'
color_ear='#DED7CB'
color_nose='#1F221F'




for a in range(4):
    if a%2==0:
        x=-75
        y=75
        radius=50
    else:
        x += 5
        y += 15
        radius -= 15
    if a ==2:
        x=75
    pen.penup()

    pen.goto(x, y)
    pen.pendown()




    if a%2==0:
        pen.fillcolor(color_ear)
    else :
        pen.fillcolor(color_head)

    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

pen.penup()
pen.goto(0, -75)
pen.pendown()

pen.color(color_head)
pen.fillcolor(color_head)

pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(0, -100)
pen.pendown()

pen.color(color_nose)
pen.fillcolor(color_nose)

pen.begin_fill()
pen.circle(45)
pen.end_fill()

x=-50
for itr in range(2):

  pen.penup()
  pen.goto(x, 25)
  pen.pendown()

  pen.color("black")
  pen.fillcolor("black")

  pen.begin_fill()
  pen.circle(20)
  pen.end_fill()

  x = 50

pen.hideturtle()
