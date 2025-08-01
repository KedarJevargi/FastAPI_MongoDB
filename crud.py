# crud.py
from models import UserCreate, User
from database import collection
from bson import ObjectId

async def create_user(user: UserCreate) -> User:
    result = await collection.insert_one(user.dict())
    return User(id=str(result.inserted_id), **user.dict())

async def get_user(user_id: str) -> User | None:
    doc = await collection.find_one({"_id": ObjectId(user_id)})
    if doc:
        return User(id=str(doc["_id"]), name=doc["name"], email=doc["email"])
    return None

async def get_all_users() -> list[User]:
    users = []
    async for doc in collection.find():
        users.append(User(id=str(doc["_id"]), name=doc["name"], email=doc["email"]))
    return users

async def update_user(user_id: str, user: UserCreate) -> bool:
    result = await collection.update_one(
        {"_id": ObjectId(user_id)}, {"$set": user.dict()}
    )
    return result.modified_count > 0

async def delete_user(user_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0
