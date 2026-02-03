
## Phenix Payton
## CS1350
## Homework 2
## 2/3/26

"""Problem 1: Movie Rating Analyzer"""
print()
print("Problem 1: Movie Rating Analyzer")
print()
print("Part A: User Statistics")
ratings = {
"Alice": {"Inception": 5, "Titanic": 3, "Avatar": 4, "Jaws": 2},
"Bob": {"Inception": 4, "The Matrix": 5, "Avatar": 5, "Jaws": 3},
"Carol": {"Titanic": 5, "The Matrix": 4, "Avatar": 3, "Interstellar": 5},
"Dave": {"Inception": 3, "Titanic": 4, "The Matrix": 5, "Jaws": 4},
"Eve": {"Inception": 5, "Avatar": 4, "Interstellar": 4, "Jaws": 1}
}

print("=== User Statistics ===")
for name, movies in ratings.items():
    print(f"{name}: {len(movies.items())} movies,", end=" ")
    highest_rate = 0
    rating_total = 0
    for movie, rating in movies.items():
        rating_total += rating
        if rating > highest_rate:
            highest_rate = rating
            favorite = movie
    avg_rating = rating_total / len(movies.items())
    print(f"avg rating: {avg_rating:.2f}, favorite: {favorite} ({highest_rate})")
print()

print("Part B: Movie Statistics")
movie_stats = {}
total_movie_rating = 0
movie_ratings = []
for movies in ratings.values():
    for movie, rating in movies.items():
        if movie not in movie_stats:
            movie_stats[movie] = {"ratings": []}
        movie_stats[movie]["ratings"].append(rating)

for movie, stats in movie_stats.items():
    movie_avg = sum(stats["ratings"]) / len(stats["ratings"])
    reviews = len(stats["ratings"])
    print(f"{movie}: {movie_avg:.2f} avg ({reviews} reviews)")
print()



