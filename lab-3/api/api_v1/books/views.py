"""Book endpoints"""
from fastapi import APIRouter, Depends
from .crud import get_all_books
from .dependencies import validate_book_id, BookTemplate

from books.dependencies import BookTemplate

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookTemplate])
def read_all_books():
    """Get all books"""
    return get_all_books()


@router.get("/{book_id}", response_model=BookTemplate)
def read_book(book: BookTemplate = Depends(validate_book_id)):
    """Get a book by its id"""
    return book
