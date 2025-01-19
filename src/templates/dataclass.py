from pydantic import BaseModel, Field


class RawFlood(BaseModel):
    data: str = Field(..., min_length=10, max_length=10)
    status: str = Field(..., min_length=5, max_length=20)

    periodo: str = Field(..., min_length=5, max_length=20)
    endereco: str = Field(..., min_length=5, max_length=150)
    sentido: str = Field(..., min_length=5, max_length=50)
    referencia: str = Field(..., min_length=5, max_length=150)


class SilverFlood(RawFlood):
    latitude: float
    longitude: float

    tipo_alagamento: int

    periodo_inicial: str = Field(..., min_length=5, max_length=20)
    periodo_final: str = Field(..., min_length=5, max_length=20)

    endereco_modificado: str = Field(..., min_length=5, max_length=150)
    referencia_modificado: str = Field(..., min_length=5, max_length=150)

    endereco_formatado: str = Field(..., min_length=5, max_length=150)
