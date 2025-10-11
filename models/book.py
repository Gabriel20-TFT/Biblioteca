from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    author_id = Column(Integer, ForeignKey("author.author_id"), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    available = Column(Integer, default=1)  # 1 = available, 0 = not

    author = relationship("Author", back_populates="books")
    loans = relationship("Loan", back_populates="book", cascade="all, delete-orphan")
