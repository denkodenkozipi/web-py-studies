""" Movie model """
from pydantic import BaseModel, Field


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

    model_config = {"from_attributes": True}
