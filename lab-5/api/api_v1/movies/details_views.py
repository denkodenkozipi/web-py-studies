from fastapi import APIRouter, status, Depends
from .crud import StorageMovie
from .dependencies import validate_movie_by_id, validate_movie_by_slug
from .schemas import MovieResponse, MovieUpdate

responses_404 = {
    status.HTTP_404_NOT_FOUND: {
        "description": "Movie not found",
        "content": {
            "application/json": {
                "example": {"detail": "Movie does not exist"}
            }
        },
    }
}

router = APIRouter(prefix="/movies", tags=["Movies"], responses=responses_404)


@router.get("/id/{movie_id}", response_model=MovieResponse)
def read_movie_by_id(movie: MovieResponse = Depends(validate_movie_by_id)):
    """get a movie by its id"""
    return movie


@router.get("/{slug}", response_model=MovieResponse)
def read_movie_by_slug(movie: MovieResponse = Depends(validate_movie_by_slug)):
    """get a movie by its slug"""
    return movie


@router.delete("/id/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie_by_id(movie: MovieResponse = Depends(validate_movie_by_id)):
    """delete a movie by its id"""
    StorageMovie.delete_by_id(movie.id)
    return None


@router.delete("/{slug}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie_by_slug(movie: MovieResponse = Depends(validate_movie_by_slug)):
    """delete a movie by its slug"""
    StorageMovie.delete_by_slug(movie.slug)
    return None


@router.put("/{slug}", response_model=MovieResponse)
def update_movie(movie_in: MovieUpdate, movie: MovieResponse = Depends(validate_movie_by_slug)):
    """ Update a movie completely via PUT """
    return StorageMovie.update(current_movie=movie, movie_in=movie_in)
