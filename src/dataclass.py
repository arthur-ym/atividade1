from pydantic import BaseModel, Field


class RawCursos(BaseModel):
    curso: str = Field(..., min_length=10, max_length=100)


class RawProfessores(BaseModel):
    nome: str = Field(..., min_length=5, max_length=50)
    instituicao: str = Field(..., min_length=3, max_length=50)
    tipo: str = Field(..., min_length=3, max_length=10)
