import random
hex='abcdef0123456789'
print(random.choice(hex))
pos1=random.choice(hex)
pos2=random.choice(hex)
pos3=random.choice(hex)
pos4=random.choice(hex)
pos5=random.choice(hex)
pos6=random.choice(hex)
hex_color='#'+pos1+pos2+pos3+pos4+pos5+pos6
print(hex_color)
