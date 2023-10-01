from paq_modelo.libroEsquema import LibroEsquema
from paq_modelo.libro import Libro
from sqlalchemy.orm import Session
from paq_modelo.IdiomaEsquema import IdiomaDatos 
from paq_modelo.idioma import Idioma

def crear_libro(db: Session, libroEsquema: LibroEsquema):
    nuevo_libro = Libro(id=libroEsquema.codigo, nombre=libroEsquema.nombre)    
    db.add(nuevo_libro)
    db.commit()
    db.flush(nuevo_libro)
    return nuevo_libro

def get_libro_por_id(db: Session, id: int):
    return db.query(Libro).filter(Libro.id == id).first()



def crear_idioma(db: Session, idioma_datos: IdiomaDatos):
     obj = Idioma(nombre=idioma_datos.nombre)
     db.add(obj)
     db.commit()
     db.flush(obj)
     return obj

def get_idioma_por_id(db: Session, id: int):
    return db.query(Idioma).filter(Idioma.id == id).first()

#obtener todos los estudiantes
from paq_modelo.Estudiante import Estudiante
def get_estudiantes(db: Session):
    return db.query(Estudiante).all()