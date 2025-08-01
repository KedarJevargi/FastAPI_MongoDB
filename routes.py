# routes.py
from fastapi import APIRouter, HTTPException
from models import UserCreate, User
from crud import create_user, get_user, get_all_users, update_user, delete_user

router = APIRouter()

@router.post("/users", response_model=User)
async def create(user: UserCreate):
    return await create_user(user)

@router.get("/users/{user_id}", response_model=User)
async def read(user_id: str):
    user = await get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users", response_model=list[User])
async def read_all():
    return await get_all_users()

@router.put("/users/{user_id}")
async def update(user_id: str, user: UserCreate):
    success = await update_user(user_id, user)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}

@router.delete("/users/{user_id}")
async def delete(user_id: str):
    success = await delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
