import random as rand

def guess(number):
    a = 1
    random_int = rand.randint(a , number)
    guess = a - 1
    while guess != random_int:
        try:
            guess = int(input('Guess the number: '))
        except ValueError:
            print('You must input a integer')
        if guess < random_int:
            print('Try again. Too low')
        elif guess > random_int:
            print('Try again. Too high')
    print(f'Congrates. You\'ve guessed the number {random_int} correctly!')
status = 0
while status == 0:
    try:
        level = int(input("1. Easy\n2. Medium\n3. Hard\nEnter level: "))
        status = 1
    except ValueError:
        pass 

if level == 3:
    print('1 - 1000')
    guess(1000)
elif level == 2:
    print('1 - 100')
    guess(100)
elif level == 1:
    print('1 - 10')
    guess(10)
elif level > 3 or level < 1:
    print('Enter valid level.')

#devil-prog