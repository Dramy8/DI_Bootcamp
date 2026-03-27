
#%%
# #Accept a number from the user and print its multiplication table

number = int(input("Enter a number: "))
table = range(1,11)
for t in table:
    print(f"{number} x {t} = {number*t}") 

# %%
#Print the numbers from 1 to 10 using while loop

i = 1
while i < 11:
    print(i)
    i += 1

#%%

user = input("Enter the username: ")
code = input("Enter the password: ")
password = len(code)
passe = "*" * password
print(f"{user}, your password {passe} is {password} letters long")


