from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from src.database import engine
from src import models, schemas

def get_books(db: Session, skip: int = 0, limit: int = 10):
    query = select(models.book_table).offset(skip).limit(limit)
    result = db.execute(query)
    return result.fetchall() 

def create_book(db: Session, book: models.BookCreate):

    insert_stmt = insert(models.book_table).values(
        title=book.title,
        author_id=book.author_id,  
        description=book.description
    )
    db.execute(insert_stmt)
    db.commit()


    result = db.execute(models.book_table.select().where(models.book_table.c.title == book.title).limit(1))
    return result.fetchone()  

def create_author(db: Session, author: models.AuthorCreate):
    query = insert(models.author_table).values(name = author.name, age= author.age)
    db.execute(query)
    db.commit()

    result = db.execute(select(models.author_table).where(models.author_table.c.name == author.name).limit(1))
    return result.fetchone()

def get_author_by_id(db: Session, author_id: int):

    query = select(models.author_table).where(models.author_table.c.id == author_id)
    

    result = db.execute(query)
    

    author = result.fetchone()  


    return author if author else None