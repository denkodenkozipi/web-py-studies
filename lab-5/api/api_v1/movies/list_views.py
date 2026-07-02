from fastapi import APIRouter, status
from .crud import MovieResponse, StorageMovie, MovieCreate

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/", response_model=list[MovieResponse])
def read_all_movies():
    """get all movies from storage"""
    return StorageMovie.get_all()


@router.post("/", response_model=MovieResponse, status_code=status.HTTP_201_CREATED)
def create_movie(movie_in: MovieCreate):
    """create a new movie in storage"""
    return StorageMovie.create(movie_in)

