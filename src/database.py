from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import MetaData


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/bookdb")


engine = create_engine(DATABASE_URL, echo=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


metadata = MetaData()


metadata.create_all(engine)
