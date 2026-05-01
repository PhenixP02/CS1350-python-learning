## Phenix Payton
## CS1350
## Final Exam
## 5/1/26

"""Problem 1 — Dictionary: Gradebook Summary PARTIAL"""
print(" --- Problem 1 — Dictionary: Gradebook Summary --- ")
grades = {
"alice": {"CS1350": [85, 92, 78], "MATH201": [90, 88]},
"bob": {"CS1350": [72, 75, 80], "PHYS100": [65, 70]},
"carol": {"CS1350": [95, 98, 92], "MATH201": [85, 90]},
}
summary = {
    "student_averages": {},
    "course_averages": {},
    "top_per_course": {}
}

# Student Averages
for stu, course_scores in grades.items():
    all_scores = []
    
    for scores in course_scores.values():
        all_scores.extend(scores)
    average = sum(all_scores) / len(all_scores)
    summary["student_averages"][stu] = average

# Course Averages
course_totals = {}
for stu, course_scores in grades.items():
    for course, scores in course_scores.items():
        if course not in course_totals:
            course_totals[course] = []
        course_totals[course].extend(scores)
for course, all_scores in course_totals.items():
    summary["course_averages"][course] = sum(all_scores) / len(all_scores)
    
# Top Performers
top_per_course = {}
for stu, course_scores in grades.items():
    for course, scores in course_scores.items():
        average = sum(scores) / len(scores)
    
    if course not in top_per_course:
        top_per_course[course] = stu, average
    else:
        current_top_stu, current_top_avg = top_per_course[course]
        if average > current_top_avg:
            top_per_course[course] = (stu, average)
summary["top_per_course"] = top_per_course
print(summary)
print()
        
        
"""Problem 3 — Regex: Social Media Parser PARTIAL"""
print(" --- Problem 3 — Regex: Social Media Parser --- ")
import re

def parse_post(text):
    data = {
        "hashtags": [],
        "urls": [],
        "mentions": []
    }
    hashtags = re.findall(r"#\w+", text)
    for hashtag in hashtags:
        if hashtag not in data["hashtags"]:
            data["hashtags"].append(hashtag)
    urls = re.findall(r"https?://[^\s]+", text)
    for url in urls:
        if url not in data["urls"]:
            data["urls"].append(url)
    mentions = re.findall(r"(@\w+_\w+|@\w+)", text)
    for mention in mentions:
        if mention not in data["mentions"]:
            data["mentions"].append(mention)

    return data

text = """ Check out #Python and #python tips by @alice_dev and @Bob!
Links: https://example.com/path?q=1 and http://foo.org.
Re-ping @alice_dev and share #Python again.
"""
print(parse_post(text))
print()


"""Problem 5 — Recursion: Subset Sum COMPLETE"""
print(" --- Problem 5 — Recursion: Subset Sum --- ")
def subset_sum(nums, target, index=0):
    """
    Check if any subset of nums adds up to target.
    Example: subset_sum([3, 34, 4, 12, 5, 2], 9) = True (3 + 4 + 2 = 9)
    Example: subset_sum([3, 34, 4, 12, 5, 2], 30) = False
    """
    if target == 0:
        return True
    if index == len(nums):
        return False
    
    if subset_sum(nums, target - nums[index], index + 1):
        return True
    return subset_sum(nums, target, index + 1)

print(subset_sum([3, 34, 4, 12, 5, 2], 9)) # True (4 + 5 or 3 + 4 + 2)
print(subset_sum([3, 34, 4, 12, 5, 2], 30)) # False
print(subset_sum([1, 2, 3], 0)) # True (empty subset)
print(subset_sum([], 0)) # True
print(subset_sum([], 5)) # False
print(subset_sum([-2, 3, 5], 1)) # True (-2 + 3)
print(subset_sum([1, 2, 3], 7)) # False