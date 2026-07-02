""" Movie model """
from pydantic import BaseModel, Field
from typing import Optional

class MovieBase(BaseModel):
    """ Base Movie model with common fields """
    title: str = Field(..., description="Movie title")
    rating: float = Field(..., description="Movie rating", ge=0.00, le=5.00)
    year: int = Field(..., description="Movie year released", ge=1895, le=2030)
    description: str | None = Field(default=None, description="Movie description")


class MovieCreate(MovieBase):
    """Model for creating new movies in the database"""
    pass


class MovieResponse(MovieBase):
    """Response schema for a single movie with slug identifier"""
    slug: str = Field(..., description="Specific movie slug")
    id: int = Field(..., description="Specific movie id")

    model_config = {"from_attributes": True}


class MovieUpdate(MovieBase):
    """Model for updating an existing movie completely via PUT """
    pass


class MoviePatch(MovieBase):
    """ Model for updating an existing movie partially via PATCH """
    title: Optional[str] = None
    rating: Optional[float] = None
    year: Optional[int] = None
    description: Optional[str] = None
