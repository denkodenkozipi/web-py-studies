from fastapi import APIRouter, status
from .schemas import BookResponse
from .crud import StorageBooks, BookCreate

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def read_all_books():
    """get all books from storage"""
    return StorageBooks.get_all()


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookCreate):
    """create a new book in storage"""
    return StorageBooks.create(book_in)
