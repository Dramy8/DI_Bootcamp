#%%
# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****

for i in range(3):
    print((" "*(2-i))+("*"*((i*2)+1)))
# %%
# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****

for i in range(5):
    print((" "*(4-i))+("*"*(i+1)))
# %%
# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *

for i in range(5):
    print("*"*(i+1))
for i in range(5,-1,-1):
    print((" "*(5-i))+("*"*(i)))
# %%
# Exercise 2
# Instructions
# Analyse this code before executing it. Write some commnts next to each line.
#  Write the value of each variable and their changes, and add the final output.
#  Try to understand the purpose of this program.
my_list = [2, 24, 12, 354, 233]   #we have a list, unordered, of numbers
for i in range(len(my_list) - 1):  # is takes the index 0, 1, 2 and 3, not last one. 
    minimum = i                     #we suppose for now the item of index i is the minimum 
    for j in range( i + 1, len(my_list)):   #j goes over all indexes after i  
        if(my_list[j] < my_list[minimum]):    #comparing value of index j with value we suppose as minimum 
            minimum = j        # if we found smaller, we keep it as new minimum 
            if(minimum != i):     #if the minimum found isn't already at i 
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]   #then we switch both values
print(my_list)



# %%
