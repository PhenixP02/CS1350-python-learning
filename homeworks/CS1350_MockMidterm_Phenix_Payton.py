## Phenix Payton
## CS1350
## Mock Midterm
## 3/6/26

"""Problem 1: Word Frequency Analyzer (Dictionaries)"""
print("Problem 1:")
def analyze_text(text):
    """
    Analyze word frequencies in text.
    Args:
        text: a string of words (may contain punctuation)
    Returns:
        dict with keys "word_counts", "most_common", "unique_count"
    """

    text_statistics = {} # Dictionary of stats to be returned (word_counts, most_common, unique_count)
## Normalize text (Lowercase, remove punctuation, Split into words)
    import string
    normal_text = text.lower()
    for p in string.punctuation:
        normal_text = normal_text.replace(p, "")
    words = normal_text.split()
    


## Word Counter   
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1 # Access/Create entry in dict for each word and increment count by 1
    text_statistics["word_counts"] = word_counts  # Add to text stats dict to be returned


## Most Common Word
    highest_count = max(word_counts.values())
    for word in word_counts:
        if word_counts[word] == highest_count:
            most_common = word
    text_statistics["most_common"] = most_common
    
## Unique Count
    unique_count = 0
    for word in word_counts:
        if word_counts[word] == 1:
            unique_count += 1
    text_statistics["unique_count"] = unique_count
    
    return text_statistics
    
# Test cases
sample = "The cat sat on the mat. The cat liked the mat!"
result = analyze_text(sample)
print(result["word_counts"])

# {'the': 4, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 2, 'liked': 1}
print(result["most_common"])
# the
print(result["unique_count"])
# 3
print()


"""Problem 2: Student Roster with Sets (Sets)"""
print("Problem 2:")
class Roster:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = set()
        
    def enroll(self, name):
        self.students.add(name)
    
    def drop(self, name):
        self.students.discard(name)  # Discard to avoid errors
    
    def is_enrolled(self, name):
        return name in self.students

def common_students(roster1, roster2):
    common_students = roster1.students & roster2.students
    return common_students

def exclusive_students(roster1, roster2):
    exclusive_students = roster1.students ^ roster2.students
    return exclusive_students

def print_report(rosters):
    # Students enrolled in ALL courses
    if rosters:
        all_students = set.intersection(*(course.students for course in rosters))
    else:
        all_students = set()

    # Print each course
    for course in rosters:
        print(f"{course.course_name}: {len(course.students)} students")
        print(f"  {course.students}")

    print("\nStudents enrolled in ALL courses:")
    print(all_students)

# Test cases
cs101 = Roster("CS 101")
for name in ["Alice", "Bob", "Carol", "Dave"]:
    cs101.enroll(name)
    
cs201 = Roster("CS 201")
for name in ["Carol", "Dave", "Eve", "Frank"]:
    cs201.enroll(name)

cs301 = Roster("CS 301")
for name in ["Dave", "Eve", "Grace"]:
    cs301.enroll(name)

print(common_students(cs101, cs201))
# {'Carol', 'Dave'}
print(exclusive_students(cs101, cs201))
# {'Alice', 'Bob', 'Eve', 'Frank'}
print_report([cs101, cs201, cs301])
# CS 101: 4 students
# CS 201: 4 students
# CS 301: 3 students
# Enrolled in all courses: {'Dave'}
print()


"""Problem 3: Grade Statistics with NumPy (NumPy)"""
print("Problem 3:")
import numpy as np

def grade_report(grades_2d):
    """
    Compute grade statistics from a 2D array (students x assignments).
    
    Args:
        grades_2d: numpy 2D array, shape (num_students, num_assignments)
    
    Returns:
        dict with keys listed above
    """
    # 1. Student averages (mean across columns)
    student_averages = grades_2d.mean(axis=1)

    # 2. Assignment averages (mean across rows)
    assignment_averages = grades_2d.mean(axis=0)

    # 3. Highest student index
    highest_student = np.argmax(student_averages)

    # 4. Curved grades
    max_avg = student_averages.max()
    curved_grades = grades_2d * (100 / max_avg)

    # 5. Passing boolean array
    passing = grades_2d >= 60

    return {
        "student_averages": student_averages,
        "assignment_averages": assignment_averages,
        "highest_student": highest_student,
        "curved_grades": np.round(curved_grades, 2),
        "passing": passing
    }

# Test cases
grades = np.array([
[85, 90, 78, 92], # Student 0
[70, 65, 80, 75], # Student 1
[95, 88, 92, 97], # Student 2
[60, 72, 68, 55] # Student 3
])

report = grade_report(grades)
print("Student averages:", report["student_averages"])
# [86.25 72.5 93. 63.75]
print("Assignment averages:", report["assignment_averages"])
# [77.5 78.75 79.5 79.75]
print("Highest student index:", report["highest_student"])
# 2
print("Curved grades (Student 0):", report["curved_grades"][0])
# [91.40 96.77 83.87 98.92] (approximately)
print("Passing (Student 3):", report["passing"][3])
# [ True True True False]
print()


