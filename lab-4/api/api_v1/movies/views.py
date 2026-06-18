"""Movie endpoints"""

from fastapi import APIRouter, Depends, status

from .crud import StorageMovie
from .dependencies import validate_movie_id
from .schemas import MovieResponse, MovieCreate

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/", response_model=list[MovieResponse])
def read_all_movies():
    """get all movies from storage"""
    return StorageMovie.get_all()


@router.post("/", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
def create_movie(movie_in: MovieCreate):
    """create a new movie in storage"""
    return StorageMovie.create(movie_in)


@router.get("/id/{movie_id}", response_model=MovieResponse)
def read_movie_by_id(movie: MovieResponse = Depends(validate_movie_id)):
    """get a movie by its id"""
    return movie


@router.get("/{slug}", response_model=MovieResponse)
def read_movie_by_slug(slug: str):
    """get a movie by its slug"""
    return StorageMovie.get_by_slug(slug)
