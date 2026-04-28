## Phenix Payton
## CS 1350
## Homework 9
## 4/26/26

# Exercise 2.1
print("# Exercise 2.1")
def sum_natural(n):
    """
    Calculate sum of natural numbers from 1 to n recursively.
    Example: sum_natural(5) = 1 + 2 + 3 + 4 + 5 = 15
    """

    # TODO: Implement this
    # Hint: What's the base case? When n = 0 or n = 1?
    # Hint: How can you express sum(n) in terms of sum(n-1)?
    if n == 0:
        return 0
    
    return n + sum_natural(n - 1)

# Test cases:
print(sum_natural(5)) # should return 15
print(sum_natural(10)) # should return 55
print(sum_natural(1)) # should return 1
print()


# Exercise 2.2
print("# Exercise 2.2")
def count_digits(n):
    """
    Count the number of digits in n recursively.
    Example: count_digits(1234) = 4
    Example: count_digits(7) = 1
    """

    # TODO: Implement this
    # Hint: How many digits does n // 10 have?
    # Hint: What's the base case? Single digit number?
    if n < 10:
        return 1
    
    return 1 + count_digits(n // 10)
# Test cases:
print(count_digits(1234)) # should return 4
print(count_digits(987654321)) # should return 9
print(count_digits(5)) # should return 1
print()


## Exercise 2.3
print("Exercise 2.3")
def is_palindrome(s):
    """
    Check if string s is a palindrome recursively.
    Ignore case and consider only alphanumeric characters.
    Example: is_palindrome("A man a plan a canal Panama") = True
    Example: is_palindrome("race a car") = False
    """
    # TODO: Implement this
    # Hint: Compare first and last characters
    # Hint: What happens to the middle?
    # Hint: What are the base cases? (empty string, single char)
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

# Test cases:
print(is_palindrome("racecar")) # should return True
print(is_palindrome("hello")) # should return False
print(is_palindrome("a")) # should return True
print()


# Exercise 4.1
print("Exercise 4.1")
def power(x, n):
    """
    Calculate x raised to the power n recursively.
    Assume n is a non-negative integer.
    Example: power(2, 5) = 32
    Example: power(3, 0) = 1
    """

    # TODO: Implement this
    # Hint: x^n = x * x^(n-1)
    # Hint: What's x^0?
    if n == 0:
        return 1
    
    return x * power(x, n-1) 

# Test cases:
print(power(2, 5)) # should return 32
print(power(3, 0)) # should return 1
print(power(5, 3)) # should return 125
print()


# Exercise 4.2
print("Exercise 4.2")
def generate_binary_strings(n):
    """
    Generate all binary strings of length n.
    Example: generate_binary_strings(2) = ['00', '01', '10', '11']
    Example: generate_binary_strings(3) = ['000', '001', '010', '011', '100',
    '101', '110', '111']
    """
    # TODO: Implement this
    # Hint: For each position, you can place either '0' or '1'
    # Hint: Use a helper function that builds strings character by character
    if n == 0:
        return [""]
    
    smaller = generate_binary_strings(n-1)
    
    result = []
    for s in smaller:
        result.append("0" + s)
        result.append("1" + s)
    return result

# Test cases:
print(generate_binary_strings(2)) # should return ['00', '01', '10', '11']
print(generate_binary_strings(1)) # should return ['0', '1']
print()


# Exercise 4.3
print("Exercise 4.3")
def subset_sum(nums, target, index=0):
    """
    Check if any subset of nums adds up to target.
    Example: subset_sum([3, 34, 4, 12, 5, 2], 9) = True (3 + 4 + 2 = 9)
    Example: subset_sum([3, 34, 4, 12, 5, 2], 30) = False
    """
    # TODO: Implement this
    # Hint: For each number, you have two choices: include it or exclude it
    # Hint: Use index to track position in array
    if target == 0:
        return True
    if index == len(nums):
        return False
    
    if subset_sum(nums, target - nums[index], index + 1):
        return True
    return subset_sum(nums, target, index + 1)

# Test cases:
print(subset_sum([3, 34, 4, 12, 5, 2], 9)) # should return True
print(subset_sum([1, 2, 3, 4], 10)) # should return True
print(subset_sum([1, 2, 3], 7)) # should return False
print()


# Exercise 5.1
def recursive_sum(arr, n):
    """
    Sum first n elements of array arr recursively.
    """
    if n <= 0:
        return 0
    
    return arr[n-1] + recursive_sum(arr, n-1)
    # Questions to answer:
    # 1. Write the recurrence relation for time complexity
    ## T(n) = T(n-1) + 0(1)
    # 2. What is the time complexity? O(?)
    ## 0(n)
    # 3. What is the space complexity? O(?)
    ## 0(n)
    # 4. Draw the recursion tree for recursive_sum([1,2,3,4], 4)
    ## recursive_sum([1,2,3,4], 4)
    ##   ├── 4 + recursive_sum([1,2,3,4], 3)
    ##       ├── 3 + recursive_sum([1,2,3,4], 2)
    ##           ├── 2 + recursive_sum([1,2,3,4], 1)
    ##               ├── 1 + recursive_sum([1,2,3,4], 0)
    ##                   └── 0 (base case)


# Exercise 5.2
def binary_search(arr, target, left, right):
    """
    Search for target in sorted array arr[left:right+1].
    Return index if found, -1 otherwise.
    """
    # TODO: Implement recursive binary search
    # TODO: Analyze time complexity
    # TODO: Analyze space complexity
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    
    if target < arr[mid]:
        return binary_search(arr, target, left, mid-1)
    else:
        return binary_search(arr, target, mid+1, right)
    

# Requirements:
# 1. Implement the function
# 2. Write the recurrence relation
## T(n) = T(n/2) + O(1)
# 3. Prove time complexity is O(log n)
## Every recursive call halves the remaining search space
# 4. Compare space complexity with iterative version
## Recusive version --> Space = O(logn) | Iterative version --> Space = O(1)


# Exercise 5.3
def edit_distance(s1, s2):
    """
    Find minimum edit distance between s1 and s2.
    Operations allowed: insert, delete, replace
    Example: edit_distance("cat", "cut") = 1 (replace 'a' with 'u')
    Example: edit_distance("sunday", "saturday") = 3
    """
    # TODO: Design recursive solution
    # TODO: Identify overlapping subproblems
    # TODO: Optimize with memoization
    # TODO: Analyze time complexity (both versions)
    pass

# Tasks:
# 1. Write naive recursive solution
def edit_distance(s1, s2):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    
    if s1[0] == s2[0]:
        return edit_distance(s1[1:],s2[1:])
    
    insert = 1 + edit_distance(s1, s2[1:])
    delete = 1 + edit_distance(s1[1:], s2)
    replace = 1 + edit_distance(s1[1:], s2[1:])
    
    return min(insert, delete, replace)
# 2. Identify why it's inefficient
## Recomputes same subproblems over and over (thousands of times)
# 3. Add memoization
def edit_distance(s1, s2, i=0, j=0, memo=None):
    if memo is None:
        memo = {}
    
    if (i, j) in memo:
        return memo[(i, j)]
    
    if i == len(s1):
        return len(s2) - j
    
    if j == len(s2):
        return len(s1) - i
    
    if s1[i] == s2[j]:
        memo[(i, j)] = edit_distance(s1, s2, i+1, j+1, memo)
        return memo[(i, j)]
    
    insert = 1 + edit_distance(s1, s2, i, j+1, memo)
    delete = 1 + edit_distance(s1, s2, i+1, j, memo)
    replace = 1 + edit_distance(s1, s2, i+1, j+1, memo)
    
    memo[(i,j)] = min(insert, delete, replace)
# 4. Compare complexities
## Naive recursive function is exponential because it recompuites the same subproblems many times,
## while the memo version runs in O(m*n) time because each (i, j) subproblem is solved once and stored.
## The memo version uses O(m*n) space for the table compared to the naive version's O(m+n) recursion 
## depth but exponential time


# Question 2: Copy and run merge sort on a randomly generated list of 1000000 integers, and explain what's the complexity of the algorithm and why it is fast.
def merge_sort(arr):
    """Sort array using divide and conquer"""
    if len(arr) <= 1: # Base case
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid]) # Divide & recurse
    right = merge_sort(arr[mid:]) # Divide & recurse
    
    # Conquer: merge sorted halves
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

import random
import time

nums = [random.randint(0, 10_000_000) for _ in range(1_000_000)]

start = time.time()
sorted_nums = merge_sort(nums)
end = time.time()

print(f"Merge sort completed in {end - start:.2f} seconds")
## Merge sort runs in O(n logn) time because it repeatedly divides the list in half (logn levels) and performs 
## a linear merge at each level. Even for a list of a million integers, the algorithim is fast because the total
## work is proportional to n logn rather than n^2, and the merge step processes elements sequentially with great efficiency.