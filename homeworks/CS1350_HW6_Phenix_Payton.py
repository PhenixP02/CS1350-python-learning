## Phenix Payton
## CS1350
## Homework 6
## 4/3/26


"""Week 11 Lecture 1: Grouping, Capturing, Alternation, and Match Objects"""
## -----UNIT 1: Grouping and Capturing-----
import re

# Beginner — Extract Name and Age
print("Beginner — Extract Name and Age")
texts = [
    "Alice is 20 years old",
    "Bob is 22 years old",
    "Charlie is 19 years old",
]

for text in texts:
    # TODO: Use two capturing groups to extract name and age
    match = re.search(r"(?P<name>\w+) is (?P<age>\d+) years old", text)
    if match:
        name = match.group("name")
        age = match.group("age")
        print(f"Name: {name}, Age: {age}")
print()

# Intermediate — Parse a Date
print("Intermediate — Parse a Date")
dates = ["03-15-2026", "12-25-2025", "01-01-2000"]

for date in dates:
    # TODO 1: Write a pattern with named groups for month, day, year
    # Format: MM-DD-YYYY
    match = re.search(r"(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})", date)
    if match:
        # TODO 2: Extract using named groups
        info = match.groupdict()
        print(f"{info['month']}/{info['day']}/{info['year']}")
print()

# Advanced — Timestamp Parser
print("Advanced — Timestamp Parser")
log_entries = [
"[2026-03-10 14:30:45] Server started",
"[2026-03-10 09:15:02] User login",
"[2026-03-11 22:00:00] Backup complete",
]

for entry in log_entries:
    # TODO: Write a pattern that captures date, time, and message
    # The bracket section: [YYYY-MM-DD HH:MM:SS]
    # Then the message after "] "
    # Use named groups: date, time, message
    pattern = r"\[(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})\] (?P<message>.*)"
    match = re.search(pattern, entry)
    if match:
        d = match.groupdict()
        print(f"{d['message']} on {d['month']}/{d['day']}/{d['year']} at {d['hour']}:{d['minute']}:{d['second']}")


## ----Unit 2: Match Object Deep Dive----
# Beginner — Match Positions
print("Beginner — Match Positions")
text = "The price is $49.99 today"
match = re.search(r"\$\d+\.\d{2}", text)

if match:
    # TODO 1: Print the matched text
    print(f"Price: {match.group()}")
    
    # TODO 2: Print start and end positions
    # Hint: match.start(), match.end()
    print(f"Start: {match.start()} End: {match.end()}")
    
    # TODO 3: Use span to extract everything before and after the price
    start, end = match.span()
    before = text[0: start]
    after = text[end:]
    print(f"Before: '{before}'")
    print(f"After: '{after}'")
print()

# Intermediate — Duplicate Word Finder
print("Intermediate — Duplicate Word Finder")
sentences = [
"This is is a problem",
"The the cat sat down",
"No duplicates here",
"I really really like Python",
]

for sentence in sentences:
    # TODO: Use a backreference to find repeated words
    # Pattern: word boundary, capture a word, whitespace, same word, word boundary
    
    match = re.search(r"\b(\w+)\s+\1\b", sentence)
    if match:
        print(f"Duplicate '{match.group(1)}' in: {sentence}")
    else:
        print(f"No duplicates in: {sentence}")
print()

# Advanced — Structured Data Extractor
print("Advanced — Structured Data Extractor")
records = [
    "Name: Alice Smith | ID: EMP-001 | Dept: Engineering",
    "Name: Bob Jones | ID: EMP-042 | Dept: Marketing",
    "Name: Carol White | ID: EMP-108 | Dept: Sales",
]

pattern = r"Name: (?P<name>\w+\s\w+) \| ID: (?P<id>\w{3}-\d{3}) \| Dept: (?P<dept>\b\w+\b)"

for record in records:
    match = re.search(pattern, record)
    if match:
        d = match.groupdict()
        print(f"Name: {d['name']} ID: {d['id']} Department: {d['dept']}")
        
        # TODO 2: Print the position of the ID field using match.span('id')
        id_span = match.span("id")
        print(f"ID span: {id_span}")
print()


