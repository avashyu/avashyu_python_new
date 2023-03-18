import turtle,random
canvas= turtle.Screen()
canvas.setup(400,400)
# create a turtle charachter
a_turtle= turtle.Turtle()# Write your code here :-)
a_turtle.pencolor('black')
a_turtle.speed(0)# Write your code here :-)
fonts='cambria','arial','candara','carbel','courier'
avashyu_style= (random.choice(fonts),25,'bold')
a_turtle.write('hello',font=avashyu_style,align='center')
a_turtle.right(90)

