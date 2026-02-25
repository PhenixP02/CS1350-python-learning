
## Phenix Payton
## CS1350
## Homework 4 
## 2/27/26

class Book:
    def __init__(self, title, author, total_pages, isbn):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.isbn = isbn

        # TODO: Set private _current_page to 0
        self._current_page = 0
    
    @property
    def current_page(self):
        # TODO: Return _current_page
        return self._current_page
    
    @property
    def progress(self):
        # TODO: Return percentage string like "45.0%"
        return f"{round(self._current_page / self.total_pages * 100, 1)}%"
    
    def read(self, pages):
        # TODO: Advance current page by pages
        # Cap at total_pages
        # Print error if pages is not positive
        # Return new current page
        if pages <= 0:
            print("Error! Must advance atleast 1 page.")
            return self._current_page
        
        self._current_page += pages
        if self._current_page > self.total_pages:
            self._current_page = self.total_pages
           
        return self._current_page
    
    def reset(self):
        # TODO: Set _current_page back to 0
        self._current_page = 0
        return f"{self.title} Current page reset back to 0."
    
    def __str__(self):
        # TODO: Return formatted string
        return f"'{self.title}' by {self.author}. {self.total_pages} total pages ISBN: {self.isbn}"


class TextBook(Book):
    def __init__(self, title, author, total_pages, isbn, subject, edition):
        # TODO: Call parent constructor
        super().__init__(title, author, total_pages, isbn)
        # TODO: Store subject and edition
        self.subject = subject
        self.edition = edition
        # TODO: Initialize private _highlights dictionary
        self._highlights = {}

    def highlight(self, page, text):
        # TODO: Add highlight to _highlights[page]
        # Print error if page is out of range
        if page > self.total_pages or page <= 0:
            print("Error! Can't create highlight, page is out of textbook range.")
            return
        if page not in self._highlights:
            self._highlights[page] = [] # Create list of highlights for page
            
        self._highlights[page].append(text) 


    def get_highlights(self, page):
        # TODO: Return list of highlights for the page
        # Return empty list if none
        if page not in self._highlights:
            self._highlights[page] = []
        return self._highlights[page]

    def __str__(self):
        # TODO: Return formatted string with edition and subject
        return f"'{self.title}' by {self.author}. {self.total_pages} total pages, ISBN: {self.isbn}, Subject: {self.subject}, Edition: {self.edition}"

# Test your code
if __name__ == "__main__":
    # --- Test Book ---
    print("=== Book Tests ===")
    novel = Book("1984", "George Orwell", 328, "978-0451524935")
    print(novel)
    novel.read(50)
    print(f"Current page: {novel.current_page}")
    print(f"Progress: {novel.progress}")
    novel.read(-10) # Should print error
    novel.read(400) # Should cap at 328
    print(f"Current page: {novel.current_page}")
    print(f"Progress: {novel.progress}")
    novel.reset()
    print(f"After reset: page {novel.current_page}")
    print("\n=== TextBook Tests ===")
    # --- Test TextBook ---
    cs_book = TextBook("Intro to Python", "Deitel", 880, "978-0135404676", "Computer Science", 1)
    print(cs_book)
    cs_book.read(120)
    print(f"Progress: {cs_book.progress}")
    cs_book.highlight(45, "Dictionaries store key-value pairs")
    cs_book.highlight(45, "Keys must be immutable")
    cs_book.highlight(72, "Sets cannot contain duplicates")
    cs_book.highlight(0, "Important note") # Should print error
    print(f"Page 45 highlights: {cs_book.get_highlights(45)}")
    print(f"Page 72 highlights: {cs_book.get_highlights(72)}")
    print(f"Page 1 highlights: {cs_book.get_highlights(1)}")    