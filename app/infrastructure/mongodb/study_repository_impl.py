from datetime import datetime, timedelta

from bson import ObjectId
from app.core.database import db
from app.utils.mongo_utils import convert_mongo_document, convert_mongo_list

COLLECTION = "studies"
REVISION_COLLECTION = "revisions"

class StudyRepositoryImpl:

    async def create(self, study):
        study_dict = {
            "user_id": study.user_id,
            "disciplina": study.disciplina,
            "conteudo": study.conteudo,
            "tempo_horas": study.tempo_horas,
            "tempo_minutos": study.tempo_minutos,
            "dificuldade": study.dificuldade,
            "criado_em": study.criado_em
        }

        result = await db[COLLECTION].insert_one(study_dict)
        study_dict["_id"] = str(result.inserted_id)
        return study_dict
    
    async def find_by_date(self, user_id, date):
        start = datetime(date.year, date.month, date.day)
        end = start + timedelta(days=1)

        cursor = db[COLLECTION].find({
            "user_id": user_id,
            "criado_em": {"$gte": start, "$lt": end}
        })

        docs = await cursor.to_list(None)
        return convert_mongo_list(docs)
    
    async def find_by_id(self, study_id):
        study = await db[COLLECTION].find_one({"_id": ObjectId(study_id)})
        return convert_mongo_document(study)

    async def delete(self, study_id: str) -> bool:
        await db[REVISION_COLLECTION].delete_many({"study_id": study_id})

        result = await db[COLLECTION].delete_one({"_id": ObjectId(study_id)})

        return result.deleted_count > 0
    
    async def update(self, study_id: str, study_data: dict) -> bool:
        result = await db[COLLECTION].update_one(
            {"_id": ObjectId(study_id)},  
            {"$set": study_data}  
        )

        return result.modified_count > 0
    
    async def find_by_user_id(self, user_id: str):
        """Encontra todos os estudos de um usuário pelo user_id."""
        cursor = db[COLLECTION].find({"user_id": user_id})
        studies = await cursor.to_list(None)
        return convert_mongo_list(studies)