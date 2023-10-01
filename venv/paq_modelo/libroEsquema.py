from pydantic import BaseModel
from typing import Optional

class LibroEsquema(BaseModel):
    codigo: Optional[str] = None
    nombre: str
    
class LibroId(BaseModel):
    id: int

