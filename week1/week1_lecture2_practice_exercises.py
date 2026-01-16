

"""Part 1 Exercises"""
# a) "student_name" # Valid (reason: Immuatable)
# b) [1, 2, 3] # Invalid (reason: Mutable)
# c) 100 # Valid (reason: Immutable)
# d) ("x", "y") # Valid (reason: Immutable)
# e) {"a": 1} # Invalid (reason: Mutable)
# f) frozenset({1,2}) # Valid (reason: Immutable)

locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"} ## Changed to tuples from list
print(locations[(40.7, -74.0)])
print(locations[(34.0, -118.2)])

data = {"a": 1, "b": 2, "a": 3, "b": 4} 
print(data) # "a": 3 "b": 4
print(len(data)) #2

print(hash("Phenix"))
print(hash(100))



"""Part 2 Exercises"""
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(temps.keys())
print(temps.values())
print(f"Days in Dictionary: {len(temps)}")

max_temp = max(temps.values())
print(max_temp)
min_temp = min(temps.values())
print(min_temp)

print("Friday is in Dictionary") if "Friday" in temps else print("Friday not in Dictionary")

if "Thursday" not in temps:
    temps.setdefault("Thursday", 70)
    print(temps)

print(f"Before Keys change: {temps.keys()}")
temps.update({"Friday": 73})
print(f"After Keys change: {temps.keys()}")



"""Part 3 Exercises"""
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for fruit, color in colors.items():
    print(f"The {fruit} is {color}")
    
# Without running the code, predict what list(colors.items()) returns
# [apple, red, banana, yellow....]
print(list(colors.items())) #ACTUAL: [('apple', 'red'), ('banana', 'yellow')...]

prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
above_4_count = 0
for item, price in prices.items():
    price_wtax = price + (price * .10)
    print(f"{item} costs ${price_wtax} with tax")
    if price > 4.00:
        above_4_count += 1
print(f"Items above $4.00: {above_4_count}")

x = 10
y = 20
print(f"Pre swap x = {x} y = {y}")
x, y = y, x
print(f"Post swap x = {x} y = {y}")

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)
print(middle)
print(last)