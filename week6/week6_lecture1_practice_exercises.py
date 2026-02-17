class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        # Return the private age
        return self._age
        pass
    
    def set_age(self, new_age):
    # Only allow ages between 0 and 150
    # Print an error message if invalid
        if new_age > 150 or new_age < 0:
           print("Error: Age must be 0-150!")
           pass
        else:
            self._age = new_age
            print(f"New age: {self._age}")
        

#Test:
person = Person("Bob", 25)
print(person.get_age()) # Should print 25
person.set_age(30) # Should work
person.set_age(-5) # Should print error
print()



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    @property
    def area(self):
        # Calculate and return width * height
        return self.width * self.height
    
    @property
    def perimeter(self):
        # Calculate and return 2 * (width + height)
        return 2 * (self.width + self.height)
        
    
# Test:
rect = Rectangle(5, 3)
print(rect.area) # 15 (no parentheses!)
print(rect.perimeter) # 16 (no parentheses!)