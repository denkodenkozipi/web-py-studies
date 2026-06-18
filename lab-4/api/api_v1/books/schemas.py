"""Book model"""

from pydantic import BaseModel
from typing_extensions import Annotated
from annotated_types import MinLen, MaxLen, Le


class BookBase(BaseModel):
    """Template for Book model"""
    id: int
    title: str
    slug: str
    pages: int
    year: int


class BookUpdate(BookBase):
    """ Annotated Book model """
    title: Annotated[str, MinLen(3), MaxLen(30)]
    slug: Annotated[str, MinLen(3), MaxLen(10)]
    year: Annotated[int, Le(2030)]


class BookTemplate(BookBase):
    """Ready model for crud operations """
