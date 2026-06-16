"""This module contains all dependencies needed for the Book API"""

from fastapi import HTTPException, Path
from .crud import get_book_by_id


def validate_book_id(book_id: int = Path(..., description="The Book ID")):
    """Validates The Book ID"""

    book = get_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
