from datetime import datetime

class GetDayOverviewUseCase:

    def __init__(self, study_repo, revision_repo):
        self.study_repo = study_repo
        self.revision_repo = revision_repo

    async def execute(self, user_id):
        today = datetime.utcnow()

        studies = await self.study_repo.find_by_date(user_id, today)
        revisions = await self.revision_repo.find_by_date(user_id, today)

        return {
            "data": today.date().isoformat(),
            "studies": studies,
            "revisions": revisions
        }
