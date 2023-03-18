import turtle# Write your code here :-)
screen = turtle.Screen()
pen = turtle.Turtle()


color='#B4B4B4'

color_ear='#FECCCB'
color_whisker='black'

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
        pen.fillcolor(color)
    else :
        pen.fillcolor(color_ear)

    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

pen.penup()
pen.goto(0, -75)
pen.pendown()

pen.color(color)
pen.fillcolor(color)

pen.begin_fill()
pen.circle(100)
pen.end_fill()

pen.penup()
pen.goto(0,-25)
pen.pendown()

pen.color(color_ear)
pen.fillcolor(color_ear)

pen.begin_fill()
pen.circle(20)
pen.end_fill()


pen.color(color_whisker)
pen.penup()
pen.goto(20,-15)
pen.pendown()

pen.forward(45)

pen.penup()
pen.goto(20,5)
pen.pendown()

pen.forward(45)

pen.penup()
pen.goto(-65,-15)
pen.pendown()
pen.forward(45)

pen.penup()
pen.goto(-65,5)
pen.pendown()
pen.forward(45)

x=-50
for itr in range(2):

  pen.penup()
  pen.goto(x, 25)
  pen.pendown()

  pen.color("black")
  pen.fillcolor("black")

  pen.begin_fill()
  pen.circle(10)
  pen.end_fill()

  x = 50



pen.hideturtle()

mouse=input('what is  this animal?')
print(mouse)
avashyu_style= ('gothic',25,'bold')
pen.penup()
pen.goto(0,-100)
pen.pendown()
pen.write(mouse,font=avashyu_style,align='center')







