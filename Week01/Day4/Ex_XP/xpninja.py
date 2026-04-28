#%%
#EX1
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:

# 18,22,24

results = []
C = 50
H = 30
numbers = input("Enter several numbers separated by a comma: ").split(",")
for n in numbers:
    D = int(n)
    Q = int(((2*C*D)/H)**0.5)
    results.append(str(Q))
    
print(",".join(results))
# %%
#EX2
# Instructions
# Given a list of 10 integers to analyze. For example:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]


# 1. Store the list of numbers in a variable.

# 2. Print the following information:
# a. The list of numbers – printed in a single line
# b. The list of numbers – sorted in descending order (largest to smallest)
# c. The sum of all the numbers

# 3. A list containing the first and the last numbers.

# 4. A list of all the numbers greater than 50.

# 5. A list of all the numbers smaller than 10.

# 6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.

# 7. The numbers without any duplicates – also print how many numbers are in the new list.

# 8. The average of all the numbers.

# 9. The largest number.

# 10.The smallest number.

# 11. Bonus: Find the sum, average, largest and smallest number without using built in functions.

# 12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100.
#  Ask the user for an integer between -100 and 100 – repeat this question 10 times. 
# Each number should be added into a variable that you created earlier.

# 13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.

# 14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.

# 15. Bonus: Will the code work when the number of random numbers is not equal to 10?


my_list = [3, 47, 99, -80, 22, 5, 7, -23, 5, 7]
print(f"The list of numbers is {my_list}")
ordered_list = sorted(my_list, reverse=True)
print(f"The list by descending order is: {ordered_list}")
print(f"The sum of all the numbers is: {sum(my_list)}")

short_list = []
short_list.append(my_list[0])
short_list.append(my_list[-1])
print(f"The first and last numbers of the list are {short_list}")
greater_than_50 = []
for i in my_list:
    if i>50:
        greater_than_50.append(i)
print(f"The numbers greater than 50 in the list are: {greater_than_50}")

smaller_than_10 = []
for i in my_list:
    if i<10:
        smaller_than_10.append(i)
print(f"The numbers smaller than 10 in the list are: {smaller_than_10}")

squared_list = []
for i in my_list:
    j = i**2
    squared_list.append(j)
print(f"The squared numbers are: {squared_list}")


no_duplicates = list(set(my_list))
print(f"The list with no duplicates is: {no_duplicates}")
print(f"There are {len(no_duplicates)} numbers in the list with no duplicates")

print(f"The average of all the numbers is: {sum(my_list)/len(my_list)}")
print(f"The maximum of all the numbers is: {max(my_list)}")
print(f"The minimum of all the numbers is: {min(my_list)}")

# %%
#EX3
# Find an interesting paragraph of text online. 
# (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

my_quote = "Imagination is more important than knowledge. For knowledge is limited, whereas imagination embraces the entire world, stimulating progress, giving birth to evolution."
print(f"The paragraph contains {len(my_quote)} characters.")
print(f"The paragraph contains {my_quote.count('.')} sentences.")
words = my_quote.split()
print(f"The paragraph contains {len(words)} words.")
clean_words = [word.strip(".,") .lower() for word in words]
unique_words = set(clean_words)
print(f"The paragraph contains {len(unique_words)} unique words.")


# %%
#EX4
# Write a program that prints the frequency of the words from the input.

# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1

phrase = input("Enter a sentence: ")
words = phrase.split()
for word in set(words):
    print(f"{word}:{words.count(word)}")

# %%
