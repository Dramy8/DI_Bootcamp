#%%
#EX1
# Write a script that inserts an item at a defined index in a list.

my_list = ['apple','mom','cleo','cola']
my_list.insert(-2, "orange")
#%%
#EX2
# Write a script that counts the number of spaces in a string.

def counting():
    text = input("Enter a text: ")
    return text.count(' ')

counting()
# %%
#EX3
# Write a script that calculates the number of upper case letters and lower case letters in a string.

def uplow():
    text = input("Enter a text: ")
    
    upper = 0
    lower = 0
    
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    
    print(f"Uppercase letters: {upper}")
    print(f"Lowercase letters: {lower}")

uplow()
# %%
#EX4
# Write a function to find the sum of an array without using the built in function:

def my_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

my_sum(1,2,3,4,10)
# %%
#EX5
# Write a function to find the max number in a list

def max_num(*args):
    return max(args)

max_num(50,20,3,-99)
# %%
#EX6
# Write a function that returns factorial of a number
import math

def factoriel(n):
    print(math.factorial(n))

factoriel(5)
# %%
#EX7
# Write a function that counts an element in a list (without using the count method):

def element_count(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count

element_count("barnabe is an alpaga","a")
# %%
#EX8
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

# >>>norm([1,2,2])
# >>>3

import math

def l2_norm(*args):
    return math.sqrt(sum(n**2 for n in args))

l2_norm(3,4)

# %%
#EX9
# Write a function to find if an array is monotonic (sorted either ascending of descending)

def is_monotonic(arr):
    ascending = True
    descending = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            ascending = False

        if arr[i] < arr[i + 1]:
            descending = False

    return ascending or descending

is_monotonic([1,3,0,9])
# %%
#EX10
# Write a function that prints the longest word in a list.

def longest(arr):
    return max(arr, key=len)

longest(['banana','auriane','apple'])
# %%
#EX11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def type_cat(arr):
    text = []
    num = []
    
    for i in arr:
        if isinstance(i, str):
            text.append(i)
        elif isinstance(i, int):
            num.append(i)
    
    return text, num

type_cat(["auriane",8,12,"banana"])
#%%
#EX12
# Write a function to check if a string is a palindrome:

# >>>is_palindrome('radar')
# >>>True

# >>>is_palindrome('John)
# >>>False

def is_palindrome(word):
    return word == word[::-1]


is_palindrome('club')
# %%
# #EX13
# Write a function that returns the amount of words in a sentence with length > k:

# >>>sentence = 'Do or do not there is no try'
# >>>k=2
# >>>sum_over_k(sentence,k)
# >>>3

def sum_over_k(sentence,k):
    count = 0
    for word in sentence.split():
        if len(word) > k:
            count += 1
    return count

sum_over_k("am not ok with it",3)
# %%
#EX14
# Write a function that returns the average value in a dictionary (assume the values are numeric):

# >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
# >>>3

def dict_avg(d):
    if len(d) == 0:
        return 0
    return sum(d.values()) / len(d)

print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))
# %%
#EX15
#Write a function that returns common divisors of 2 numbers:

# >>>common_div(10,20)
# >>>[2,5,10]

def common_div(a, b):
    result = []
    
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            result.append(i)
    
    return result

common_div(10,20)
# %%
#EX16
# Write a function that test if a number is prime:

# >>>is_prime(11)
# >>>True

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

is_prime(12)
# %%
#EX17
