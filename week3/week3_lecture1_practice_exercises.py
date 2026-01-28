

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print()

#1. Find all unique numbers (union).
#2. Find numbers in both sets (intersection).
#3. Find numbers only in set a (difference)
all_unique = a | b
both_sets = a & b
only_seta = a - b
print(f"All unique numbers (union): {all_unique}")
print(f"Numbers in both sets (intersection): {both_sets}")
print(f"Numbers only in set A: {only_seta}")
print()

morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

#1. Find employees who work ALL shifts.
#2. Find employees who work at least one shift (any shift).
#3. Find employees who ONLY work morning (not evening or weekend).
#4. Find employees who work exactly one shift.
all_shifts = morning_shift & evening_shift & weekend_shift
any_shift = morning_shift | evening_shift | weekend_shift
only_morning = morning_shift - evening_shift - weekend_shift
one_shift = morning_shift ^ evening_shift ^ weekend_shift
print(f"Working all shifts: {all_shifts}")
print(f"Working any shift: {any_shift}")
print(f"Only morning shift: {only_morning}")
print(f"Only one shift: {one_shift}")
print()

#Alice, Carol, Bob, Dave, Eve, Frank
prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

#1. Find students eligible to enroll (must meet ALL three criteria).
#2. Find students who met prereqs but haven't paid tuition.
#3. Find students who need to meet prereqs OR pay tuition (missing at least one)
enroll_eligible = prereqs_met & has_space & paid_tuition
prereq_no_tuition = prereqs_met - paid_tuition
all_students = prereqs_met | has_space | paid_tuition
need_tuition = all_students - paid_tuition
need_prereqs = all_students - prereqs_met
need_something = need_tuition | need_prereqs
print(f"Enroll eligible: {enroll_eligible}")
print(f"Prereqs met but no tuition paid: {prereq_no_tuition}")
print(f"Need tuition paid or prereqs: {need_something}")

# 1. Create a set {1, 2, 3}, add 4, and remove 1.
# 2. Create a set comprehension that generates all even numbers from 0-20.
# 3. Use discard() vs remove() to safely try removing an element that doesn't exist.

nums = {1, 2, 3}
nums.add(4)
nums.remove(1)
print(nums)

even_nums = {x for x in range(20) if x % 2 == 0}
print(f"Even numbers up to 20: {even_nums}")

#nums.remove(100) ##ERROR
nums.discard(100)
print(nums) ## NO ERROR

new_list = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
seen = set()
result = []
for num in new_list:
    if num not in seen:
        seen.add(num)
        result.append(num)
print(result)
print()

# Create a set comprehension that extracts all unique words from:
sentence = "To be or not to be that is the question"
sentence_lower = sentence.lower()
words = {word for word in sentence_lower.split()}
print(words)
print()

expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}
missing = expected - actual
print(f"Missing numbers: {missing}")