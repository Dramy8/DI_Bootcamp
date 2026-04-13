#%%
# Use python to create a Hangman game.
# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows 
# (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) 
# or all six body parts are on the gallows.
# The player can’t guess the same letter twice.

# Starter code
# Here is a piece of code that will give you a random word.

import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 

hidden = ["*"] * len(word)

errors = 0

while True:
    print(' '.join(hidden)) 

    letter = input("Guess one letter: ")

    found = False

    for i in range(len(word)):
        if word[i] == letter:
            hidden[i] = word[i]
            found = True

    if not found:
        errors += 1
        if errors == 1:
            print(" O ")

        elif errors == 2:
            print(" O ")
            print(" | ")

        elif errors == 3:
            print(" O ")
            print("/| ")

        elif errors == 4:
            print(" O ")
            print("/|\\ ")

        elif errors == 5:
            print(" O ")
            print("/|\\ ")
            print("/  ")

        elif errors == 6:
            print(" O ")
            print("/|\\ ")
            print("/ \\ ")

    if "*" not in hidden:
        print(f'You found the word: {word}!')
        break
    
    if errors == 6:
        print("Game over!")
        print(f"The word was: {word}")
        break

# %%
