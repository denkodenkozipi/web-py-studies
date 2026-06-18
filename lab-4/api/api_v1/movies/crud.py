"""This module provides CRUD operations for Movies"""
from .schemas import MovieResponse

MOVIES_DATABASE = [
    MovieResponse(
        id=1,
        title="Movie 1",
        slug="mv-1",
        rating=2.5,
        year=2020,
    ),
    MovieResponse(
        id=2,
        title="Movie 2",
        slug="mv-2",
        rating=4.5,
        year=1993,
    ),
    MovieResponse(
        id=3,
        title="Movie 3",
        slug="mv-3",
        rating=4.3,
        year=2001,
    ),
]


def get_all_movies():
    """ Get all movies """
    return MOVIES_DATABASE


def get_movies_by_id(movie_id: int):
    """ Get movie by id """
    for movie in MOVIES_DATABASE:
        if movie.id == movie_id:
            return movie
    return None
