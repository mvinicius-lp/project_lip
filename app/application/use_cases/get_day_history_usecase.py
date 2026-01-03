class GetDayHistoryUseCase:

    def __init__(self, study_repo, revision_repo):
        self.study_repo = study_repo
        self.revision_repo = revision_repo

    async def execute(self, user_id, date):
        studies = await self.study_repo.find_by_date(user_id, date)
        revisions = await self.revision_repo.find_past(user_id, date)

        return {
            "data": date.date().isoformat(),
            "studies": studies,
            "revisions": revisions
        }
