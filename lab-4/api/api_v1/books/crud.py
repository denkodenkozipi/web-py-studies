"""This module provides CRUD operations for Book"""

from .schemas import BookResponse, BookCreate
from fastapi import HTTPException, status


class StorageBooks:
    """Class for storing storage related operations"""
    _id_counter = 2

    _storage: dict[str, BookResponse] = {
        "harry-potter-2002": BookResponse(
            id=1,
            title="Harry Potter",
            slug="harry-potter-2002",
            pages=400,
            year=2002,
            description="Some description",
        ),
        "lords-of-the-ring-2000": BookResponse(
            id=2,
            title="Lord's of the ring",
            slug="lords-of-the-ring-2000",
            pages=800,
            year=2000,
            description="Some description",
        )

    }

    @classmethod
    def get_all(cls) -> list[BookResponse]:
        """ Get all books"""
        return list(cls._storage.values())

    @classmethod
    def get_by_slug(cls, slug: str) -> BookResponse:
        """ Get book by slug or raise 404"""
        book = cls._storage.get(slug)

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with slug '{slug}' does not exist",
            )

        return book

    @classmethod
    def get_by_id(cls, book_id: int) -> BookResponse:
        """Get book by id or raise 404"""
        for book in cls._storage.values():
            if book.id == book_id:
                return book

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id '{book_id}' does not exist",
        )

    @classmethod
    def create(cls, book_in: BookCreate) -> BookResponse:
        """Create new book in storage"""
        slug_title = book_in.title.lower().replace("'", "").replace(" ", "-")
        generated_slug = f"{slug_title}-{book_in.year}"

        if generated_slug in cls._storage:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Book with slug '{generated_slug}' already exists",
            )

        cls._id_counter += 1

        new_book = BookResponse(
            id=cls._id_counter,
            title=book_in.title,
            pages=book_in.pages,
            year=book_in.year,
            description=book_in.description,
            slug=generated_slug,
        )

        cls._storage[generated_slug] = new_book
        return new_book
