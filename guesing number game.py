import random,time

print('''welcome to the guessing number game,
in this game you have to guess the computers number which is between 1 and 5
there are 3 rounds and whoever wins the majority, will win the game,
good luck.''')

players_points=0
computers_points=0
print('*'*30)
time.sleep(10)
for n in range(3):
    print(f' round {n+1}\n')
    guess=int(input('enter you guess:'))
    numbers=random.randint(1,5)
    if guess==numbers:
        players_points=players_points+1
        print(f' you were correct\n')
    else:
        computers_points=computers_points+1
        print(f' you were incorrect because the correct number was {numbers}\n')

    time.sleep(4)
    print(f' you have {players_points}p')
    time.sleep(2)
    print(f' the computer has {computers_points}p\n')
    time.sleep(3)
    print('*'*30)
if computers_points>players_points:
    print('you lost')
else:
    print('you won!')

time.sleep(2)

print(f' the final score was {computers_points}-{players_points}')


