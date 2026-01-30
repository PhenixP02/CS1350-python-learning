

import numpy as np


num_array = np.array([10, 20, 30, 40, 50])
print(num_array)
print(type(num_array))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"Array a + Array B: {a + b}")
print(f"Array a + Array B: {a * b}")

print(np.array([1, 2, 3]) + np.array([10])) ## Prediction: [11, 2, 3]  Actual: [11, 12 ,13]
## Numpy uses C for memory efficiency and faster performance




#1. What data type will np.array([1, 2, 3.0]) have?  ## float
test_Array = np.array([1, 2, 3.0])
print(test_Array.dtype)
#2. What does np.array([1, 2, 3]) * 3 produce?  ## 3, 6, 9
print(np.array([1, 2, 3]) * 3)

list = [ 1, 2, 3, 4, 5]
array = np.array([1, 2, 3, 4, 5])
print(list * 2) # appends 1, 2, 3, 4, 5 duplicate elements to list
print(array * 2) # Doubles value of all elements in array

big_array = np.arange(1000000)
print(f"{big_array.nbytes} bytes")




#1. Create a 1D array of 10 zeros.
zeros = np.zeros(10)
print(zeros)
#2. Create a 3×3 matrix filled with the value 5.
matrix_fives = np.full((3, 3), 5)
print(matrix_fives)
#3. Create an array of even numbers from 0 to 20.
array_even = np.arange(0, 21, 2)
print(array_even)

#1. Create a 4×4 identity matrix.
print(np.eye(4))
#2. Create 50 evenly spaced numbers between 0 and 10.
lin_array = np.linspace(0, 10, 50)
print(lin_array)
#3. Create a 2×3 array and print all its attributes.
twobythree = np.full((2, 3), 9)
print(twobythree)
print(twobythree.ndim) # 2 dimensions
print(twobythree.shape) # (2, 3) - 2 rows, 3 columns
print(twobythree.size) # 6 total elements
print(twobythree.dtype) # int64 data type
print(twobythree.itemsize) # 8 bytes per element
print(twobythree.nbytes) # 48 total bytes (6 x 8)