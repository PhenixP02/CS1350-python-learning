## Phenix Payton
## CS1350
## Mock Final

"""Problem 1 — Dictionary: Word Frequency Counter"""
def word_frequencies(text):
    freq = {}
    cleaned = ""
    for ch in text:
        if ch.isalpha() or ch.isspace(): # Keep only words and whitespaces (No nums or punctuation)
            cleaned += ch
        else:
            cleaned += " "
    
    for word in cleaned.lower().split():
        freq[word] = freq.get(word,0) + 1
    
    return freq

print(word_frequencies("The cat and THE dog. The dog ran."))
# Returns: {'the': 3, 'cat': 1, 'and': 1, 'dog': 2, 'ran': 1}
print()


"""Problem 2 — NumPy: Score Analysis"""
import numpy as np
def analyze(scores):
    overall_mean = np.round(np.average(scores), 2)
    student_means = np.round(np.average(scores, axis=1), 2)
    exam_means = np.round(np.average(scores, axis=0), 2)
    top_student = int(np.argmax(student_means))
    
    summary = {
        "Overall Average": overall_mean,
        "Student Averages": student_means,
        "Exam Averages": exam_means,
        "Top Student": top_student
    }
    
    return summary
scores = np.array([
[70, 80, 90, 100],
[60, 65, 70, 75],
[85, 90, 95, 100],
])
result = analyze(scores)
print(result)
# result["top_student"] == 2
print()


"""Problem 3 — OOP: BankAccount with Validation"""
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance must be positive")
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance must be positive")
        self._balance = value
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("insufficient funds")
        self._balance -= amount
    
    def __repr__(self):
        return f"BankAccount('{self.owner}', {self._balance})"

acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc.balance) # 120
print(acc) # BankAccount('Alice', 120)
# acc.withdraw(9999) # raises InsufficientFundsError
print()


"""Problem 4 — Regex: Log Line Parser"""
# [YYYY-MM-DD HH:MM:SS] LEVEL: message text
import re

def parse_log(line):
    match = re.search(r"\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+(?P<level>\w+):\s+(?P<message>.+)", line)
    if match:
        log_info = {
            "Timestamp": match.group("timestamp"),
            "Level": match.group("level"),
            "Message": match.group("message")
        }
        return log_info
    else:
        return None

print(parse_log("[2026-04-15 14:32:01] INFO: System started"))
# {'timestamp': '2026-04-15 14:32:01', 'level': 'INFO', 'message': 'System started'}
print(parse_log("invalid line"))
# None
print()


"""Problem 5 — Exception Handling: Safe Integer Conversion"""
def safe_convert(values):
    successes = []
    failures = []
    
    for i, value in enumerate(values):
        try:
            num = int(value)
            successes.append(num)
        except (ValueError, TypeError) as e:
            failures.append((i, value, str(e)))
    
    return (successes, failures)

print(safe_convert(["10", "abc", "42", None, "3.14"]))
# successes: [10, 42]
# failures: [(1, "abc", "..."), (3, None, "..."), (4, "3.14", "...")]
print()


"""Problem 6 — Recursion: Sum of Digits"""
def sum_of_digits(n):
    if n < 0:
        raise ValueError("n cannot be negative")
    
    if n < 10: # Base Case
        return n
    
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(0)) # 0
print(sum_of_digits(7)) # 7
print(sum_of_digits(1234)) # 10 (1 + 2 + 3 + 4)
print(sum_of_digits(99999)) # 45
#sum_of_digits(-5) # raises ValueError
print()


"""Problem 7 — Generators & Higher-Order Functions: Pipeline"""
def pipeline(iterable, funcs):
    for item in iterable:
        num = item
        for f in funcs:
            num = f(num)
        yield num

double = lambda x: x * 2
add_one = lambda x: x + 1
square = lambda x: x ** 2

gen = pipeline([1, 2, 3], [double, add_one, square])
print(list(gen)) # [9, 25, 49]
# reasoning: (1*2+1)**2 = 9, (2*2+1)**2 = 25, (3*2+1)**2 = 49
gen2 = pipeline(range(5), [])
print(list(gen2)) # [0, 1, 2, 3, 4]