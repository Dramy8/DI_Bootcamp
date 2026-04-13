#%%
#EX1
#Write code that concatenates two lists together without using the + sign.

list1 = [1,3,5,7]
list2 = [2,4,6,8]
list1.extend(list2)
print(list1)
# %%
#EX2
#Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
i = 1500
while i<=2500:
    if i%5==0 or i%7==0:
        print(i)
    i += 1

#other option

# for i in range(1500, 2501):
#     if i % 5 == 0 or i % 7 == 0:
#         print(i)
# %%
#EX3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

nom = input("Enter a name: ")
if nom in names:
    print(names.index(nom))

# %%
#EX4
#Ask the user for 3 numbers and print the greatest number.
list = [
int(input("Enter the first number: ")),
int(input("Enter the second number: ")),
int(input("Enter the third number: "))
]
print(f"The biggest number you entered was {max(list)}")
# %%
#EX5
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
# %%
#EX6
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence 
# of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

words = [
    input("enter a word: "),
    input("enter a word: "),
    input("enter a word: "),
    input("enter a word: "),
    input("enter a word: "),
    input("enter a word: "),
    input("enter a word: ")
]

letter = input("enter a character: ")

for word in words:
    if letter in word:
        print(word.index(letter))
    else:
        print(f"the letter {letter} does not appear in {word}")

#%%
#EX7
# Create a list of numbers from one to one million and 
# then use min() and max() to make sure your list actually starts at one and ends at one million.
# Use the sum() function to see how quickly Python can add a million numbers.

num = []

i = 1
while i <= 1000000:
    num.append(i)
    i += 1

print(sum(num))

# %%
#EX8
# Write a program which accepts a sequence of comma-separated numbers. 
# Generate a list and a tuple which contain every number.

values = input("Enter a sequence of comma-separated numbers: ").split(',')
list_values = [int(v) for v in values]
print(list_values)
t = tuple(list_values)
print(t)
# %%
#EX9
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random
wins = 0
losses = 0

while True:
    guess = input("Enter a number (1-9) or 'exit': ")

    if guess.lower() == "exit":
        break

    guess = int(guess)
    random_number = random.randint(1, 9)

    if guess == random_number:
        print("Winner!")
        wins += 1
    else:
        print("Better luck next time!")
        losses += 1

print(f"Games won: {wins}")
print(f"Games lost: {losses}")

# %%
