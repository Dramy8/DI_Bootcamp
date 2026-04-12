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
    input("enter a word: ")
    input("enter a word: ")
    input("enter a word: ")
    input("enter a word: ")
    input("enter a word: ")
    input("enter a word: ")
    input("enter a word: ")
]

letter = input("enter a character: ")

for word in words:
    print([0])

#%%

# %%
