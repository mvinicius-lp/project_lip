from passlib.hash import pbkdf2_sha256
from fastapi import HTTPException
from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository


class CreateUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def execute(self, nome: str, email: str, senha: str, confirma: str):
        if senha != confirma:
            raise HTTPException(status_code=400, detail="Senha e confirmação não conferem.")

        existing = await self.repo.get_by_email(email)
        if existing:
            raise HTTPException(status_code=409, detail="E-mail já cadastrado.")

        hashed = pbkdf2_sha256.hash(senha)

        user = User(nome=nome, email=email, senha=hashed)
        return await self.repo.create(user)
