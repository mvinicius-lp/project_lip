from app.core.database import db
from app.domain.entities.revision import Revision
from app.domain.repositories.revision_repository import RevisionRepository

COLLECTION = "revisions"

class RevisionRepositoryImpl(RevisionRepository):

    async def create(self, revision: Revision):
        revision_dict = {
            "user_id": revision.user_id,
            "study_id": revision.study_id,
            "data_revisao": revision.data_revisao,
            "realizada": revision.realizada
        }

        result = await db[COLLECTION].insert_one(revision_dict)
        revision_dict["_id"] = str(result.inserted_id)
        return revision_dict
