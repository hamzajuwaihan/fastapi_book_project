from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    description: str
    author_id: int

class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True

class AuthorBase(BaseModel):
    name: str
    age: int

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True