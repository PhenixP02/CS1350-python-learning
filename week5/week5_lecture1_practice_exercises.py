#1. Calculate the mean, median, and standard deviation of [23, 45, 67, 32, 56, 78, 43].
import numpy as np
a = np.array([23, 45, 67, 32, 56, 78, 43])
print(a)
print(f"Average: {np.average(a)}")
print(f"Median: {np.median(a)}")
print(f"Standard Deviation: {np.std(a)}")
#2. Find the index of the maximum value in [3, 7, 2, 9, 1, 5].
b = np.array([3, 7, 2, 9, 1, 5])
print(b)
print(f"Index of max: {np.argmax(b)}")
print()


#1. Create a 4×5 matrix of random integers (1-100). Calculate the mean of each row and each column.
c = np.random.randint(1,101, size = 20).reshape(4,5)
print(c)
print(f"Column Average: {np.average(c, axis=0)}")
print(f"Row Average: {np.average(c, axis=1)}")
#2. Given data with np.nan values, calculate the mean ignoring NaN.
data = np.array([1, 2, np.nan, 4, 5])
print(f"Average (ignoring missing data): {np.nanmean(data)}")
print()