from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin, UserResponse
from utils.security import hash_password, verify_password

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if len(user_in.password.encode("utf-8")) > 72:
        raise HTTPException(
            status_code=400,
            detail="Password too long (max 72 bytes)"
        )

    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hash_password(user_in.password)
    )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except IntegrityError as e:
        db.rollback()

        if "username" in str(e.orig):
            detail = "Username already exists"
        elif "email" in str(e.orig):
            detail = "Email already exists"
        else:
            detail = "Duplicate entry"

        raise HTTPException(status_code=409, detail=detail)


@router.post("/login")
def login(payload: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.username == payload.username).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")


    if not verify_password(payload.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": f"Welcome, {db_user.username}!"}
