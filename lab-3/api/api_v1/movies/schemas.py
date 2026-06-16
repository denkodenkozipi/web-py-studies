""" Movie model """

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
