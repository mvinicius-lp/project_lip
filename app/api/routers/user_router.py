from fastapi import APIRouter, HTTPException
from app.infrastructure.mongodb.user_repository_impl import UserRepositoryImpl
from app.application.use_cases.create_user_usecase import CreateUserUseCase
from app.application.use_cases.delete_user_usecase import DeleteUserUseCase
from app.application.use_cases.login_user_usecase import LoginUserUseCase
from app.application.use_cases.update_user_usecase import UpdateUserUseCase

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_user(nome: str, email: str, senha: str, confirma: str):
    repo = UserRepositoryImpl()
    usecase = CreateUserUseCase(repo)
    return await usecase.execute(nome, email, senha, confirma)

@router.post("/login")
async def login(email: str, senha: str):
    repo = UserRepositoryImpl()
    usecase = LoginUserUseCase(repo)
    return await usecase.execute(email, senha)

@router.put("/update")
async def update_user(user_id: str, name: str):
    user_repo = UserRepositoryImpl()
    usecase = UpdateUserUseCase(user_repo)

    updated = await usecase.execute(user_id, name)

    if updated:
        return {"message": "Nome de usuário atualizado com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.delete("/{email}")
async def delete_user(email: str):
    repo = UserRepositoryImpl()
    usecase = DeleteUserUseCase(repo)
    return await usecase.execute(email)
