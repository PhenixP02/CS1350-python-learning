
#[1, 2, 3, 4] - List, mutable (changeable), can't be hashed
#{1, 2, 3, 4} - Set, mutable, unordered, elements must be immutable, Unique elements only (No dupes), fast in checks
#(1, 2, 3, 4) - Tuple, immutable
#{"d": 0} - Dictionary, mutable 

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat(), Dog()]
for a in animals:
    print(a.speak())
 
 
    
# Abstract Methods - Methods every object of a class must have to be created. A method that must be overridden

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r**2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    
c1 = Circle(5)
print(c1.area())
c2 = Circle(10)
print(c2.area())
r1 = Rectangle(5, 4)
print(r1.area())

#s =Shape() ## TypeError Can't instantiate abstract class Shape without an implementation for abstract method 'area'

# @staticmethod a method that belongs to the class but receives no automatic first argument
class Math:
    @staticmethod
    def add(a, b):
        return a + b

sum1 = Math.add(3, 6)
print(sum1)

# @classmethod — receives cls, the class object
class User:
    def __init__(self, name):
        self.name = name
        
    @classmethod
    def from_username(cls, name):
        return cls(name)   # creates a User

user1 =User.from_username("Phenix")
print(user1.name)

# @property — turns a method into a read‑only attribute
class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    @property
    def area(self):
        return (1/2) * self.b * self.h

t1 = Triangle(2, 4)
print(t1.area)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(1, 2) + Point(3, 4)
print(p)

menu = {"burger": 12, "steak": 25, "salad": 10, "lobster": 40, "soup": 8}
expensive = {item: menu[item] for item in menu if menu[item] > 15 }
print(expensive)


import numpy as np
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[0:2, 1:])
print(np.mean(arr, axis=1))


import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(5), Rectangle(3, 4), Triangle(6, 8)]
total_area = sum(s.area() for s in shapes)

print(total_area)