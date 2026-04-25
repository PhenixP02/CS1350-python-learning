## Phenix Payton
## CS1350
## Homework 8
## 4/21/26

""" --- Lecture 1 --- """
# Lecture 1 Unit 1
def practice_1_basic_exceptions():
    """
    Practice identifying and handling common exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 1: Handle the Exceptions")
    print("="*50)

    # TODO 1: Fix division by zero
    def safe_divide(a, b):
        """Return a/b or None if division by zero"""
        try:
            return a / b
        except ZeroDivisionError as e:
            return f"Error: {e}"

    # Test your function
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print()

    # TODO 2: Fix list index error
    def safe_get_item(lst, index):
        """Get item at index or return 'Not found'"""
        try:
            return lst[index]
        except IndexError as e:
            return f"Error: {e}"

    # Test your function
    my_list = [1, 2, 3]
    print(f"Item at index 1: {safe_get_item(my_list, 1)}")
    print(f"Item at index 10: {safe_get_item(my_list, 10)}")
    print()

    # TODO 3: Handle multiple exceptions
    def convert_to_number(value):
        """Convert string to int or float, return None if impossible"""
        # Try int first, then float, handle ValueError
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError) as e:
                print(f"Error: {e} (Must be integer or float)")
                return None

    # Test conversions
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = convert_to_number(val)
        print(f"Converting '{val}': {result}")

# Run the practice
practice_1_basic_exceptions()


# Lecture 1 Unit 2
def practice_2_exception_hierarchy():
    """
    Practice with exception hierarchy
    """
    print("\n" + "="*50)
    print("EXERCISE 2: Exception Hierarchy")
    print("="*50)

    # TODO 1: Catch multiple related exceptions efficiently
    def access_data(data_structure, key):
        """
        Access data[key] whether data is list or dict.
        Return None if key doesn't exist.
        """
        try:
            return data_structure[key]
        except LookupError: # TODO: Replace with appropriate parent exception
            return "Lookup Error"

    # Test with different data structures
    test_list = [10, 20, 30]
    test_dict = {"a": 1, "b": 2}

    print(f"List[1]: {access_data(test_list, 1)}")
    print(f"List[10]: {access_data(test_list, 10)}")
    print(f"Dict['a']: {access_data(test_dict, 'a')}")
    print(f"Dict['z']: {access_data(test_dict, 'z')}")

    # TODO 2: Order exception handlers correctly
    def parse_value(value):
        """
        Try to parse value as int, then float, then return as string.
        """
        # TODO: Fix the order of exception handlers
        try:
            return int(value)
        except(ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                return str(value)
    
    # Test parsing
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = parse_value(val)
        print(f"Parsing '{val}': {result} (type: {type(result).__name__})")

# Run the practice
practice_2_exception_hierarchy()

# Lecture 1 Unit 3
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            file = open(filename)
        except FileNotFoundError:
            # TODO: Handle missing file
            return "Error: File not found"
        except PermissionError:
            # TODO: Handle permission issues
            return "Error: File permission denied"
        else:
            # TODO: Process file content (only if opened successfully)
            data = file.read()
            processed = data.lower().split()
            print("Success: File processed")
        finally:
            # TODO: Ensure file is closed
            if file is not None:
                file.close()

# Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None
        
        def acquire(self):
            """Acquire resource - might fail."""
            # TODO: Implement with possible RuntimeError
            import random
            if random.choice([True, False]):
                raise RuntimeError("Failed to acquire resource")
            self.resource = f"{self.name} Connection Acquired"
            return self.resource

        def release(self):
            """Release resource - must always happen."""
            # TODO: Implement cleanup
            self.resource = None
            return f"{self.name} Connection Released"

        def use(self):
            """Use resource - only if acquired."""
            # TODO: Implement usage
            if not self.resource:
                raise RuntimeError("Resource not Acquired")
            return f"Using {self.resource}"

    # Test resource management
    rm = ResourceManager("Database")
    # TODO: Use try-except-else-finally to manage resource
    try:
        rm.acquire()
        result = rm.use()
        print(result)
    except RuntimeError as e:
        print(f"Error: {e}")
    else:
        print("Resource used successfully")
    finally:
        rm.release()

# Run the practice
practice_3_complete_pattern()


""" --- Lecture 2 --- """
# Lecture 2 Unit 2 (No Practice exercises for Unit 1)
def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""
        # TODO: Add __init__ with position and reason
        def __init__(self, row, col, reason):
            self.row = row
            self.col = col
            self.reason = reason
            super().__init__(f"Move: {row}, {col} is invalid: {reason}")

    class GameOverError(GameError):
        """Game has ended."""
        # TODO: Add __init__ with winner
        def __init__(self, winner):
            self.winner = winner
            super().__init__(f"Game is over! Winner: {winner}")

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False
            self.winner = None
        
        def make_move(self, row, col):
            # TODO: Raise GameOverError if game_over is True
            if self.game_over:
                raise GameOverError(self.winner)
            
            # TODO: Raise InvalidMoveError if position is out of bounds
            if not (0 <= row < 3 and 0 <= col < 3 ):
                raise InvalidMoveError (row, col, "Position out of bounds")
            
            # TODO: Raise InvalidMoveError if position is taken
            if self.board[row][col] != " ":
                raise InvalidMoveError(row, col, "Position already taken")
            
            self.board[row][col] = self.current_player
    
    # Test the game
    game = TicTacToe()
    
    test_moves = [
    (0, 0), # Valid
    (0, 0), # Already taken
    (5, 5), # Out of bounds
    ]
    
    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"✅ Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"❌ Invalid move: {e}")
        except GameOverError as e:
            print(f"🏁 Game over: {e}")

# Run the practice
practice_2_custom_exceptions()


# Lecture 2 Unit 3
def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)

    # TODO: Build a file processing system with proper error handling
    class FileProcessor:
        def __init__(self):
            self.processed_files = []
            self.failed_files = []
        
        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            # TODO: Implement with try-except-else-finally
            # TODO: Handle FileNotFoundError
            # TODO: Handle PermissionError
            # TODO: Handle general exceptions
            # TODO: Ensure file is closed
            file = None
            try:
                file = open(filename)
                data = file.read()
            except FileNotFoundError as e:
                self.failed_files.append(filename)
                return f"File Process Fail: {e}"
            except PermissionError as e:
                self.failed_files.append(filename)
                return f"File Process Fail: {e}"
            except Exception as e:
                self.failed_files.append(filename)
                return f"File Process Fail: {e}"
            else:
                self.processed_files.append(filename)
                return "File Process Success"
            finally:
                if file is not None:
                    file.close()    
        
        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            # TODO: Process each file
            # TODO: Continue on errors
            # TODO: Track successes and failures
            for file in directory:
                status = self.process_file(file)
                if status != "File Process Success":
                    self.failed_files.append(file)
                else:
                    self.processed_files.append(file)

        def get_report(self):
            """
            Get processing report.
            """
            # TODO: Return summary of processing
            return f"Successfully Processed: {self.processed_files}\nFailed:{self.failed_files}"
        
    # Test the processor
    processor = FileProcessor()

    test_files = [
    "valid.txt",
    "missing.txt",
    "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")

# Run the practice
practice_3_complete_system()