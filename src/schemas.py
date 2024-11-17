from sqlalchemy import ForeignKey, Table, Column, Integer, String, MetaData
from src.database import engine

metadata = MetaData()

book_table = Table('books', metadata,
                   Column('id', Integer, primary_key=True, index=True),
                   Column('title', String, index=True),
                   Column('author', String),
                   Column('description', String),
                   Column('author_id', Integer, ForeignKey('authors.id')))

author_table = Table('authors', metadata,
                     Column('id', Integer, primary_key=True, index=True),
                     Column('name', String),
                     Column('age', Integer))

metadata.create_all(engine)
