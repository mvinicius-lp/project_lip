from datetime import datetime, timedelta
from app.core.database import db
from app.utils.mongo_utils import convert_mongo_document, convert_mongo_list
from bson import ObjectId

COLLECTION = "revisions"

class RevisionRepositoryImpl:

    async def create(self, revision):
        revision_dict = {
            "user_id": revision.user_id,
            "study_id": revision.study_id,
            "data_revisao": revision.data_revisao,
            "realizada": revision.realizada
        }

        result = await db[COLLECTION].insert_one(revision_dict)
        revision_dict["_id"] = str(result.inserted_id)
        return revision_dict
    
    async def find_by_date(self, user_id, date):
        start = datetime(date.year, date.month, date.day)
        end = start + timedelta(days=1)

        cursor = db[COLLECTION].find({
            "user_id": user_id,
            "data_revisao": {"$gte": start, "$lt": end}
        })

        docs = await cursor.to_list(None)
        return convert_mongo_list(docs)

    async def find_future(self, user_id, date):
        cursor = db[COLLECTION].find({
            "user_id": user_id,
            "data_revisao": {"$gt": date}
        })
        docs = await cursor.to_list(None)
        return convert_mongo_list(docs)

    async def find_past(self, user_id, date):
        start = datetime(date.year, date.month, date.day)
        end = start + timedelta(days=1)

        cursor = db[COLLECTION].find({
            "user_id": user_id,
            "data_revisao": {"$gte": start, "$lt": end}
        })

        docs = await cursor.to_list(None)
        return convert_mongo_list(docs)

    async def find_by_id(self, revision_id):
        revision = await db[COLLECTION].find_one({"_id": ObjectId(revision_id)})
        return convert_mongo_document(revision)

    async def find_completed(self, user_id):
        cursor = db[COLLECTION].find({
            "user_id": user_id,
            "realizada": True
        })

        docs = await cursor.to_list(None)
        return convert_mongo_list(docs)

    async def update(self, revision_id, revision_data):
        """Atualiza uma revisão existente."""
        if '_id' in revision_data:
            del revision_data['_id']  
        result = await db[COLLECTION].update_one(
            {"_id": ObjectId(revision_id)},
            {"$set": revision_data}
        )

        if result.matched_count > 0:
            return True
        return False
    
    async def delete(self, revision_id: str):
        """Deleta uma revisão pelo seu ID"""
        result = await db[COLLECTION].delete_one({"_id": ObjectId(revision_id)})

        if result.deleted_count > 0:
            return True  
        return False  
