# database.py
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["mydatabase"]  # like CREATE DATABASE mydatabase
collection = db["users"]   # like CREATE TABLE users
