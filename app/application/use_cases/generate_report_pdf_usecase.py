from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

class GenerateReportPdfUseCase:
    def __init__(self, study_repo, revision_repo, streak_repo):
        self.study_repo = study_repo
        self.revision_repo = revision_repo
        self.streak_repo = streak_repo

    async def execute(self, user_id: str):
        buffer = BytesIO()
        pdf = SimpleDocTemplate(buffer, pagesize=A4)
        styles = getSampleStyleSheet()
        content = []

        studies = await self.study_repo.find_by_user_id(user_id)
        streak = await self.streak_repo.find_by_user_id(user_id)

        content.append(Paragraph("Relatório Completo de Estudos", styles["Title"]))
        content.append(Paragraph(f"Dias de ofensiva: {streak['current_streak'] if streak else 0}", styles["Normal"]))

        for s in studies:
            content.append(
                Paragraph(
                    f"{s['disciplina']} – {s['conteudo']} ({s['tempo_horas']}h {s['tempo_minutos']}m)",
                    styles["Normal"]
                )
            )

        pdf.build(content)
        buffer.seek(0)

        return buffer
