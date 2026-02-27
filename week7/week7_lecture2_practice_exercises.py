class Pet:
    count = 0

    def __init__(self, name):
        self.name = name
        Pet.count += 1

    @classmethod
    def get_count(cls):
        # TODO: Return count
        return Pet.count

#Test:
Pet("Buddy"); Pet("Luna"); Pet("Max")
print(Pet.get_count()) # 3


class Student:
    all_students = []

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.all_students.append(self)
        # TODO: Append self to all_students

    @classmethod
    def honor_roll(cls):
        return [student for student in cls.all_students if student.gpa >= 3.5]

# Test:
Student("Alice", 3.8); Student("Bob", 3.2); Student("Carol", 3.9)
for s in Student.honor_roll():
    print(s.name) # Alice, Carol



class TextUtils:
    @staticmethod
    def word_count(text):
        # TODO: Return number of words
        return len(text.split())

    @staticmethod
    def is_palindrome(text):
        # TODO: Ignore case and spaces, check if palindrome
        cleaned_text = text.replace(" ", "").lower()
        if cleaned_text == cleaned_text[::-1]:
            return True
        return False

    @staticmethod
    def caesar_cipher(text, shift):
        # TODO: Shift each letter by shift, wrap around
        # Only shift a-z and A-Z, leave other characters unchanged
        pass

print(TextUtils.word_count("Hello World"))
print(TextUtils.is_palindrome("race car"))



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def from_csv_row(cls, row):
        # TODO: Split row by comma, convert types, return cls(...)
        parts = row.split(",")
        return cls(parts[0], float(parts[1]), int(parts[2]))
    
    @classmethod
    def from_dict(cls, data):
        """Create from dictionary"""
        return cls(data["name"], data["price"], data["quantity"])

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} x {self.quantity}"

# Test:
p2 = Product.from_csv_row("Mouse,29.99,50")
print(p2)