## Unit 3: Alternation
# Beginner — Match Greetings
print("Beginner — Match Greetings")
texts = [
"Hello there!",
"Hi everyone.",
"Hey you!",
"Goodbye now.",
"Howdy partner!"
]

for text in texts:
    # TODO: Match "Hello", "Hi", or "Hey" at the start of the string
    match = re.search(r"^(Hello |Hi |Hey )", text)
    
    if match:
        print(f"Greeting found: '{match.group(1)}' in '{text}'")
    else:
        print(f"No greeting in: '{text}'")
print()

# Intermediate — File Type Categorizer
print("Intermediate — File Type Categorizer")
files = [
"report.pdf", "photo.jpg", "data.csv",
"script.py", "style.css", "page.html",
"notes.txt", "image.png", "app.js"
]

for f in files:
    lower_f = f.lower()
    
    # TODO 1: Match document extensions (.pdf, .doc, .txt, .csv)
    is_doc = re.search(r"(\.pdf|\.csv|\.txt|\.doc)$",lower_f)
    
    # TODO 2: Match image extensions (.jpg, .jpeg, .png, .gif)
    is_img = re.search(r"(\.jpg|\.jpeg|\.png|\.gif)$",lower_f)
    
    # TODO 3: Match code extensions (.py, .js, .html, .css)
    is_code = re.search(r"(\.py|\.js|\.html|\.css)$",lower_f)
    
    if is_doc:
        category = f"Document ({is_doc.group(1)})"
    elif is_img:
        category = f"Image ({is_img.group(1)})"
    elif is_code:
        category = f"Code ({is_code.group(1)})"
    else:
        category = "Other"
    
    print(f"{f:<15} → {category}")
print()

# Advanced — Multi-Format Date Parser
print("Advanced — Multi-Format Date Parser")

dates = [
    "2026-03-15", # ISO: YYYY-MM-DD
    "03/15/2026", # US: MM/DD/YYYY
    "15 Mar 2026", # Text: DD Mon YYYY
    "March 15, 2026", # Long: Month DD, YYYY
    "not a date",
]

for date in dates:
    # TODO 1: Try ISO format with named groups
    iso = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date)

    # TODO 2: Try US format
    us = re.search(r"(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})", date)

    # TODO 3: Try text format (3-letter month abbreviation)
    text_fmt = re.search(r"(?P<day>\d{2})\s(?P<month>\w+)\s(?P<year>\d{4})", date)

    # TODO 4: Try long format — write the pattern yourself
    long_fmt = re.search(r"(?P<month>\w+)\s(?P<day>\d{2}),\s(?P<year>\d{4})", date)

    matched = iso or us or text_fmt or long_fmt
    if matched:
        d = matched.groupdict()
        print(f"'{date}' → month={d['month']}, day={d['day']}, year={d['year']}")
    else:
        print(f"'{date}' → no match")
print()


"""Week 12 Lecture 2: Advanced File Processing"""
## UNIT 1: Working with File Formats
# Exercise 1.1: Beginner — Text to CSV Converter
def practice_1_beginner():
    """
    Beginner: Convert text to CSV
    """
    print("\n" + "=" * 50)
    print("EXERCISE 1.1: Text to CSV Converter")
    print("=" * 50)

    # Create a text file with data
    with open("employees.txt", "w") as employees:
        employees.write("John Smith 35 Engineer\n")
        employees.write("Jane Doe 28 Designer\n")
        employees.write("Bob Johnson 42 Manager\n")
        
    # TODO 1: Read text file and convert to CSV
    with open("employees.txt", "r") as employees:
        with open("employees.csv", "w") as employees_csv:
            # Write CSV header
            employees_csv.write("First,Last,Age,Job\n")
            
            # TODO: Read each line and convert
            for line in employees:
                parts = line.strip().split()
                # parts[0] = first name, parts[1] = last name, etc.

                # TODO: Write as CSV line
                # Format: John,Smith,35,Engineer
                csv_line = f"{parts[0]},{parts[1]},{parts[2]},{parts[3]}"
                employees_csv.write(csv_line + "\n")

    # TODO 2: Read and verify CSV
    print("\nCSV Contents:")
    with open("employees.csv", "r") as employees_csv:
        # TODO: Read and display
        for line in employees_csv:
            print(line.strip())

# Run the exercise
practice_1_beginner()
print()


