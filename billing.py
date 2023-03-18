margarita = 10
pepperoni = 15
barbeque = 17

order = input("Enter your Order: ")

bill = 0

if order == 'margarita':
  bill = bill + margarita

elif order=='pepperoni':
    bill= bill + pepperoni

elif order=='barbeque':
    bill=bill+ barbeque

print(f"Your Final bill is {bill}")
