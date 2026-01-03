class GetDayScheduleUseCase:

    def __init__(self, revision_repo, study_repo):
        self.revision_repo = revision_repo
        self.study_repo = study_repo

    async def execute(self, user_id, date):
        revisions = await self.revision_repo.find_by_date(user_id, date)

        enriched = []

        for rev in revisions:
            study = await self.study_repo.find_by_id(rev["study_id"])

            enriched.append({
                "_id": rev["_id"],
                "data_revisao": rev["data_revisao"],
                "realizada": rev["realizada"],
                "disciplina": study["disciplina"],
                "conteudo": study["conteudo"],
                "tempo_dedicado": f"{study['tempo_horas']}h{study['tempo_minutos']}m",
                "dificuldade": study["dificuldade"]
            })

        return {
            "data": date.date().isoformat(),
            "total_revisoes": len(enriched),
            "revisions": enriched
        }
