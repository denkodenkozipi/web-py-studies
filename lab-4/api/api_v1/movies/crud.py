"""This module provides CRUD operations for Movies"""

from .schemas import MovieResponse, MovieCreate
from fastapi import HTTPException, status


class StorageMovie:
    """Class for storing storage related operations"""
    _id_counter = 2

    _storage: dict[str, MovieResponse] = {
        "harry-potter-2002": MovieResponse(
            id=1,
            title="Harry Potter",
            slug="harry-potter-2002",
            rating=4.9,
            year=2002,
            description="Some description",
        ),
        "lords-of-the-ring-2000": MovieResponse(
            id=2,
            title="Lord's of the ring",
            slug="lords-of-the-ring-2000",
            rating=4.7,
            year=2000,
            description="Some description",
        )

    }

    @classmethod
    def get_all(cls) -> list[MovieResponse]:
        """ Get all movies"""
        return list(cls._storage.values())

    @classmethod
    def get_by_slug(cls, slug: str) -> MovieResponse:
        """ Get movie by slug or raise 404"""
        movie = cls._storage.get(slug)

        if not movie:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Movie with slug '{slug}' does not exist",
            )

        return movie

    @classmethod
    def get_by_id(cls, movie_id: int) -> MovieResponse:
        """Get movie by id or raise 404"""
        for movie in cls._storage.values():
            if movie.id == movie_id:
                return movie

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Movie with id '{movie_id}' does not exist",
        )

    @classmethod
    def create(cls, movie_in: MovieCreate) -> MovieResponse:
        """Create new movie in storage"""
        slug_title = movie_in.title.lower().replace("'", "").replace(" ", "-")
        generated_slug = f"{slug_title}-{movie_in.year}"

        if generated_slug in cls._storage:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Movie with slug '{generated_slug}' already exists",
            )

        cls._id_counter += 1

        new_movie = MovieResponse(
            id=cls._id_counter,
            title=movie_in.title,
            rating=movie_in.rating,
            year=movie_in.year,
            description=movie_in.description,
            slug=generated_slug,
        )

        cls._storage[generated_slug] = new_movie
        return new_movie
