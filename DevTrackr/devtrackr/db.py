from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL') or 'postgresql://postgres:postgres@localhost:5432/devtrackr_db'
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
from .models import Base
def init_db():
    Base.metadata.create_all(bind=engine)
if __name__ == '__main__':
    init_db()
    print('Initialized DB.')
