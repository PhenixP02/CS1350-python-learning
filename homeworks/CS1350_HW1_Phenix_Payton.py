"""
Phenix Payton
CS1350
Homework 1
Due: 1/23/26
"""

"""Problem 1 Contact Manager"""
## PART A
print()
print("=== PART A Initial Contacts ===")
contacts = {}
print(f"Before Update: {contacts}")
contacts.update({"Mom": "555-1234", "Dad": "555-5678", "Best Friend": "555-8888", "Pizza Place": "555-9999", "Work": "555-0000"})
print(f"After Update: {contacts}")
print()

## PART B
print("=== PART B Access and Modify ===")
print(f"Mom's phone number: {contacts["Mom"]}")
contacts["Dad"] = "555-4321"
print(f"Dad's new number: {contacts["Dad"]}")
contacts["Dentist"] = "555-2222" ## Added Dentist to contacts
print(f"Grandma's number: {contacts.get("Grandma")}") if contacts.get("Grandma") != None else print("Contact not found") ## Print Grandma Number if in contacts
print(f"Updated List: {contacts}")
print()

## PART C
print("=== PART C Delete and Analyze ===")
del contacts["Pizza Place"]
print(contacts)
old_work_number = contacts.pop("Work")
print(f"Removed work number: {old_work_number}")
print(f"Number of contacts: {len(contacts)}")
print(f"All contact names: {contacts.keys()}")
print(f"All contact numbers: {contacts.values()}")
print()



"""Problem 2 Grade Book Analyzer"""
print("Problem 2")
print()
grades = {
"Alice": 87,
"Bob": 65,
"Carol": 92,
"Dave": 78,
"Eve": 55,
"Frank": 88,
"Grace": 71,
"Henry": 95,
"Ivy": 60,
"Jack": 83
}
print("=== PART A Basic Statistics ===")
print(f"All Students: {grades.keys()}")
print(f"All Grades: {grades.values()}")
total_students = len(grades)
grade_total = sum(grades.values())
class_average = round(grade_total / total_students, 2)
highest_grade = max(grades.values())
lowest_grade = min(grades.values())
print(f"Total number of students: {total_students}\nSum of all Grades: {grade_total}\nClass Average: {class_average}\nHighest Grade: {highest_grade}\nLowest Grade: {lowest_grade}")
print()

print("=== PART B Iteration and Analysis ===")
students_passed = 0
students_failed = 0
grade_As = 0
grade_Bs = 0
grade_Cs = 0
grade_Ds = 0
grade_Fs = 0
print("--- Grade Report ---")
for name, grade in grades.items():
    if grade >= 90:
        letter_grade = "A"
        grade_As += 1
    elif grade >= 80:
        letter_grade = "B"
        grade_Bs += 1
    elif grade >= 70:
        letter_grade = "C"
        grade_Cs += 1
    elif grade >= 60:
        letter_grade = "D"
        grade_Ds += 1
    else:
        letter_grade = "F"
        grade_Fs += 1
    if grade >= 60:
        students_passed += 1
    else:
        students_failed += 1
    print(f"{name}: {grade} ({letter_grade})")
print()
print("--- Grade Distribution ---")
print(f"Number of Passing Students: {students_passed}")
print(f"Number of failing Students: {students_failed}")
print(f"Number of As: {grade_As}\nNumber of Bs: {grade_Bs}\nNumber of Cs: {grade_Cs}\nNumber of Ds: {grade_Ds}\nNumber of Fs: {grade_Fs}")
print()

print("=== PART C Find Specific Students ===")
hi_score = -1
low_score = 101
high_achievers = {}
class_avg = sum(grades.values()) / len(grades)
for name, grade in grades.items():
    if grade > hi_score:
        hi_score = grade
        high_student = name
    elif grade < low_score:
        low_score = grade
        low_student = name
    if grade > class_avg:
        high_achievers[name] = grade
    continue
print(f"--- Top and Bottom Performers ---")
print(f"Highest scorer: {high_student} ({hi_score})")
print(f"Lowest scorer: {low_student} ({low_score})")
print(f"\n--- Above Average Students ---")
for student, score in high_achievers.items():
    print(f"{student}: {score}")