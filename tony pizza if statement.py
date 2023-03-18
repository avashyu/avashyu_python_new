# Bake Shop Sales

margarita = 10
chicken = 12
seafood = 15

print(f'''Menu)
------------------------------
Margarita    - $ {margarita}
Chicken      - $ {chicken}
Seafood      - $ {seafood}''')



bill = 0

order = input("Kindly place your Order:\n").lower()

if order == 'margarita':
  bill += margarita
elif order =='chicken':
  bill += chicken
elif order == 'seafood':
  bill += seafood
else:
  print(f'Sorry, Wrong Order!! We do not sell {order}')
  exit()

quantity = int(input(f'How Many {order} Pizza(s) do you wish to Order?\n'))


print(f'The Total Bill Amount is $ {bill*quantity}')
# Write your code here :-)
