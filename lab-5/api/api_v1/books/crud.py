"""This module provides CRUD operations for Book"""

from .schemas import BookResponse, BookCreate, BookUpdate, BookPatch
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

    @classmethod
    def delete_by_id(cls, book_id: int) -> BookResponse:
        """ Delete book by id or raise 404 """
        for slug, book in cls._storage.items():
            if book.id == book_id:
                del cls._storage[slug]
                return book

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id '{book_id}' does not exist",
        )

    @classmethod
    def delete_by_slug(cls, slug: str) -> BookResponse:
        """ Delete book by slug or raise 404 """
        book = cls._storage.pop(slug)

        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with slug '{slug}' does not exist"
            )

        return book

    @classmethod
    def update(cls, current_book: BookResponse, book_in: BookUpdate) -> BookResponse:
        """ Update a book completely (PUT) """
        slug_title = book_in.title.lower().replace("'", "").replace(" ", "-")
        new_slug = f"{slug_title}-{book_in.year}"

        if new_slug != current_book.slug and new_slug in cls._storage:
            raise HTTPException(
                status_code=status.HTTP_404_BAD_REQUEST,
                detail=f"Book with slug '{new_slug}' already exists",
            )

        if new_slug != current_book.slug:
            cls._storage.pop(current_book.slug, None)

        current_book.title = book_in.title
        current_book.pages = book_in.pages
        current_book.year = book_in.year
        current_book.description = book_in.description
        current_book.slug = new_slug

        cls._storage[new_slug] = current_book
        return current_book

    @classmethod
    def patch(cls, current_book: BookResponse, book_in: BookPatch) -> BookResponse:
        """ Patch a book """
        update_data = book_in.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(current_book, field, value)

        if "title" in update_data or "year" in update_data:
            slug_title = current_book.title.lower().replace("'", "").replace(" ", "-")
            new_slug = f"{slug_title}{current_book.year}"

            if new_slug != current_book.slug:
                if new_slug in cls._storage:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Book with slug '{new_slug}' already exists",
                    )

                cls._storage.pop(current_book.slug, None)
                current_book.slug = new_slug
                cls._storage[new_slug] = current_book

        else:
            cls._storage[current_book.slug] = current_book

        return current_book
