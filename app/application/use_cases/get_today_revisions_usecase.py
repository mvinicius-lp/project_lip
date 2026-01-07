class GetTodayRevisionsUseCase:
    def __init__(self, revision_repo):
        self.revision_repo = revision_repo

    async def execute(self, user_id, today):
        revisions = await self.revision_repo.find_by_date(user_id, today)
        
        enriched_revisions = [{
            "id": rev["_id"],
            "disciplina": rev["disciplina"],
            "conteudo": rev["conteudo"],
            "data_revisao": rev["data_revisao"],
            "realizada": rev["realizada"],
            "dificuldade": rev["dificuldade"],
            "tempo_dedicado": rev["tempo_dedicado"]
        } for rev in revisions]

        return {
            "data": today.isoformat(),
            "total_revisoes": len(enriched_revisions),
            "revisions": enriched_revisions
        }