## Exercise 1.2: Intermediate — CSV Grade Calculator
def practice_1_intermediate():
    """
    Intermediate: Process CSV data
    """
    print("\n" + "=" * 50)
    print("EXERCISE 1.2: Grade Calculator")
    print("=" * 50)
    
    # Create grades CSV
    with open("grades.csv", "w") as grades:
        grades.write("Student,Math,Science,English\n")
        grades.write("Alice,95,87,92\n")
        grades.write("Bob,78,85,88\n")
        grades.write("Charlie,92,94,85\n")
        grades.write("Diana,88,91,95\n")
   
    # TODO 1: Read CSV and calculate averages
    with open("grades.csv", "r") as grades:
        header = grades.readline().strip().split(",")
        print(f"Subjects: {header[1:]}")

        student_averages = []

        for line in grades:
            parts = line.strip().split(",")
            name = parts[0]
        
            # TODO: Convert grades to numbers
            scores = [int(x) for x in parts[1:]]
            
            # TODO: Calculate average
            average = sum(scores) / len(scores)
        
            student_averages.append((name, average))
            print(f"{name}: {average:.1f}")
    
    # TODO 2: Save results to new CSV
    with open("averages.csv", "w") as averages:
        averages.write("Student,Average\n")
        
        # TODO: Write each student's average
        for name, avg in student_averages:
            averages.write(f"{name},{avg:.1f}\n")

# Run the exercise
practice_1_intermediate()
print()


## Exercise 1.3: Advanced — JSON Database
def practice_1_advanced():
    """
    Advanced: JSON database system
    """
    print("\n" + "=" * 50)
    print("EXERCISE 1.3: JSON Database")
    print("=" * 50)

    import json

    # TODO 1: Create a product database in JSON
    products = {
        "inventory": [
            {"id": 1, "name": "Laptop", "price": 999.99, "stock": 5},
            {"id": 2, "name": "Mouse", "price": 29.99, "stock": 15},
            {"id": 3, "name": "Keyboard", "price": 79.99, "stock": 8}
        ],
        "last_updated": "2024-01-15",
        "store": "Tech Store"
    }
    
    # TODO: Save to JSON file
    with open("products.json", "w") as productdb:
        json.dump(products, productdb, indent=4)
    
    print("Product database created")
    
    # TODO 2: Load and modify JSON — add a new product
    new_product = {
        "id": 4,
        "name": "Monitor",
        "price": 299.99,
        "stock": 3
    }
    # TODO: Add to inventory
    with open("products.json", "r") as productdb:
        data = json.load(productdb)
    
    data["inventory"].append(new_product)
    
    # TODO 3: Update stock levels

    for item in data["inventory"]:
        if item["id"]  == 2:    # Mouse
            
            item["stock"] += 5
        if item["id"] == 3:     # Keyboard
            
            item["stock"] -= 2
            
    # TODO 4: Save updated data
    with open("products.json", "w") as f:
        json.dump(data, f, indent=4)

    # TODO 5: Generate report from JSON
    
    with open("products.json", "r") as f:
        report_data = json.load(f)
    
    print("\n--- PRODUCT INVENTORY REPORT ----")
    print(f"Store: {report_data['store']}")
    print(f"Last Updated: {report_data['last_updated']}\n")
    
    print(f"{'ID':<5} {'Name':<15} {'Price':<10} {item['stock']:<10}")
    print("-" * 40)
    
    for item in report_data["inventory"]:
        print(f"{item['id']:<5} {item['name']:<15} ${item['price']:<10} {item['stock']:<10}")
    
    print("\nReport Generated Successfully")
    
    

# Run the exercise
practice_1_advanced()


## Exercise 2.1: Beginner — JSON Contact Card
def practice_2_beginner():
    """
    Beginner: Basic JSON operations
    """
    print("\n" + "=" * 50)
    print("EXERCISE 2.1: JSON Contact Card")
    print("=" * 50)
    
    import json
    
    # TODO 1: Create a contact dictionary
    contact = {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "555-1234",
    "age": 25
    }

    # TODO 2: Convert to JSON string
    json_str = json.dumps(contact) # Replace with json.dumps(contact)
    print(f"JSON String: {json_str}")
    
    # TODO 3: Save to file
    with open("contact.json", "w") as f:
        # TODO: Use json.dump to save contact
        json.dump(contact, f, indent=2)
    
    print("Contact saved to file")
    
    # TODO 4: Load from file
    with open("contact.json", "r") as f:
        loaded_contact = json.load(f)
    
    # TODO 5: Access data
    print(f"\nLoaded contact:")
    print(f"Name: {loaded_contact['name']}")
    print(f"Email: {loaded_contact['email']}")

