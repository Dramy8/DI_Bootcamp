# Part 1 : Quizz :
# Answer the following questions
# # What is a class?
# What is an instance?
# What is encapsulation?
# What is abstraction?
# What is inheritance?
# What is multiple inheritance?
# What is polymorphism?
# What is method resolution order or MRO?

#My answers : 

# 1. What is a class?

# A class is a blueprint or template used to create objects. 
# It defines the attributes (data) and methods (functions) that the objects created from it will have.

# 2. What is an instance?

# An instance is a specific object created from a class. 
#     Each instance contains its own data while sharing the structure and behavior defined by the class.

# 3. What is encapsulation?

# Encapsulation is the concept of bundling data and methods that operate on that data within a single class, 
# and restricting direct access to some of the object’s internal components to protect its integrity.

# 4. What is abstraction?

# Abstraction is the process of hiding complex implementation details 
# and exposing only the necessary features of an object. 
# It allows the user to interact with an object without needing to understand how it works internally.

# 5. What is inheritance?

# Inheritance is a mechanism that allows a class to inherit attributes and methods from another class, 
# promoting code reuse and hierarchical relationships between classes.

# 6. What is multiple inheritance?

# Multiple inheritance is a feature where a class can inherit attributes and methods 
# from more than one parent class.

# 7. What is polymorphism?

# Polymorphism is the ability of different classes to respond to the same method name in different ways.
# It allows objects of different classes to be treated 
# as instances of the same class through a common interface.

# 8. What is Method Resolution Order (MRO)?

# Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes, 
# especially in cases of inheritance. 
# It determines which method is executed when multiple classes define the same method.

# Part 2: Create a deck of cards class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) 
# and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards 
# and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. 
# After a card is dealt, it should be removed from the deck.
import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts','Diamonds','Clubs','Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        for s in suits:
            for v in values:
                self.cards.append(Card(s, v))

    def shuffle(self):
            random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            return None
        return self.cards.pop()



deck = Deck()
deck.shuffle()
card = deck.deal()
print(card)