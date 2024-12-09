class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.times_read = 0

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book({self.id}, '{self.title}', '{self.author}')"

class Library:
    """A Library takes in an arbitrary amount of books, and has a
    dictionary of id numbers as keys, and Books as values.
    >>> b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    >>> b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    >>> b3 = Book(2, "The Fellowship of the Ring", "J.R.R. Tolkien")
    >>> l = Library(b1, b2, b3)
    >>> l.books[0].title
    'A Tale of Two Cities'
    >>> l.books[0].author
    'Charles Dickens'
    >>> l.read_book(1)
    'The Hobbit has been read 1 time(s)'
    >>> l.read_book(3) # No book with this id
    >>> l.read_author("Charles Dickens")
    'A Tale of Two Cities has been read 1 time(s)'
    >>> l.read_author("J.R.R. Tolkien")
    'The Hobbit has been read 2 time(s)\\nThe Fellowship of the Ring has been read 1 time(s)\\n'
    >>> b1.times_read
    1
    >>> b2.times_read
    2
    """

    def __init__(self, *args):
        """Takes in an arbitrary number of book objects and 
        puts them in a books dictionary which takes the book 
        id as the key and the book object as the value"""
        self.books = {}
        for book in args:
            self.books[book.id] = book

    def read_book(self, id):
        """Takes in an id of the book read,
        increments the number of times that book was read, 
        and returns a string describing that book's
        title and the number of times it has been read.
        (See doctests above for required formatting) """
        if id in self.books:
            self.books[id].times_read += 1
            return f"{self.books[id].title} has been read {self.books[id].times_read} time(s)"

    def read_author(self, author):
        """Takes in the name of an author, and
        returns a single string containing every
        book written by that author (and how many times it was read).
        The book descriptions should be formatted in 
        the same way as the as in the read_book method. 
        Hint: Each book output should be on a different line."""
        ret = []
        for id in self.books:
            if self.books[id].author == author:
                self.books[id].times_read += 1
                ret.append(f"{self.books[id].title} has been read {self.books[id].times_read} time(s)")
        return "\n".join(ret)

    def add_book(self, book):
        """Takes in a book object and adds it to the books
        dictionary if the book id is not already taken."""
        if not book.id in self.books:
            self.books[book.id] = book

    def __str__(self):
        strs = []
        for id in self.books:
            strs.append(str(self.books[id]))
        return ' | '.join(strs)

    def __repr__(self):
        strs = []
        for id in self.books:
            strs.append(repr(self.books[id]))
        return f"Library({', '.join(strs)})"
