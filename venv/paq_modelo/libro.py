from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from paq_infraestructura.Conexion import Base

class Libro(Base):
    __tablename__ = 'libro'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(200))    