"""Problem 2: Sales Data Transformer"""
print("Problem 2: Sales Data Transformer")
print()
print("Part A: Dictionary Comprehensions")
sales_records = [
{"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 5, "region": "North"},
{"product": "Mouse", "category": "Electronics", "price": 25, "quantity": 50, "region": "North"},
{"product": "Desk", "category": "Furniture", "price": 350, "quantity": 8, "region": "South"},
{"product": "Chair", "category": "Furniture", "price": 150, "quantity": 20, "region": "South"},
{"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 3, "region": "South"},
{"product": "Keyboard", "category": "Electronics", "price": 75, "quantity":30, "region": "North"},
{"product": "Desk", "category": "Furniture", "price": 350, "quantity": 5, "region": "North"},
{"product": "Monitor", "category": "Electronics", "price": 300, "quantity": 12, "region": "South"},
]

product_prices = {record["product"]: record["price"] for record in sales_records}
print(f"Product prices: {product_prices}")
expensive_products = {record["product"]: record["price"] for record in sales_records if record["price"] > 100}
print(f"Expensive products: {expensive_products}")
price_catergory = {record["product"]: "Premium" if record["price"] >= 300 else "Standard" for record in sales_records}
print(f"Product Category: {price_catergory}")
print()


print("Part B: Aggregation Patterns")
category_total = {}
for record in sales_records:
    category = record["category"]
    revenue = record["price"] * record["quantity"]
    category_total[category] = category_total.get(category, 0) + revenue
print(f"Revenue totals by category: {category_total}")  ## Homework Example Appears to be Incorrect

region_total = {}
for record in sales_records:
    region = record["region"]
    revenue = record["price"] * record["quantity"]
    region_total[region] = region_total.get(region, 0) + revenue
print(f"Revenue total by region: {region_total}") ## Homework Example Appears to be Incorrect

product_quantity = {}
for record in sales_records:
    product = record["product"]
    quantity = record["quantity"]
    product_quantity[product] = product_quantity.get(product, 0) + quantity
print(f"Total quantity sold by product: {product_quantity}")
print()



"""Problem 3: Course Registration System"""
print("Problem 3: Course Registration System")
# Students and their registered courses
registrations = {
"Alice": {"CS101", "CS201", "MATH101"},
"Bob": {"CS101", "MATH101", "PHYS101"},
"Carol": {"CS201", "CS301", "MATH201"},
"Dave": {"CS101", "CS201", "MATH101", "PHYS101"},
"Eve": {"CS301", "MATH201", "MATH301"}
}

# Course prerequisites (must have taken these BEFORE registering)
prerequisites = {
"CS101": set(), # No prerequisites
"CS201": {"CS101"}, # Must have CS101
"CS301": {"CS201"}, # Must have CS201
"MATH101": set(), # No prerequisites
"MATH201": {"MATH101"}, # Must have MATH101
"MATH301": {"MATH201"}, # Must have MATH201
"PHYS101": {"MATH101"} # Must have MATH101
}

# Course capacities and current enrollment
capacity = {"CS101": 30, "CS201": 25, "CS301": 20, "MATH101": 35, "MATH201": 25,
"MATH301": 20, "PHYS101": 30}

print("Part A: Set Operations")
all_courses = set()
all_courses = registrations["Alice"] | registrations["Bob"] | registrations["Carol"] | registrations["Dave"] | registrations["Eve"]
common_courses = registrations["Alice"] & registrations["Bob"] & registrations["Carol"] & registrations["Dave"] & registrations["Eve"]
only_alice = registrations["Alice"] - registrations["Bob"] - registrations["Carol"] - registrations["Dave"] - registrations["Eve"]
cs_students = [student 
               for student, courses in registrations.items() 
               if any(course.startswith("CS") for course in courses)]
print(f"All courese with enrollment: {all_courses}")
print(f"Courses all students share: {common_courses}")
print(f"Courses only Alice takes: {only_alice}")
print(f"Students in CS courses: {cs_students}")
print()


print("Part B: Prerequisite Validation")
valid_students = []
missing_courses = {}

for student, courses in registrations.items():
    valid = True
    for course in courses:
        required = prerequisites[course]  ## Create set of required Prereqs
        missing = required - courses    ## Create set of missing courses
        if missing:
            valid = False           ## Mark student as invalid
            if student not in missing_courses:  ## Create empty set if student not in missing_courses dict yet
                missing_courses[student] = set()
            missing_courses[student].update(missing)   ## Update missing classes
    if valid:
        valid_students.append(student)
print(f"Valid Students: {valid_students}")
print(f"Invalid Students:")
for name, courses in missing_courses.items():
    print(f"    {name} | Missing Courses - {courses}")
#print(f"Missing Prerequisites: {missing_courses}")
print()


print("Part C: Enrollment Analysis")
overloaded_students = set()
math_courses = set()
identical_schedules = {}
students = list(registrations.keys())
course_enrollment = {}
under_enrolled_courses = []

## Find Overloaded Students
for student in registrations.keys():
    if len(registrations[student]) >= 4:
        overloaded_students.add(student)

## Find all MATH courses enrolled in
for courses in registrations.values():
    for course in courses:
        if course.startswith("MATH"):
            math_courses.add(course)

## Check if schedules are identical
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        s1 = students[i]
        s2 = students[j]
        if registrations[s1] == registrations[s2]:
            if s1 not in identical_schedules:
                identical_schedules[s1] = []
            identical_schedules[s1].append(s2)

for student, courses in registrations.items():
    for course in courses:
        if course not in course_enrollment:
            course_enrollment[course] = 0
        course_enrollment[course] += 1
print(f"Overloaded students (4+ courses): {overloaded_students}")
print(f"All MATH courses enrolled: {math_courses}")
print(f"Students with identical schedules: {identical_schedules}")
print("Enrollment per course:")
for course, count in course_enrollment.items():
    print(f"    {course}: {count} students")
    if course_enrollment[course] < 3:
        under_enrolled_courses.append(course)
print(f"Under-Enrolled courses: {under_enrolled_courses}")