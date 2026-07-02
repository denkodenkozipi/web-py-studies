"""This module contains all the dependencies needed for the Movie API"""

from fastapi import Path
from .crud import StorageMovie
from .schemas import MovieResponse


def validate_movie_id(movie_id: int = Path(..., description="The id of the movie to get")) -> MovieResponse:
    """Validate movie id"""
    return StorageMovie.get_by_id(movie_id)

def validate_movie_by_slug(slug: str = Path(..., description="The slug of the movie to get")) -> MovieResponse:
    """Validate movie slug"""
    return StorageMovie.get_by_slug(slug)