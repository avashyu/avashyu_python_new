import random# Write your code here :-)

clothes='red shirt','blue shirt','orange shirt', ' grey shirt'

pants='red pant','blue pant',' orange pant', 'grey pant'

shoes=' red shoes',' blue shoes', 'orange shoes','grey shoes'

random_clothes=random.choice(clothes)
random_pants=random.choice(pants)
random_shoes=random.choice(shoes)

print(f'Im wearing a {random_clothes} and  a {random_pants} and {random_shoes}')
