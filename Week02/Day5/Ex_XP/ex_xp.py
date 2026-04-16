#%%
#EX1
# Use the provided Cat class to create three cat objects. 
# Then, create a function to find the oldest cat and print its details.

# Step 1: Create Cat Objects
# Use the Cat class to create three cat objects with different names and ages.

# Step 2: Create a Function to Find the Oldest Cat
# Create a function that takes the three cat objects as input.
# Inside the function, compare the ages of the cats to find the oldest one.
# Return the oldest cat object.

# Step 3: Print the Oldest Cat’s Details
# Call the function to get the oldest cat.
# Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
# Replace <cat_name> and <cat_age> with the oldest cat’s name and age.


class Cat():
     def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

Cat1 = Cat("Lady",3)
Cat2 = Cat("Berlioz",4)
Cat3 = Cat("Toulouse",5)

def find_oldest(cat1, cat2, cat3):
    return max(cat1, cat2, cat3, key=lambda cat: cat.age)

oldest_cat = find_oldest(Cat1, Cat2, Cat3)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old")
# %%
#EX2
# Create a Dog class with methods for barking and jumping. Instantiate dog objects, 
# call their methods, and compare their sizes.

# Step 1: Create the Dog Class
# Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.

# Step 2: Create Dog Objects
# Create davids_dog and sarahs_dog objects with their respective names and heights.

# Step 3: Print Dog Details and Call Methods
# Print the name and height of each dog.
# Call the bark() and jump() methods for each dog.

# Step 4: Compare Dog Sizes


class Dog():
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height*2
        print(f"{self.name} jumps {x} cm high!")

davids_dog = Dog("Balto",25)
sarahs_dog = Dog("Shailo",20)

print(f"{davids_dog.name}, {davids_dog.height} cm.")
print(f"{sarahs_dog.name}, {sarahs_dog.height} cm.")
davids_dog.bark()
sarahs_dog.bark()
davids_dog.jump()
sarahs_dog.jump()

biggest = max([davids_dog, sarahs_dog], key=lambda dog: dog.height)
print(f"The tallest dog is {biggest.name}")

# %%
#EX3
# Instructions:
# Create a Song class with a method to print song lyrics line by line.
# Step 1: Create the Song Class
# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
# Example:
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", 
# "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
# Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven

class Song():
    def __init__(self,song_lyrics):
        self.lyrics = song_lyrics


    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

stairway.sing_me_a_song()

#%%
#EX4
# Instructions
# Step 1: Define the Zoo Class
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:
# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.
# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.
# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.
# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.
# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.
# Example output:
# {
#    'B': ['Baboon', 'Bear'],
#    'C': ['Cat', 'Cougar'],
#    'G': ['Giraffe'],
#    'L': ['Lion'],
#    'Z': ['Zebra']
# }
# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals().
# Example output:
# B: ['Baboon', 'Bear']
# C: ['Cat', 'Cougar']
# G: ['Giraffe']
# ...

# Step 2: Create a Zoo Object
# Create an instance of the Zoo class and pass a name for the zoo.
# Step 3: Call the Zoo Methods
# Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.
# Bonus: Modify the add_animal() method to get *args so you dont need to repeat the method each time
#  for a new animal, you can pass multiple animals names separated by a comma.

class Zoo():
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self.grouped = {}

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        self.grouped = {}

        for animal in self.animals:
            first_letter = animal[0]

            if first_letter not in self.grouped:
                self.grouped[first_letter] = []

            self.grouped[first_letter].append(animal)

    def get_groups(self):
        for letter, animals in self.grouped.items():
            print(f"{letter}: {animals}")


zoo_A = Zoo("Petpark")

zoo_A.add_animal("Giraffe")
zoo_A.add_animal("Bear")
zoo_A.add_animal("Baboon")

zoo_A.get_animals()

zoo_A.sell_animal("Bear")
zoo_A.get_animals()

zoo_A.sort_animals()
zoo_A.get_groups()
# %%
