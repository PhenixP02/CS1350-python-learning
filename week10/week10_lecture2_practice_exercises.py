import re

texts = ["Hello World", "Say Hello", "Hello", "HELLO"]
for text in texts:
    # TODO 1: Check if text starts with "Hello" using ^
    starts = re.search(r"^Hello", text)
    # TODO 2: Check if text ends with "Hello" using $
    ends = re.search(r"Hello$", text)
    # TODO 3: Check if text is exactly "Hello" using ^ and $
    exact = re.search(r"^Hello$", text)
    s = "yes" if starts else "no"
    e = "yes" if ends else "no"
    x = "yes" if exact else "no"
    print(f"'{text}' — starts: {s}, ends: {e}, exact: {x}")
    

filenames = [
"report.pdf", "image.jpg", "notes.txt",
"script.py", "data.csv", "photo.PNG",
"noext", ".hidden", "tricky.pdf.exe"
]

for name in filenames:
    lower_name = name.lower()
    # TODO 1: Check if file ends with .pdf using $ anchor and escaped dot
    is_pdf = re.search(r"\.pdf$", name)
    # TODO 2: Check if file ends with .jpg or .png
    is_image = re.search(r"\.jpg$", name) or re.search(r"\.PNG$", name)
    # TODO 3: Check if filename starts with a dot (hidden file)
    is_hidden = re.search(r"^\.", name)
    label = []
    if is_pdf: label.append("PDF")
    if is_image: label.append("IMAGE")
    if is_hidden: label.append("HIDDEN")
    print(f"{name:<20} → {', '.join(label) if label else 'other'}")


# Quantifiers — *, +, ?
# * = 0+, + =1+, ? = 0/1

import re
text = "My phone is 555-1234 and my zip is 46802"
# TODO 1: Find the first sequence of one or more digits
match = re.search(r"\d+", text)
if match:
    print(f"First number: {match.group()}")

# TODO 2: Find the first sequence of one or more word characters
match2 = re.search(r"\w+", text)
if match2:
    print(f"First word: {match2.group()}")

# TODO 3: Search for optional "s" — match "cat" or "cats"
for word in ["cat", "cats", "catch"]:
    m = re.search(r"^cats?$", word)
    found = m.group() if m else "no match"
    print(f"'{word}' → {found}")


html = '<a href="page1.html">Link 1</a> and <a href="page2.html">Link 2</a>'
# TODO 1: Use a greedy pattern to match from first < to last >
greedy = re.search(r"<.+>", html)
print(f"Greedy: '{greedy.group()}'")
# TODO 2: Use a non-greedy pattern to match from first < to first >
non_greedy = re.search(r"<.+?>", html)
print(f"Non-greedy: '{non_greedy.group()}'")
# TODO 3: Match a quoted string (anything between double quotes, non-greedy)
quote_match = re.search(r"\".*?\"", html)
if quote_match:
    print(f"First quoted: {quote_match.group()}")