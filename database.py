from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Change username & password
DATABASE_URL = "mysql+pymysql://root:12345@localhost/product_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()