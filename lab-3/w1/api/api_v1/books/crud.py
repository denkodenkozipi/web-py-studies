"""This module provides CRUD operations for Book"""

from .dependencies import BookTemplate

BOOKS_DATABASE = [
    BookTemplate(
        id=1,
        title="Book 1",
        slug="bk-1",
        pages=1200,
        year=1999,
    ),
    BookTemplate(
        id=2,
        title="Book 2",
        slug="bk-2",
        pages=2000,
        year=1935,
    ),
    BookTemplate(
        id=3,
        title="Book 3",
        slug="bk-3",
        pages=500,
        year=2015,
    ),
]

def get_all_books():
    """Get all books"""
    return BOOKS_DATABASE

def get_book_by_id(book_id: int):
    """Get a book by its id"""
    for book in BOOKS_DATABASE:
        if book.id == book_id:
            return book
    return None