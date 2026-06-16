"""This module contains all the dependencies needed for the Movie API"""

from fastapi import HTTPException, Path
from typing import Annotated
from annotated_types import MinLen, MaxLen, Ge, Le
from pydantic import BaseModel


class MovieBase(BaseModel):
    """ Template Movie model for crud operations """
    id: int
    title: str
    slug: str
    rating: float
    year: int


class MovieUpdate(MovieBase):
    """ Annotated Movie model for crud operations """
    title: Annotated[str, MinLen(3), MaxLen(30)]
    slug: Annotated[str, MinLen(3), MaxLen(10)]
    rating: Annotated[float, Ge(0.00), Le(5.00)]
    year: Annotated[int, Ge(1895), Le(2030)]


class MovieTemplate(MovieBase):
    """Ready model for crud operations """


def validate_movie_id(movie_id: int = Path(..., description="The movie id")):
    """ Validate the movie id """
    from .crud import get_movies_by_id
    # yeah, that's dumb. but the best way is :)

    movie = get_movies_by_id(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
