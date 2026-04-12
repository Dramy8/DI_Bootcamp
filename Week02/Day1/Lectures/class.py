def calculate(var1,var2):
    return var1+var2, var1-var2

print(calculate(3,4))

#%%
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filtered = filter(lambda s: len(s) <= 4, people)
greetings = map(lambda name: f"Hello {name}", filtered)

for g in greetings:
    print(g)
# %%
for i in range(11):
    print(i) 
# %%
nbr = int(input("enter a number: "))
if nbr%2==0:
    print("this number is even")
else:
    print("this number is odd")
# %%
def some(mylist):
    total = 0 
    for nombre in mylist:
        total += nombre
    return total  

print(some([1,7,7]))
# %%
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
# Using map and filter, try to say hello to everyone who's name 
# is less than or equal to 4 letters

filtered = filter(lambda name: len(name) <= 4, people)
hello = map(lambda name: f"Hello {name}", filtered)

print(list(hello))