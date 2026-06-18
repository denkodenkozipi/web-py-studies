"""Book endpoints"""

from fastapi import APIRouter, Depends, status

from .crud import StorageBooks
from .dependencies import validate_book_id
from .schemas import BookResponse, BookCreate

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def read_all_books():
    """get all books from storage"""
    return StorageBooks.get_all()


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookCreate):
    """create a new book in storage"""
    return StorageBooks.create(book_in)


@router.get("/id/{book_id}", response_model=BookResponse)
def read_book_by_id(book: BookResponse = Depends(validate_book_id)):
    """get a book by its id"""
    return book


@router.get("/{slug}", response_model=BookResponse)
def read_book_by_slug(slug: str):
    """get a book by its slug"""
    return StorageBooks.get_by_slug(slug)
