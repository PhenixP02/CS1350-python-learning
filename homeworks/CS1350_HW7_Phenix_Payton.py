## Phenix Payton 
## CS1350 
## Homework 7 
## 4/17/27


"""UNIT 3: Pickle, File Paths, and File System Operations"""
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
        for category, extensions in organized.items():             
            if ext in extensions:                                  
                dest_folder = os.path.join(messy_folder, category) 
                shutil.move(file_path, dest_folder)
                print(f"Moved {file} --> {category}/")
    
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