"""This module contains all the dependencies needed for the Movie API"""

from fastapi import HTTPException, Path
from .crud import get_movies_by_id


def validate_movie_id(movie_id: int = Path(..., description="The movie id")):
    """ Validate the movie id """

    movie = get_movies_by_id(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
