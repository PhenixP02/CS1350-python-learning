vowels = {"a", "e", "i", "o", "u"}

num_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_nums = set(num_list)
print(f"Number of items in set: {len(unique_nums)}")

empty = {}  ##This is a dictionary!

text = "mississippi"
unique_chars = set(text)
print(f"Unique Characters: {unique_chars}")
print(f"Number of unique Characters: {len(unique_chars)}")

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
emails_set = set(emails)
emails_no_dupes = list(emails_set)
print(f"List from set: {emails_no_dupes}")

s = {[1, 2], [3, 4]} ##LIST

