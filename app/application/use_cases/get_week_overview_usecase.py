from datetime import datetime, timedelta

class GetWeekOverviewUseCase:

    def __init__(self, study_repo, revision_repo):
        self.study_repo = study_repo
        self.revision_repo = revision_repo

    async def execute(self, user_id):
        today = datetime.utcnow()
        week = []

        for offset in range(-3, 4):
            day = today + timedelta(days=offset)

            studies = await self.study_repo.find_by_date(user_id, day)
            revisions = await self.revision_repo.find_by_date(user_id, day)

            week.append({
                "offset": offset,
                "data": day.date().isoformat(),
                "tem_conteudo": len(studies) + len(revisions) > 0
            })

        return week
