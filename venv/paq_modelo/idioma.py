from sqlalchemy import Column, Integer, String
from paq_infraestructura.Conexion import Base

class Idioma(Base):
    __tablename__ = 'idioma'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))    
