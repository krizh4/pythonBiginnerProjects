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

def cguess(number):
    resp = ''
    low = 0
    high = number
    while resp != 'c':
        if low != high:
            guess = rand.randint(low, high)
        elif low == high:
            guess = low
        resp = input(f'Is {guess} Too high(H), Too low(L) or Correct(C)??').lower()[0]
        if resp == 'h':
            high = guess - 1
        elif resp == 'l':
            low = guess + 1
        if low > high:
            break
    print(f'I guessed the number {guess} correctly!')

mode = 0
while mode == 0:
    try:
        mode = int(input("1. You\n2. Computer\nWho's guessing number: "))
    except ValueError:
        pass

level = 0
while level == 0:
    try:
        level = int(input("1. Easy\n2. Medium\n3. Hard\nEnter level: "))
    except ValueError:
        pass

if mode == 1:
    run = guess
elif mode == 2:
    run = cguess
elif mode != 1 or mode != 2:
    run = guess

if level == 3:
    print('1 - 1000')
    run(1000)
elif level == 2:
    print('1 - 100')
    run(100)
elif level == 1:
    print('1 - 10')
    run(10)
elif level > 3 or level < 1:
    print('Enter valid level.')

#devil-prog