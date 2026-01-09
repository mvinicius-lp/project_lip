from datetime import date
from app.core.database import db

COLLECTION = "user_streaks"

class UserStreakRepositoryImpl:

    async def find_by_user_id(self, user_id: str):
        return await db[COLLECTION].find_one({"user_id": user_id})

    async def create(self, user_id: str):
        doc = {
            "user_id": user_id,
            "current_streak": 1,
            "last_activity_date": date.today().isoformat()
        }
        await db[COLLECTION].insert_one(doc)
        return doc

    async def update(self, user_id: str, streak: int, last_date: date):
        await db[COLLECTION].update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "current_streak": streak,
                    "last_activity_date": last_date.isoformat()
                }
            }
        )
