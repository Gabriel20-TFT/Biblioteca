from fastapi import APIRouter, HTTPException
from models.user import User
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
def register(user: User):
    existing = UserService.find_by_name(user.name)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    return UserService.add_user(user)

@router.post("/login")
def login(payload: User):
    u = UserService.authenticate(payload.name, payload.password)
    if not u:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message":"login successful"} 
