from pydantic import BaseModel

class IdiomaDatos(BaseModel):
    nombre: str

class IdiomaId(IdiomaDatos):
    id: int
