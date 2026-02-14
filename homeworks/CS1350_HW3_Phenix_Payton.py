## Phenix Payton
## CS 1350
## Homework 3
## 2/13/26


"""Problem 1: Array Creation and Basic Operations"""
print()
print("Problem 1: Array Creation and Basic Operations")
print()
print("Part A")
# PART A
#1. zeros_arr: A 1D array of 8 zeros
#2. ones_matrix: A 3×4 matrix of ones
#3. range_arr: Numbers from 10 to 50 (inclusive) with step 5: [10, 15, 20, ..., 50]
#4. linear_arr: 9 evenly spaced numbers from 0 to 2 (inclusive)
import numpy as np
print(np.zeros(8))
print(np.ones((3, 4)))
print(np.arange(10, 51, 5))
print(np.linspace(0, 2, 9))
print()


print("Part B")
# PART B
#Calculate and print:
#1. a + b
#2. a * b
#3. a ** 2 (each element squared)
#4. a / b
#5. The sum of all elements in a
#6. The mean of all elements in b
a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 2, 3, 4, 5])

print(a + b)
print(a * b)
print(a ** 2)
print(a / b)
print(np.sum(a))
print(np.average(b))
print()



"""Problem 2: Array Attributes and Statistics"""
print("Problem 2: Array Attributes and Statistics")
print("Part A")
# PART A
#Create a 4×5 matrix containing integers 1-20, then print:
#1. The array itself
#2. Its shape
#3. Number of dimensions
#4. Total number of elements
#5. Data type
#6. Total bytes used
prob2_array = np.arange(1,21).reshape(4,5) ## Create array then reshape it
print(prob2_array)
print(f"Shape: {prob2_array.shape}") # Shape
print(f"Dimensions: {prob2_array.ndim}") # Number of dimensions
print(f"Total Elements: {prob2_array.size}") # Total elements
print(f"Data Type: {prob2_array.dtype}") # Data type
print(f"Total bytes: {prob2_array.nbytes}") # Total bytes
print()

print("Part B")
# PART B
#Using the same matrix, calculate and print:
#1. Overall mean
#2. Overall standard deviation
#3. Minimum and maximum values
#4. Sum of each row (should give 5 values)  ### 4 VALUES NOT 5
#5. Mean of each column (should give 4 values)  ### 5 VALUES NOT 4
#6. Index of the maximum value in the flattened array
print(f"Matrix Avergae : {np.average(prob2_array)}")
print(f"Standard Deviation: {np.std(prob2_array)}")
print(f"Minimum: {np.min(prob2_array)}")
print(f"Maximum: {np.max(prob2_array)}")
print(f"Sum of rows: {np.sum(prob2_array, axis=1)}")
print(f"Average of each column: {np.average(prob2_array, axis=0)}")
print(f"Index of max value: {np.argmax(prob2_array)}")
print()



"""Problem 3: Indexing and Boolean Selection"""
print("Problem 3: Indexing and Boolean Selection")
print()
# Student scores: 6 students, 4 exams
scores = np.array([
[85, 90, 78, 92], # Alice
[70, 65, 72, 68], # Bob
[95, 98, 94, 97], # Carol
[60, 55, 58, 62], # Dave
[88, 85, 90, 87], # Eve
[75, 80, 77, 82] # Frank
])
students = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']
exams = ['Exam1', 'Exam2', 'Exam3', 'Exam4']
print("Part A: Basic Indexing")
# PART A
#Extract and print:
#1. Carol's Exam2 score (single value)
print(f"Carol's Exam2 score: {scores[2, 1]}")
#2. All of Alice's scores (first row)
print(f"All of Alice's scores: {scores[0]}")
#3. All Exam3 scores (third column)
print(f"All Exam 3 scores: {scores[:, 2]}")
#4. A 2×2 submatrix: Bob and Carol's scores on Exam1 and Exam2
print(f"Bob & Carol Exam 1 & 2 scores: {scores[1:3, 0:2]}")
print()

print("Part B: Boolean Selection")
# PART B
#1. Create a boolean mask for all scores >= 90
ge_90= scores >= 90
print(ge_90)
#2. Print all scores that are >= 90
print(f"All scores 90 or above: {scores[ge_90]}")
#3. Count how many scores are >= 90
print(f"Scores above 90 count: {len(scores[ge_90])}")
#4. Find which students have an average score >= 85 (print their names)
print("Students with average test score >= 85: ", end="")
for x in range(0, len(students)):
    if np.average(scores[x, :]) >= 85:
        print(students[x], end=", ")
#5. Replace all failing scores (< 60) with 60 (minimum passing grade). Print the modified array.
scores[scores < 60] = 60
print(f"New array (failing grades bumped to minimum passing): {scores}")
print()



print("Problem 4: Reshaping and Broadcasting")
print()
print("Part A: Reshaping")
# PART A
#1. Create a 1D array with values 1-24
array = np.arange(1, 25)
print(array)
print()
#2. Reshape it to a 4×6 matrix
print()
reshaped_array = array.reshape(4, 6)
print(reshaped_array)
#3. Reshape it to a 2×3×4 3D array
print()
reshaped_array3d = array.reshape(2, 3, 4)
print(reshaped_array3d)
#4. Flatten the 3D array back to 1D
print()
flatted_array = reshaped_array3d.flatten()
print(flatted_array)
print()


print("Part B: Broadcasting")
## PART B
# Rows: products (Apple, Banana, Orange)
# Columns: stores (Store1, Store2, Store3, Store4)
prices = np.array([
[1.20, 1.50, 1.30, 1.40], # Apple
[0.50, 0.60, 0.55, 0.45], # Banana
[0.80, 0.90, 0.85, 0.75] # Orange
])
print(f"Original Prices:\n {prices}")
#1. Apply a 10% discount to ALL prices (multiply by 0.9)
prices *= .90
print(f"After 10% discount:\n {np.round(prices, 2)}")
#2. Add a $0.10 delivery fee to each store (add [0.10, 0.10, 0.10, 0.10] to each row)
prices += .10 
print(f"After 10 cent delivery fee:\n {np.round(prices, 2)}")
#3. The stores have different tax rates: [0.08, 0.06, 0.07, 0.05]. Calculate the final price with tax for each product in each store.
prices *= [1.08, 1.06, 1.07, 1.05]
print(f"After store tax rates:\n {np.round(prices, 2)}")
#4. Normalize prices by subtracting each product's mean price (center the data by row)
means = prices.mean(axis=1, keepdims=True) ## Keepdims=True to keep shape so broadcasting works cleanly
normalized_prices = np.round(prices - means, 2)
print(f"Normalized Prices:\n {normalized_prices}")