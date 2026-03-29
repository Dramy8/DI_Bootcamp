#%%
#EX1
# You are given two lists. 
# Convert them into a dictionary where the first list contains the keys 
# and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

numbers = {key: value for (key,value) in zip(keys,values)}
print(numbers)

#%%
#EX2
# Write a program that calculates the total cost of movie tickets for a family based on their ages.
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15
# Family Data:
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0
for x,y in family.items(): 
    if y>12:
        price = 15
        total += price
    elif 3<=y<=12:
        price = 10
        total += price
    else:
        price = 0
        total += price
    print(f"The price for {x} is ${price}")
print(f"The total price is ${total}")


# %%
#EX2BONUS
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

family = {}
while True: 
    name = input("Enter the name of the person or stop when you are done: ")
    if name == "stop":
        break
    age =  int(input("Enter the age of the person: "))
    family[name] = age
total = 0
for x,y in family.items(): 
    if y>12:
        price = 15
    elif 3<=y<=12:
        price = 10
    else:
        price = 0
    total += price
    print(f"The price for {x} is ${price}")
print(f"The total price is ${total}")
# %%
# Create and manipulate a dictionary that contains information about the Zara brand.
# Brand Information:
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.


brand = {
    'name':'Zara', 
    'creation_date':1975,
    'creator_name':'Amancio Ortega Gaona',
    'type_of_clothes':['men','women','children','home'],
    'international_competitors': ['Gap','H&M','Benetton'],
    'number_stores': 7000,
    'major_color': {
    'France':'blue', 
    'Spain':'red', 
    'US':['pink','green']
    }
 }

brand['number_stores'] = 2
print('Zara has different sections such as', ','.join(brand['type_of_clothes']))
brand['country_creation'] = 'Spain'
if 'international_competitors' in brand: 
    brand['international_competitors'].append('Desigual')
del brand['creation_date']
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())

# Bonus:
# Create another dictionary called more_on_zara with creation_date and number_stores. 
# Merge this dictionary with the original brand dictionary and print the result.
more_on_zara = {'number_stores': brand['number_stores'],
            'creation_date': '1975'}
brand.update(more_on_zara)


# %%
#EX4
# You are given a list of Disney characters. 
# Create three dictionaries based on different patterns as shown below:
# Character List:
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# Expected Results:
# 1. Create a dictionary that maps characters to their indices:
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# 2. Create a dictionary that maps indices to characters:
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
map1 = {}
for index,name in enumerate(users):
    map1[name] = index
print(map1)

map2 = {}
for index,name in enumerate(users):
    map2[index] = name
print(map2)

map3 = {name: index for name, index in sorted(map1.items(), key=lambda item: item[0])}
for index, name in enumerate(map3):
    map3[name] = index
print(map3)



