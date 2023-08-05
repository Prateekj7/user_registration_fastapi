from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

# Function to create the PostgreSQL engine
def create_postgres_engine():
    # Replace with your PostgreSQL connection URL
    DATABASE_URL = "postgresql://username:password@localhost/dbname"
    return create_engine(DATABASE_URL)


# Function to create a PostgreSQL session
def create_postgres_session(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)()
