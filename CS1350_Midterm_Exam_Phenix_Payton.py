##Phenix Payton
##CS1350
##Midterm Exam
##3/6/26

"""Problem 2: Event Planner with sets (COMPLETE)"""
print("Problem 2:")
class Event:
    def __init__(self, event):
        self.event = event
        self.volunteers = set()
    def add_volunteer(self, name):
        self.volunteers.add(name)
    def remove_volunteer(self, name):
        self.volunteers.discard(name)
    def volunteer_count(self):
        return len(self.volunteers)

def find_overcommitted(events, max_events):
    counts = {}
    over_commited = set()
    for e in events:
        for volunteer in e.volunteers:
            counts[volunteer] = counts.get(volunteer, 0) + 1
            if counts[volunteer] > max_events:
                over_commited.add(volunteer)
    return over_commited

def find_available(all_volunteers, events):
    assigned = set()
    for e in events:
        assigned |= e.volunteers
        
    return set(all_volunteers) - assigned

def schedule_conflict(event1, event2):
    event1_staff = set(event1.volunteers)
    event2_staff = set(event2.volunteers)
    conflicted = event1_staff & event2_staff
    return conflicted

# Test cases
setup = Event("Setup")
for v in ["Alice", "Bob", "Carol", "Dave"]:
    setup.add_volunteer(v)
    
ceremony = Event("Ceremony")
for v in ["Carol", "Dave", "Eve", "Frank"]:
    ceremony.add_volunteer(v)

cleanup = Event("Cleanup")
for v in ["Alice", "Dave", "Frank", "Grace"]:
    cleanup.add_volunteer(v)

print(f"Setup: {setup.volunteer_count()} volunteers") # 4
print(f"Ceremony: {ceremony.volunteer_count()} volunteers") # 4

# Conflicts
print(f"Conflicted volunteers: {schedule_conflict(setup, ceremony)}") # {'Carol', 'Dave'}

# Overcommitted (signed up for more than 2 events)
events = [setup, ceremony, cleanup]
print(f"Overcommitted volunteers: {find_overcommitted(events, 2)}") # {'Dave'}

# Available (not signed up for anything)
everyone = {"Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Hank"}
print(f"Available volunteers: {find_available(everyone, events)}") # {'Hank'}   
print()   
        
    
    
"""Problem 3: Weather Data Analysis (COMPLETE)"""
print("Problem 3:")
import numpy as np

def weather_analysis(temps_2d):
    """
    Analyze weekly temperature data for multiple cities.
    
    Args:
        temps_2d: numpy 2D array, shape (num_cities, 7)
    
    Returns:
        dict with keys listed above
    """
# YOUR CODE HERE
    city_averages = temps_2d.mean(axis=1)
    
    daily_averages = temps_2d.mean(axis=0)
    
    hottest_day = np.argmax(daily_averages)
    
    coldest_city = np.argmin(city_averages)
    
    above_80 = temps_2d > 80
    
    means = temps_2d.mean(axis=1, keepdims=True)
    normalized = np.round(temps_2d - means)
    
    return {
        "city_averages": np.round(city_averages, 2),
        "daily_averages": np.round(daily_averages, 2),
        "hottest_day": hottest_day,
        "coldest_city": coldest_city,
        "above_80": above_80,
        "normalized": normalized
    }

# Test cases
temps = np.array([
[72, 75, 78, 82, 85, 80, 74], # City 0 (moderate)
[88, 91, 93, 95, 90, 87, 85], # City 1 (hot)
[55, 58, 60, 62, 59, 56, 53], # City 2 (cool)
])

report = weather_analysis(temps)
print("City averages:", report["city_averages"])
# [78. 89.86 57.57] (approximately)
print("Daily averages:", report["daily_averages"])
# [71.67 74.67 77. 79.67 78. 74.33 70.67] (approximately)
print("Hottest day index:", report["hottest_day"])
# 3
print("Coldest city index:", report["coldest_city"])
# 2
print("Above 80 (City 0):", report["above_80"][0])
# [False False False True True False False]
print("Normalized (City 2):", np.round(report["normalized"][2], 2)) ##Unsure what is meant by Normalize
# [0.22 0.56 0.78 1. 0.67 0.33 0. ]
print()


"""Problem 4: (COMPLETE)"""
print("Problem 4:")
from abc import ABC, abstractmethod

class Product(ABC):
        def __init__(self, name, base_price):
            self.name = name
            self.base_price = base_price
        
        @abstractmethod
        def final_price(self):
            pass
        
        def label(self):
            return f"{self.name} - ${self.final_price()}"
        
        @staticmethod
        def validate_price(price):
            if price <= 0:
                raise ValueError("Price must be greater than 0!")

class DigitalProduct(Product):
    def __init__(self, name, base_price, discount_pct=0.0):
        if discount_pct > 1.0:
            self.discount_pct = 1.0
        else:
            self.discount_pct = discount_pct
        super().__init__(name, base_price)
        
    def final_price(self):
        return round(self.base_price * (1 - self.discount_pct), 2)

class PhysicalProduct(Product):
    def __init__(self, name, base_price, weight_lbs, shipping_rate=.50):
        super().__init__(name, base_price)
        self.weight_lbs = weight_lbs
        self.shipping_rate = shipping_rate
        
    def final_price(self):
        return round(self.base_price + (self.weight_lbs * self.shipping_rate), 2)

class SubscriptionProduct(Product):
    def __init__(self, name, base_price, months, monthly_discount=.10):
        super().__init__(name, base_price)
        self.months = months
        self.monthly_discount = monthly_discount
        
    def final_price(self):
        return round(self.base_price * self.months * (1 - self.monthly_discount * (self.months - 1) / self.months), 2)
    
def checkout(cart):
    cart_total = 0
    for c in cart:
        print(f"{c.label()}")
        cart_total += c.final_price()
    print(f"Cart total: ${cart_total}")
    return f"Cart total: ${cart_total}"

# Test cases
cart = [
DigitalProduct("E-book: Python 101", 29.99, discount_pct=0.20),
PhysicalProduct("Mechanical Keyboard", 89.99, weight_lbs=2.5),
SubscriptionProduct("Cloud Storage", 9.99, months=12),
]

total = checkout(cart)
# E-book: Python 101 — $24.00  ## My Output off by one penny
# Mechanical Keyboard — $91.24
# Cloud Storage — $109.09 ## My Output off by 10 cents
# Total: $224.33  ## Unsure where Error occurs, Something with disocunt