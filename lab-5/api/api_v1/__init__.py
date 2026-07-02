from fastapi import APIRouter
from .movies.list_views import router as movie_list_router
from .movies.details_views import router as movies_details_router
from .books.views import router as books_router

router = APIRouter(prefix="/v1")

router.include_router(movie_list_router)
router.include_router(movies_details_router)
router.include_router(books_router)
