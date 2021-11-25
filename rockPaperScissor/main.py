import random

def play():
    user = input('What is your choice?\n\"R\" for rock, \"P\" for paper, \"S\" for scissors\n:')
    computer = random.choice(['r','p','s'])

    if user == computer:
        print('TIE!')

    if winner(user, computer):
        print('You WON!')

    if winner(computer, user):
        print('You LOSE!')

def winner(x, y):
    # R > S ----------- P > R ----------- S > P
    if (x == 'r' and y == 's') or (x == 'p' and y == 'r') or (x == 's' and y == 'p'):
        return True
while True:
    play()