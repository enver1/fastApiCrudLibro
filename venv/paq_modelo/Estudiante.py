from sqlalchemy import Column, Integer, String
from paq_infraestructura.Conexion import Base

class Estudiante(Base):
    __tablename__ = 'estudiante'
    idEstudiante = Column( Integer, primary_key=True)
    nombres = Column(String(100))    
    apellidos = Column(String(100))
    correo = Column(String(100))
    fechaNacimiento = Column(String(100))
    telefono = Column(String(100))
    pais = Column(String(100))
    provincia = Column(String(100))
    codigoPostal = Column(String(100))
    direccion = Column(String(100))
    genero = Column(String(100))
    clave = Column(String(100))
    avatar = Column(String(100))
    fechaRegistro = Column(String(100))
    fechaModifica = Column(String(100))


