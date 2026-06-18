"""Movie endpoints"""

from fastapi import APIRouter, Depends
from .crud import get_all_movies
from .dependencies import validate_movie_id
from .schemas import MovieResponse

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/", response_model=list[MovieResponse])
def read_all_movies():
    """get all movies"""
    return get_all_movies()


@router.get("/{movie_id}", response_model=MovieResponse)
def read_movie(movie: MovieResponse = Depends(validate_movie_id)):
    """get a movie by its id"""
    return movie
