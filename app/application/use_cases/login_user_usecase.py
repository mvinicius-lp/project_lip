from fastapi import HTTPException
from passlib.hash import pbkdf2_sha256
from app.domain.repositories.user_repository import UserRepository

class LoginUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def execute(self, email: str, senha: str):
        user = await self.repo.get_by_email(email)

        if not user:
            raise HTTPException(status_code=401, detail="E-mail ou senha inválidos.")

        stored_password = user.get("senha")

        if not pbkdf2_sha256.verify(senha, stored_password):
            raise HTTPException(status_code=401, detail="E-mail ou senha inválidos.")

        return {
            "message": "Login realizado com sucesso.",
            "user": {
                "id": str(user["_id"]),
                "nome": user["nome"],
                "email": user["email"]
            }
        }
