from fastapi import HTTPException
from app.domain.repositories.user_repository import UserRepository


class DeleteUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def execute(self, email: str):
        deleted = await self.repo.delete_by_email(email)
        if not deleted:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        return {"message": "Usuário deletado com sucesso."}
