"""This module contains all dependencies needed for the Book API"""

from annotated_types import MinLen, MaxLen, Le
from fastapi import HTTPException, Path
from pydantic import BaseModel
from typing_extensions import Annotated


class BookBase(BaseModel):
    """Template for Book model"""
    id: int
    title: str
    slug: str
    pages: int
    year: int


class BookUpdate(BookBase):
    """ Annotated Book model """
    title: Annotated[str, MinLen(3), MaxLen(30)]
    slug: Annotated[str, MinLen(3), MaxLen(10)]
    year: Annotated[int, Le(2030)]


class BookTemplate(BookBase):
    """Ready model for crud operations """


def validate_book_id(book_id: int = Path(..., description="The Book ID")):
    """Validates The Book ID"""
    from .crud import get_book_by_id
    book = get_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
