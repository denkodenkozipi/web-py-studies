from fastapi import APIRouter
from .movies.list_views import router as movie_list_router
from .movies.details_views import router as movies_details_router
from .books.list_views import router as books_list_router
from .books.details_views import router as books_details_router

router = APIRouter(prefix="/v1")

router.include_router(movie_list_router)
router.include_router(movies_details_router)
router.include_router(books_list_router)
router.include_router(books_details_router)
