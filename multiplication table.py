number=int(input('please input a number of your choice:'))
table_limit=int(input('what number do you want the the table to go up to?:'))
#when the user inputs the number a multiplication table will apear in the form of a list
for n in range(1,table_limit+1):
    print(f'{number}x{n} = {n*number}')