# Run the exercise
practice_2_beginner()
print()


## Exercise 2.2: Intermediate — Settings Manager
def practice_2_intermediate():
    """
    Intermediate: Application settings in JSON
    """
    print("\n" + "=" * 50)
    print("EXERCISE 2.2: Settings Manager")
    print("=" * 50)
    
    import json
    
    # Default settings
    default_settings = {
        "app_name": "My App",
        "version": "1.0.0",
        "user_preferences": {
            "theme": "dark",
            "font_size": 12,
            "auto_save": True
            },
        "recent_files": [],
        "window_size": [800, 600]
    }
    
    # TODO 1: Save default settings with nice formatting
    with open("settings.json", "w") as settings_json:
        json.dump(default_settings, settings_json, indent=2)
    
    print("Default settings created")
    
    # TODO 2: Load and modify settings
    # Change theme to "light", add a file to recent_files, etc.
    with open("settings.json", "r") as f:
        settings_load = json.load(f)
    
    settings_load['user_preferences']['theme'] = "Light"
    settings_load['recent_files'].append("document.txt")
    
    # TODO 3: Save updated settings
    with open("settings.json", "w") as settings_json:
        json.dump(settings_load, settings_json, indent=2)
    
    # TODO 4: Create backup
    with open("settings.json", "r") as settings_json:
        settings_load = json.load(settings_json)
    
    with open("settings_backup.json", "w") as settings_backup:
        json.dump(settings_load, settings_backup, indent=2)
    
    print("Settings backed up")

# Run the exercise
practice_2_intermediate()
print()


## Exercise 2.3: Advanced — Student Database
def practice_2_advanced():
    """
    Advanced: Mini database with JSON
    """
    print("\n" + "=" * 50)
    print("EXERCISE 2.3: Student Database")
    print("=" * 50)
    
    import json
    
    # TODO 1: Create database structure
    database = {
        "students": {}
    }
    
    # TODO 2: Add students function
    def add_student(db, student_id, name, grades):
        db["students"][student_id] = {
            "name": name,
            "grades": grades
        }
    
    # Add sample students
    add_student(database, 1001, "Alice", [95, 87, 92, 88])
    add_student(database, 1002, "Bob", [78, 85, 80, 82])
    add_student(database, 1003, "Charlie", [92, 94, 96, 91])
    
    # TODO 3: Save database to student_db.json
    with open("student_db.json", "w") as f:
        json.dump(database, f, indent=2)
    print("Database created")
    
    # TODO 4: Query function
    def find_student(db_file, student_id):
        with open(db_file, 'r') as f:
            data = json.load(f)
        
        return data["students"].get(student_id)
    
    # Test query
    result = find_student("student_db.json", 1001)
    if result:
        print(f"\nFound: {result['name']}")
    
    # TODO 5: Generate report
    # Read database, categorize students as "high_achievers" or "needs_support"
    # Save report to report.json
    with open("student_db.json", "r") as f:
        data = json.load(f)
    
    report = {
        "high_achievers": [],
        "average_performers": [],
        "needs_support": []
    }

    for sid, info in data["students"].items():
        avg = sum(info["grades"]) / len(info["grades"])
        
        entry = {
            "id": sid,
            "name": info["name"],
            "average": avg
        }

        if avg >= 90:
            report["high_achievers"].append(entry)
        elif avg < 70:
            report["needs_support"].append(entry)
        else:
            report["average_performers"].append(entry)
    
    with open("report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Report Generated")

# Run the exercise
practice_2_advanced()
print()


