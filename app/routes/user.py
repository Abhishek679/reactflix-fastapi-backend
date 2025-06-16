from fastapi import APIRouter, HTTPException, status
from app.models.user import UserModel
from app.crud import (
    create_user, retrieve_user, retrieve_users,
    update_user, delete_user
)
from app.database import db, user_collection
from bson import ObjectId
from app.utils.auth import hash_password

router = APIRouter()


from fastapi import APIRouter, HTTPException, status
from app.models.user import UserModel
from app.database import db
from pymongo.errors import DuplicateKeyError

router = APIRouter()

@router.post("/", response_model=UserModel)
async def create_user(user: UserModel):
    user_dict = user.dict(by_alias=True)
    user_dict.pop("_id", None)  # remove _id if present so MongoDB generates it
    user_dict["password"] = hash_password(user.password)
    # Check if email already exists
    existing_user = await db["user_collection"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists. Please log in."
        )

    # Insert new user
    result = await db["user_collection"].insert_one(user_dict)
    created_user = await db["user_collection"].find_one({"_id": result.inserted_id})
    created_user["_id"] = str(created_user["_id"])  # convert ObjectId to str

    return UserModel(**created_user)


@router.get("/", response_model=list[UserModel])
async def get_users():
    users = await retrieve_users()
    return users

@router.get("/{id}", response_model=UserModel)
async def get_user(id: str):
    user = await retrieve_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{id}", response_model=UserModel)
async def update_existing_user(id: str, user: UserModel):
    user = user.dict(exclude_unset=True)
    updated_user = await update_user(id, user)
    if updated_user:
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{id}")
async def delete_existing_user(id: str):
    deleted = await delete_user(id)
    if deleted:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
