#%%
#EX1
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.


my_list = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(', ')
print(f"There are {len(my_list)} companies in the list.")

order_list = sorted(my_list, reverse=True)
total_o = 0
for company in order_list:
    if 'o' in company.lower():
        total_o += 1
print(f"There are {total_o} companies with an 'o' in their name")

total_no_i = 0
for company in order_list:
    if 'i' not in company.lower():
        total_no_i += 1
print(f"There are {total_no_i} companies without an 'i' in their name")

# Bonus: There are a few duplicates in this list:
# ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks 
# (eg. “Acura, Alfa Romeo, Aston Martin, …”),
#  also print out a message saying how many companies are now in the list.


the_list = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
no_duplicate = set(the_list)
clean_list = sorted(no_duplicate)
print(", ".join(clean_list))
print(f"There are now {len(clean_list)} manufacturers in the list")


# Bonus: Print out the list of manufacturers in ascending order (A-Z), 
# but reverse the letters of each manufacturer’s name.


sorted_list = sorted(my_list)

reversed_names = [company[::-1] for company in sorted_list]

print(reversed_names)
# %%
#how to reverse a string
name = "Auriane"
print(name[::-1])
# %%
