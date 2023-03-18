#create a list of words
# create a list of colours
#define a loop that will display the words on the screen
# each word should be of a different colour and size
# the words should appear on different positions on the screen
import turtle,random
canvas= turtle.Screen()
canvas.setup(400,400)
# create a turtle charachter
a_turtle= turtle.Turtle()# Write your code here :-)
a_turtle.pencolor('black')
a_turtle.speed(3)
color=('red','green','blue','yellow','pink','black','orange','violet')
word=('china','India','Thailand','Russia','Romania','Germany','Spain','Argentia','France','Kenya')
for x in range(75):
    hex='abcdef0123456789'
    print(random.choice(hex))
    pos1=random.choice(hex)
    pos2=random.choice(hex)
    pos3=random.choice(hex)
    pos4=random.choice(hex)
    pos5=random.choice(hex)
    pos6=random.choice(hex)
    hex_color='#'+pos1+pos2+pos3+pos4+pos5+pos6
    avashyu_style='courier',random.randint(5,30),'bold'
    a_turtle.write(random.choice(word),font=avashyu_style)
    random_x=random.randint(-200,200)
    random_y=random.randint(-200,200)
    a_turtle.penup()
    a_turtle.goto(random_x,random_y)
    a_turtle.pendown()
    a_turtle.pencolor(hex_color)
    a_turtle.right(45)
