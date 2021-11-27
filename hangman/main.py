import random
from wordlist import words
import string

def valid_word(words):
    word = random.choice(words)
    while '_' in word or '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    hangword = valid_word(words)
    wordLetters = set(hangword)
    alpha = set(string.ascii_uppercase)
    guessedLetters = set()

    lives = 6

    while len(wordLetters) > 0 and lives > 0:

        print('You have', lives, 'left and You have used these letters', ' '.join(guessedLetters))

        showWord = [letter if letter in guessedLetters else '-' for letter in hangword]
        print('Current word is: ', ' '.join(showWord))

        userLetter = input('Guess a letter: ').upper()

        if userLetter in alpha - guessedLetters:
            guessedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            
            else:
                lives = lives - 1
                print('Letter is not in the word')

        elif userLetter in guessedLetters:
            print('You already used this character, try again..')

        else:
            print('Wrong input, try again..')
        
    if lives == 0:
        print('You died! the word was', hangword)

    else:
        print('yay! You guessed the word', hangword , 'correctly!')

hangman()