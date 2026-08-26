"""
Task:
Implement a small library management system using object-oriented programming.

Requirements:
- Create `Book`, `Member`, and `Library` classes.
- A Book has a title, author, and unique ISBN.
- A Member has a unique member ID and a name.
- A Library manages books and members.
- A library member can borrow books.
- A borrowed book cannot be borrowed by another member.
- A member can return a book they currently borrowed.
- The library can find books by author.
- The library can find the most borrowed book.

Rules:
- Book title and author cannot be empty.
- ISBN cannot be empty.
- Member ID and name cannot be empty.
- A book can be borrowed by only one member at a time.
- A member cannot borrow the same book twice.
- Borrowing an unavailable book must raise `ValueError`.
- Returning a book that the member did not borrow must raise `ValueError`.
- Adding a book with an existing ISBN must raise `ValueError`.
- Adding a member with an existing member ID must raise `ValueError`.

Methods:

Book:
    - title
    - author
    - isbn
    - borrow_count

Member:
    - member_id
    - name
    - borrowed_books

Library:
    - add_book(book)
    - add_member(member)
    - borrow_book(member_id, isbn)
    - return_book(member_id, isbn)
    - find_books_by_author(author)
    - most_borrowed_book()

Algorithm:
- `find_books_by_author()` filters books by author.
- `most_borrowed_book()` finds the book with the highest borrow count.
- Borrowing and returning require finding the correct objects and updating their state.
"""


class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        if not title or not author or not isbn:
            raise ValueError("Title, author and isbn can not be empty.")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrow_count = 0
        self.borrowed_by: Member | None = None


class Member:
    def __init__(self, member_id: str, name: str) -> None:
        if not member_id or not name:
            raise ValueError("Member ID and name can not be empty.")

        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []
        self.members: list[Member] = []

    def _find_member(self, member_id: str) -> Member | None:
        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def _find_book(self, isbn: str) -> Book | None:
        for book in self.books:
            if book.isbn == isbn:
                return book

        return None

    def add_book(self, book: Book) -> None:
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                raise ValueError("Book already added.")

        self.books.append(book)

    def add_member(self, member: Member) -> None:
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                raise ValueError("Member already added.")

        self.members.append(member)

    def borrow_book(self, member_id: str, isbn: str) -> None:
        member = self._find_member(member_id)
        book = self._find_book(isbn)

        if member is None:
            raise ValueError("Member does not exist in Library.")

        if book is None:
            raise ValueError("Book does not exist in Library.")

        if book.borrowed_by is not None:
            raise ValueError("Book currently borrowed.")

        if book in member.borrowed_books:
            raise ValueError("Member already borrowed current book.")

        book.borrow_count += 1
        book.borrowed_by = member
        member.borrowed_books.append(book)

    def return_book(self, member_id: str, isbn: str) -> None:
        member = self._find_member(member_id)
        book = self._find_book(isbn)

        if member is None:
            raise ValueError("Member does not exist in Library.")

        if book is None:
            raise ValueError("Book does not exist in Library.")

        if book not in member.borrowed_books:
            raise ValueError("Book was not borrowed by current member.")

        book.borrowed_by = None
        member.borrowed_books.remove(book)

    def find_books_by_author(self, author: str) -> list[Book]:
        books_by_author = []

        for book in self.books:
            if book.author == author:
                books_by_author.append(book)

        return books_by_author

    def most_borrowed_book(self) -> Book | None:
        if not self.books:
            return None

        return max(self.books, key=lambda book: book.borrow_count)
