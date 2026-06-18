"""Book model"""

from pydantic import BaseModel, Field


class BookBase(BaseModel):
    """Base Book model with common fields"""
    title: str = Field(..., description="Title of the book")
    pages: int = Field(..., description="Number of pages")
    year: int = Field(..., description="Year of the book", le=2030)
    description: str | None = Field(default=None, description="Book description")

class BookCreate(BookBase):
    """Model for creating new book in the database"""
    pass

class BookResponse(BookBase):
    """Response model for a single book with common identifier"""
    slug: str = Field(..., description="Specific book slug")
    id: int = Field(..., description="Specific id of the book")

    model_config = {"from_attributes": True}