## UNIT 3: Pickle, File Paths, and File System Operations
# Exercise 3.1: Beginner — Pickle Basics and Project Structure
def practice_3_beginner():
    """
    Beginner: Basic pickle operations and directory creation
    """

    print("\n" + "=" * 50)
    print("EXERCISE 3.1: Pickle & Project Setup")
    print("=" * 50)
    
    import pickle
    import os
    
    # --- Part A: Pickle ---
    # TODO 1: Create a list to pickle
    shopping_list = ["Apples", "Bananas", "Milk", "Bread"]

    # TODO 2: Save with pickle
    with open("shopping.pkl", "wb") as f:
        # TODO: Use pickle.dump
        pickle.dump(shopping_list, f)

    print("Shopping list pickled!")

    # TODO 3: Load with pickle
    with open("shopping.pkl", "rb") as f:
        loaded_list = pickle.load(f)
        print(f"Loaded list: {loaded_list}")

    # TODO 4: Add items and re-save
    loaded_list.append("Eggs")
    loaded_list.append("Cheese")
    with open("shopping.pkl", "wb") as f:
        # TODO: Save updated list
        pickle.dump(loaded_list, f)
    print("Updated list saved")

    # --- Part B: Directory Structure ---
    
    # TODO 5: Create project directory
    project_name = "my_project"
    if not os.path.exists(project_name):
        # TODO: Create the directory
        os.mkdir(project_name)

    # TODO 6: Create subdirectories
    subdirs = ["src", "docs", "tests", "data"]
    for subdir in subdirs:
        path = os.path.join(project_name, subdir)
        # TODO: Create each subdirectory
        if not os.path.exists(path):
            os.mkdir(path)

    # TODO 7: Create initial files (README.md, main.py in src)
    readme_path = os.path.join(project_name, "README.md")
    with open(readme_path, "w") as f:
        f.write("# My Project\n\nMy Project README.md")
    
    main_path = os.path.join(project_name, "src", "main.py")
    with open(main_path, "w") as f:
        f.write("def main():\n")
        f.write("   print('Hello from main.py!')\n\n")
        f.write("main()")
    
    # TODO 8: List project structure
    print("\nProject structure:")
    for root, dirs, files in os.walk(project_name):
        level = root.replace(project_name, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}{os.path.basename(root)}/")
        for file in files:
            print(f"{indent}  {file}")

# Run the exercise
practice_3_beginner()


