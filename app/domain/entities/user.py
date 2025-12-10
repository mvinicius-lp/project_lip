from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    nome: str
    email: EmailStr
    senha: str 
