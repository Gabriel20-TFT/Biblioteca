from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(45), unique=True, nullable=False)
    email = Column(String(64), unique=True, nullable=True)
    hashed_password = Column(String(128), nullable=False)

    loans = relationship("Loan", back_populates="user", cascade="all, delete-orphan")
