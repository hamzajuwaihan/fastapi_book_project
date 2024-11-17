from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src import crud, models, database

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=models.Book)
def create_book(book: models.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

@app.get("/books/", response_model=list[models.Book])
def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = crud.get_books(db=db, skip=skip, limit=limit)
    return books

@app.post("/authors/", response_model= models.Author)
def create_author(author: models.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db= db, author = author)

@app.get("/authors/{author_id}", response_model=models.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):

    author = crud.get_author_by_id(db, author_id)

    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    return author