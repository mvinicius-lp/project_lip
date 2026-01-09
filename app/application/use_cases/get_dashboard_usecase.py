from datetime import datetime, timedelta

class GetDashboardUseCase:
    def __init__(
        self,
        study_repo,
        revision_repo,
        streak_repo
    ):
        self.study_repo = study_repo
        self.revision_repo = revision_repo
        self.streak_repo = streak_repo

    async def execute(self, user_id: str):
        today = datetime.utcnow().date()

        # Revisões de hoje
        revisoes_hoje = await self.revision_repo.find_by_date(user_id, today)

        # Streak
        streak = await self.streak_repo.find_by_user_id(user_id)
        dias_ofensiva = streak["current_streak"] if streak else 0

        # Tempo total
        estudos = await self.study_repo.find_by_user_id(user_id)
        total_minutos = sum(
            (e["tempo_horas"] * 60) + e["tempo_minutos"]
            for e in estudos
        )

        # Disciplina mais estudada
        disciplina_count = {}
        for e in estudos:
            disciplina_count[e["disciplina"]] = disciplina_count.get(e["disciplina"], 0) + 1

        mais_estudada = max(disciplina_count, key=disciplina_count.get) if disciplina_count else None

        # Atividade semanal
        inicio_semana = today - timedelta(days=6)
        atividade = []

        for i in range(7):
            dia = inicio_semana + timedelta(days=i)
            estudos_dia = await self.study_repo.find_by_date(user_id, dia)
            atividade.append({
                "dia": dia.strftime("%a"),
                "total": len(estudos_dia)
            })

        # Próximas revisões
        proximas = await self.revision_repo.find_future(user_id, datetime.utcnow())

        return {
            "cards": {
                "revisoes_hoje": len(revisoes_hoje),
                "dias_ofensiva": dias_ofensiva,
                "tempo_total": f"{total_minutos // 60}h {total_minutos % 60}m",
                "disciplina_mais_estudada": mais_estudada
            },
            "atividade_semanal": atividade,
            "proximas_revisoes": proximas[:5]
        }
