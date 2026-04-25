#%%
# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.

# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.

# Test your implementation by creating several circles and printing comparisons, additions, and sorted results.

import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter/2
        else:
            raise ValueError("You must provide radius or diameter")
        
    @property
    def diameter(self):
        return self.radius*2

    @property
    def area(self):
        return math.pi*(self.radius)**2
    
    def __repr__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area})"
    
    def __add__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("You can only add another Circle")

        new_radius = self.radius + other.radius
        return Circle(new_radius)
    
    def __gt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("You can only compare with another Circle")
        return self.radius > other.radius
        
    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("You can only compare with another Circle")
        return self.radius == other.radius
        
    
    def __lt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("You can only compare with another Circle")
        return self.radius < other.radius
      

c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=2)

print(c1)
print(c1.diameter)
print(c1.area)

print(c1 == c2)
print(c1 > c3)

c4 = c1 + c3
print(c4)

circles = [c1, c2, c3, c4]
sorted_circles = sorted(circles)
print(sorted_circles)


# %%
