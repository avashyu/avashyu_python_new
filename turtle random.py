import turtle,random
canvas= turtle.Screen()
canvas.setup(400,400)
# create a turtle charachter
a_turtle= turtle.Turtle()# Write your code here :-)
a_turtle.pencolor('white')
a_turtle.speed(0)
color=('red','green','blue','yellow','pink','black','orange','violet')
for _ in range(1000):
    random_color= random.choice(color)
    random_x=random.randint(-200,200)
    random_y=random.randint(-200,200)
    a_turtle.goto(random_x,random_y)
    a_turtle.fillcolor(random_color)
    a_turtle.begin_fill()
    a_turtle.circle(random.randint(10,50))
    a_turtle.end_fill()




