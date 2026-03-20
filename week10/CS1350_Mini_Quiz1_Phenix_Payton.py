## Phenix Payton
## CS 1350
## Mini Quiz
## 3/20/26
import re

text = "Error 42 on server-7"
m1 = re.search(r"\d", text)
print(m1.group()) # Answer: _________________________

m2 = re.search(r"[^a-zA-Z0-9 ]", text)
print(m2.group()) # Answer: _________________________
print(m2.start()) # Answer: _________________________

m3 = re.search(r"\s\w", text)
print(m3.group())


vin = "1HGCM82633A004352"
match = re.search(r"\d", vin)
if match:
    print(f"Digit: {match.group()}, Position: {match.start()}")
    # Expected: Digit: 1, Position: 0
    
raw_input = " SensorID: tX7-alpha "
# Step 1: Use a string method to remove leading/trailing whitespace
cleaned = raw_input.strip() # one string method call
print(cleaned)
# Step 2: Use re.search to find a lowercase letter followed by an uppercase letter followed by a digit (like tX7)
match = re.search(r"[a-z][A-Z]\d", cleaned)
# Replace ___ with your pattern

if match:
    print(f"Sensor tag: {match.group()}")
    # Expected: Sensor tag: tX7
   
plate = "ABC 1234"
# Write a pattern that matches an uppercase letter followed by a digit.
match2 = re.search(r"[A-Z]\d", plate) # Replace ___ with your pattern
# Expected output:
# Found: C1 at position (2, 4)
if match2:
    print(f"Found: {match2.group()} at position {match2.span()}")