# Exercise 3.2: Intermediate — File Organizer
def practice_3_intermediate():
    """
    Intermediate: Organize files by type
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3.2: File Organizer")
    print("=" * 50)

    import os
    import shutil
    
    messy_folder = "messy_files"
    # TODO: Setup — Create messy folder with test files
    if not os.path.exists(messy_folder):
        os.mkdir(messy_folder)
    test_files = [
    "document.txt", "image.jpg", "photo.png",
    "report.pdf", "script.py", "data.csv",
    "music.mp3", "video.mp4", "archive.zip"
    ]
    
    # TODO: Create each file in messy_folder
    for file in test_files:
        file_path = os.path.join(messy_folder, file)
        with open(file_path, "w") as f:
            f.write(f"Test file: {file}")
    
    # Category mapping
    organized = {
        "documents": [".txt", ".pdf", ".doc"],
        "images": [".jpg", ".png", ".gif"],
        "code": [".py", ".js", ".html"],
        "data": [".csv", ".json", ".xml"],
        "media": [".mp3", ".mp4", ".avi"],
        "archives": [".zip", ".tar", ".rar"]
    }
    
    # TODO: Create organized folders for each category
    for cat in organized.keys():
        cat_path = os.path.join(messy_folder, cat)
        if not os.path.exists(cat_path):
            os.mkdir(cat_path)
    
    # TODO: Organize files
    # Iterate through messy_folder
    # Get file extension
    for file in os.listdir(messy_folder):
        file_path = os.path.join(messy_folder, file)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file Extension
        name, ext = os.path.splitext(file)
        ext = ext.lower()
        
        # Find matching folder
        # Move file to appropriate folder
#        for category, extensions in organized.items():             Block Commented out
#            if ext in extensions:                                  Errors due to files already moved
#                dest_folder = os.path.join(messy_folder, category) UNCOMMENT WHEN FINISHED
#                shutil.move(file_path, dest_folder)
#                print(f"Moved {file} --> {category}/")
    
    # TODO: Show organized structure
    for root, dirs, files in os.walk(messy_folder):
        level = root.replace(messy_folder, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}{os.path.basename(root)}/")
        for file in files:
            print(f"{indent} {file}")

# Run the exercise
practice_3_intermediate()
print()

# Exercise 3.3: Advanced — Game Save System with Backup
# TODO 1: Create game state class  ## Error occured when class was inside practice_3_advanced() function. Moved outside to fix it
class GameState:
    def __init__(self):
        self.player_name = ""
        self.level = 1
        self.score = 0
        self.inventory = []
        self.position = (0, 0)
        
    def __str__(self):
        return f"{self.player_name} - Level {self.level}, Score: {self.score}"

def practice_3_advanced():
    """
    Advanced: Complex object serialization and backup system
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3.3: Game Save System")
    print("=" * 50)

    import pickle
    import os
    import shutil
    from datetime import datetime
    from pathlib import Path

    # TODO 2: Create and populate a game state
    game = GameState()
    game.player_name = "Hero"
    game.level = 5
    game.score = 1250
    game.inventory = ["Sword", "Shield", "Potion"]
    game.position = (10, 25)
    
    # TODO 3: Create saves directory and save game with pickle
    saves_dir = Path("saves")
    saves_dir.mkdir(exist_ok=True)
    
    save_path = saves_dir / "save1.pkl"
    
    with open(save_path, "wb") as f:
        pickle.dump(game, f)
    print(f"Game saved to {save_path}")
    
    # TODO 4: Load and verify saved game
    # Print player name, level, score, inventory, position
    with open(save_path, "rb") as f:
        loaded_game = pickle.load(f)
    
    print("Loaded Game:")
    print(f"  Name:{loaded_game.player_name}")
    print(f"  Level:{loaded_game.level}")
    print(f"  Score:{loaded_game.score}")
    print(f"  Inventory:{loaded_game.inventory}")
    print(f"  Position:{loaded_game.position}")
    
    # TODO 5: Implement multiple save slots
    def save_game(game_state, slot_number):
        """Save game to a specific slot"""
        saves_dir = Path("saves")
        saves_dir.mkdir(exist_ok=True)
        
        filename = f"slot_{slot_number}.pkl"
        save_path = saves_dir / filename
        
        with open(save_path, "wb") as f:
            pickle.dump(game_state, f)
        print(f"Saved to {filename}")

    # TODO 6: List all save files
    def list_saves():
        saves_dir = Path("saves")
        if not saves_dir.exists():
            print("No saves directory found.")
            return
        
        saves = sorted(saves_dir.glob("*.pkl"))
        if not saves:
            print("No save files found.")
            return

        print("Available Saves:")
        for save in saves:
            print(f" - {save}")
    # TODO 7: Create backup function
    def create_backup(source_dir, backup_dir="backups"):
        """Create timestamped backup of source directory"""
        # Create backup directory
        source = Path(source_dir)
        backup_root = Path(backup_dir)
        backup_root.mkdir(exist_ok=True)
        
        # Create timestamp-based folder name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_root / f"backup_{timestamp}"
        
        # Copy entire directory
        shutil.copytree(source, backup_path)
        print(f"Backup created at {backup_path}")
        return backup_path
    
    # TODO 8: Verify backup
    def verify_backup(source, backup):
        """Check all files in source are also in backup"""
        source = Path(source)
        backup = Path(backup)
        
        source_files = sorted([p.relative_to(source) for p in source.rglob("*") if p.is_file()])
        backup_files = sorted([p.relative_to(source) for p in source.rglob("*") if p.is_file()])
        
        if source_files == backup_files:
            print("Backup verification successful - all files match.")
            return True
        else:
            print("Backup verification FAILED - file mismatch detected.")
            return False
            
    # TODO 9: Cleanup old backups (keep only most recent N)
    def cleanup_old_backups(backup_dir, keep_count=3):
        # Get all backups sorted by modification time
        backup_root = Path(backup_dir)
        if not backup_root.exists():
            print("No backups to clean.")
            return
        
        backups = sorted(
            [p for p in backup_root.iterdir() if p.is_dir()],
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )
        
        # Keep only the most recent ones
        to_delete = backups[keep_count:]
        
        for folder in to_delete:
            shutil.rmtree(folder)
            print(f"Deleted old backup: {folder.name}")
        
        print("Backup cleanup complete.")
        
# Run the exercise
practice_3_advanced()