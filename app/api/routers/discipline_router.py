from fastapi import APIRouter, HTTPException
from app.infrastructure.mongodb.discipline_repository_impl import DisciplineRepositoryImpl
from app.application.use_cases.create_discipline_usecase import CreateDisciplineUseCase
from app.application.use_cases.get_disciplines_usecase import GetDisciplinesUseCase
from app.application.use_cases.update_discipline_usecase import UpdateDisciplineUseCase
from app.application.use_cases.delete_discipline_usecase import DeleteDisciplineUseCase

router = APIRouter(prefix="/discipline", tags=["Disciplinas"])

@router.post("/create")
async def create_discipline(user_id: str, nome: str, cor: str):
    usecase = CreateDisciplineUseCase(DisciplineRepositoryImpl())
    return await usecase.execute(user_id, nome, cor)

@router.get("/list")
async def list_disciplines(user_id: str):
    usecase = GetDisciplinesUseCase(DisciplineRepositoryImpl())
    return await usecase.execute(user_id)

@router.put("/update")
async def update_discipline(
    discipline_id: str,
    nome: str | None = None,
    cor: str | None = None
):
    data = {}
    if nome:
        data["nome"] = nome
    if cor:
        data["cor"] = cor

    if not data:
        raise HTTPException(400, "Nenhum campo para atualizar")

    usecase = UpdateDisciplineUseCase(DisciplineRepositoryImpl())
    success = await usecase.execute(discipline_id, data)

    if not success:
        raise HTTPException(404, "Disciplina não encontrada")

    return {"message": "Disciplina atualizada com sucesso"}

@router.delete("/delete")
async def delete_discipline(discipline_id: str):
    usecase = DeleteDisciplineUseCase(DisciplineRepositoryImpl())
    success = await usecase.execute(discipline_id)

    if not success:
        raise HTTPException(404, "Disciplina não encontrada")

    return {"message": "Disciplina deletada com sucesso"}
