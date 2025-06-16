from app.database import user_collection, db
from app.models.user import UserModel
from bson import ObjectId

async def create_user(user_data: dict) -> dict:
    user = await db["user_collection"].insert_one(user_data)
    new_user = await db["user_collection"].find_one({"_id": user.inserted_id})
    return new_user

async def retrieve_user(id: str) -> dict:
    user = await db["user_collection"].find_one({"_id": ObjectId(id)})
    return user

async def retrieve_users() -> list[UserModel]:
    users = []
    async for user in db["user_collection"].find():
        print(user)
        user["_id"] = str(user["_id"])  # convert ObjectId to str
        users.append(UserModel(**user))
    return users

async def update_user(id: str, data: dict):
    if len(data) < 1:
        return False
    user = await db["user_collection"].find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await db["user_collection"].update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user.modified_count > 0:
            return await db["user_collection"].find_one({"_id": ObjectId(id)})
    return False

async def delete_user(id: str):
    user = await db["user_collection"].find_one({"_id": ObjectId(id)})
    if user:
        delete_result = await db["user_collection"].delete_one({"_id": ObjectId(id)})
        if delete_result.deleted_count > 0:
            return True
    return False
