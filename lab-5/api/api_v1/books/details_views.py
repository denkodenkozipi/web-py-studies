from fastapi import APIRouter, Depends, status

from .crud import StorageBooks
from .dependencies import validate_book_by_id, validate_book_by_slug
from .schemas import BookResponse, BookUpdate, BookPatch

responses_404 = {
    status.HTTP_404_NOT_FOUND: {
        "description": "Book not found",
        "content": {
            "application/json": {
                "example": {"detail": "Book does not exist"}
            }
        },
    }
}

router = APIRouter(prefix="/books", tags=["Books"], responses=responses_404)


@router.get("/id/{book_id}", response_model=BookResponse)
def read_book_by_id(book: BookResponse = Depends(validate_book_by_id)):
    """get a book by its id"""
    return book


@router.get("/{slug}", response_model=BookResponse)
def read_book_by_slug(book: BookResponse = Depends(validate_book_by_slug)):
    """get a book by its slug"""
    return book


@router.delete("/id/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_id(book: BookResponse = Depends(validate_book_by_id)):
    """ delete a book by its id """
    StorageBooks.delete_by_id(book.id)
    return None


@router.delete("/{slug}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_slug(book: BookResponse = Depends(validate_book_by_slug)):
    """ delete a book by its slug """
    StorageBooks.delete_by_slug(book.slug)
    return None


@router.put("/{slug}", response_model=BookResponse)
def update_book(book_in: BookUpdate, book: BookResponse = Depends(validate_book_by_slug)):
    """ Update a book completely via PUT """
    return StorageBooks.update(current_book=book, book_in=book_in)


@router.patch("/{slug}", response_model=BookResponse)
def patch_book(
        book_in: BookPatch,
        book: BookResponse = Depends(validate_book_by_slug),
):
    """ patch a book """
    return StorageBooks.patch(current_book=book, book_in=book_in)