"""Problem 4: Vehicle Hierarchy with Polymorphism (OOP — Inheritance & Polymorphism)"""
print("Problem 4:")
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    @abstractmethod
    def fuel_cost(self, distance):
        pass
    
    def info(self):
        return f"{self.year} {self.make} {self.model}"
    
    @staticmethod
    def validate_year(year):
        return 1900 <= year <= 2026

class GasCar(Vehicle):
    def __init__(self, make, model, year, mpg, gas_price=3.50):
        super().__init__(make, model, year)
        self.mpg = mpg
        self.gas_price = gas_price
    
    def fuel_cost(self, distance):
        return (distance / self.mpg) * self.gas_price

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, kwh_per_mile, electricity_price=.13):
        super().__init__(make, model, year)
        self.kwh_per_mile = kwh_per_mile
        self.electricity_price = electricity_price
    
    def fuel_cost(self, distance):
        return distance * self.kwh_per_mile * self.electricity_price

class HybridCar(GasCar):
    def __init__(self, make, model, year, mpg, gas_price=3.5, electric_fraction=.4):
        super().__init__(make, model, year, mpg, gas_price)
        self.electric_fraction = electric_fraction
    
    def fuel_cost(self, distance):
        return super().fuel_cost(distance) * (1 - self.electric_fraction)

def trip_cost(vehicles, distance):
    cheapest_vehicle = None
    cheapest_cost = float('inf')
    
    for v in vehicles:
        cost = v.fuel_cost(distance)
        print(f"{v.info()}: ${cost:.2f}")

        if cost < cheapest_cost:
            cheapest_cost = cost
            cheapest_vehicle = v
    print(f"\nCheapest: {cheapest_vehicle.info()} at ${cheapest_cost:.2f}")    

# Test cases
cars = [
    GasCar("Toyota", "Camry", 2024, mpg=32),
    ElectricCar("Tesla", "Model 3", 2025, kwh_per_mile=0.25),
    HybridCar("Toyota", "Prius", 2024, mpg=50, electric_fraction=0.4)
]
trip_cost(cars, 300)

# 2024 Toyota Camry: $32.81
# 2025 Tesla Model 3: $9.75
# 2024 Toyota Prius: $12.60
# Cheapest: 2025 Tesla Model 3
print()


"""Problem 5: Smart Wallet with Operator Overloading (OOP — Magic Methods)"""
print("Problem 5:")

class Wallet:
    def __init__(self, owner):
        self.owner = owner
        self.balances = {}
    
    def __getitem__(self, currency):
        return self.balances.get(currency, 0.0)
    
    def __setitem__(self, currency, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balances[currency] = amount
    
    def __contains__(self, currency):
        return currency in self.balances

    def __len__(self):
        return sum(1 for amount in self.balances.values() if amount > 0)
    
    def __iter__(self):
        return iter(self.balances.keys())
    
    def __str__(self):
        return f"{self.owner}'s Wallet ({len(self)} currencies)"
    
    def __repr__(self):
        return f"Wallet('{self.owner}')"
    
    def __add__(self, other):
        new_owner = f"{self.owner} & {other.owner}"
        new_wallet = Wallet(new_owner)
        
        for c, amt in self.balances.items():
            new_wallet[c] = amt
        
        for c, amt in other.balances.items():
            new_wallet[c] += amt
        
        return new_wallet
    
    def __mul__(self, factor):
        new_wallet = Wallet(self.owner)
        for c, amt in self.balances.items():
            new_wallet[c] = amt * factor
        return new_wallet
    
    def total(self): 
        return sum(self.balances.values()) ## Sum of all amounts regardless of currency
    
    def __eq__(self, other):
        return self.total() == other.total()
    
    def __lt__(self, other):
        return self.total() < other.total()
    

# Test cases
w1 = Wallet("Alice")
w1["USD"] = 100.0
w1["EUR"] = 50.0

w2 = Wallet("Bob")
w2["USD"] = 75.0
w2["GBP"] = 30.0

print(w1) # Alice's Wallet (2 currencies)
print(repr(w1)) # Wallet('Alice')
print(w1["USD"]) # 100.0
print(w1["JPY"]) # 0
print("EUR" in w1) # True
print(len(w1)) # 2
print()

# Arithmetic
w3 = w1 + w2
print(w3) # Alice & Bob's Wallet (3 currencies)
print(w3["USD"]) # 175.0
print(w3["EUR"]) # 50.0
print(w3["GBP"]) # 30.0


w4 = w1 * 2
print(w4["USD"]) # 200.0
print(w4["EUR"]) # 100.0
print()

# Comparison (by total value)
print(w1 == w2) # False (150 vs 105)
print(w2 < w1) # True (105 < 150)
print()

# Iteration
for currency in w1:
    print(f" {currency}: {w1[currency]}")
print()
    
# Validation
try:
    w1["USD"] = -10
except ValueError as e:
    print(f"Caught: {e}")    