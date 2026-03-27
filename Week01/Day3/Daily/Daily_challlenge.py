#%%
#challenge1
# Ask the user for two inputs:
# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

mult = []
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))
i = 1
while i<=length:
    res = i*number
    mult.append(res)
    i += 1
print(mult)

#%%
#challenge2
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

word = input("Enter a word: ")
new = []
for char in word:
    if (len(new)==0)or (char != new[-1]):
        new.append(char)
print("".join(new))
# %%
