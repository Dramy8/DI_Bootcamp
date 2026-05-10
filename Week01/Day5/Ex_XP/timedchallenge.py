#%%
# Write a program to reverse the sentence wordwise.
REverseinp= input("Enter a sentence here: ")
words = REverseinp.split()
reversed_words = words[::-1]
print(' '.join(reversed_words))
# %%
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
# Hint: Google perfect numbers
# Example

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False
# You have 30 minutes to finish this challenge :
n = int(input('enter a number: '))
total = 0
for i in range(1,n):
    if n%i == 0:
        total += i
print(total == n)




# %%
