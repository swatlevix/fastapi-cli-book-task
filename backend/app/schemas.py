from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=150, description="Title of the book")
    author: str = Field(..., min_length=2, max_length=100, description="Author of the book")

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True