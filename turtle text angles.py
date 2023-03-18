import turtle,random# Write your code here :-)
c=turtle.getcanvas()
canvas= turtle.Screen()
canvas.setup(400,400)
countries=('china','India','Thailand','Russia','Romania','Germany','Spain','Argentia','France','Kenya')
fonts='Cambria','Arial','Candara','Comic Sans','Courier'
angles= 0,45,90,180
for country in countries:
    avashyu_style= (random.choice(fonts),25,'bold')
    a=random.randint(-200,200)
    b=random.randint(-200,200)
    hex='abcdef0123456789'
    print(random.choice(hex))
    pos1=random.choice(hex)
    pos2=random.choice(hex)
    pos3=random.choice(hex)
    pos4=random.choice(hex)
    pos5=random.choice(hex)
    pos6=random.choice(hex)
    hex_color='#'+pos1+pos2+pos3+pos4+pos5+pos6
    c.create_text(a,b,text=country,angle=random.choice(angles),font=avashyu_style,fill=hex_color)


