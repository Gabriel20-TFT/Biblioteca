from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Author(Base):
    __tablename__ = "author"
    author_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    books = relationship("Book", back_populates="author", cascade="all, delete-orphan")
