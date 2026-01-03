class GetDayScheduleUseCase:

    def __init__(self, revision_repo):
        self.revision_repo = revision_repo

    async def execute(self, user_id, date):
        revisions = await self.revision_repo.find_by_date(user_id, date)

        return {
            "data": date.date().isoformat(),
            "revisions": revisions
        }
