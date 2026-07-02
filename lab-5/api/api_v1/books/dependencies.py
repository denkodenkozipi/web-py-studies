"""This module contains all dependencies needed for the Book API"""

from fastapi import Path
from .crud import StorageBooks
from .schemas import BookResponse


def validate_book_by_id(book_id: int = Path(..., description="The id of the book to get")) -> BookResponse:
    """Validate book id"""
    return StorageBooks.get_by_id(book_id)

def validate_book_by_slug(slug: str = Path(..., description="The slug of the book to get")) -> BookResponse:
    """ Validate book slug """
    return StorageBooks.get_by_slug(slug)