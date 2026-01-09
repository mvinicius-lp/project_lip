from datetime import datetime
from bson import ObjectId
from app.core.database import db
from app.utils.mongo_utils import convert_mongo_document, convert_mongo_list

COLLECTION = "disciplines"

class DisciplineRepositoryImpl:

    async def create(self, user_id: str, nome: str, cor: str):
        discipline = {
            "user_id": user_id,
            "nome": nome,
            "cor": cor,
            "criado_em": datetime.utcnow()
        }

        result = await db[COLLECTION].insert_one(discipline)
        discipline["_id"] = str(result.inserted_id)
        return discipline

    async def find_by_user(self, user_id: str):
        cursor = db[COLLECTION].find({"user_id": user_id})
        docs = await cursor.to_list(None)
        return convert_mongo_list(docs)

    async def update(self, discipline_id: str, data: dict) -> bool:
        result = await db[COLLECTION].update_one(
            {"_id": ObjectId(discipline_id)},
            {"$set": data}
        )
        return result.modified_count > 0

    async def delete(self, discipline_id: str) -> bool:
        result = await db[COLLECTION].delete_one(
            {"_id": ObjectId(discipline_id)}
        )
        return result.deleted_count > 0
