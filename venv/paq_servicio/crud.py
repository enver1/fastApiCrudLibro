from paq_modelo.libroEsquema import LibroEsquema
from paq_modelo.libro import Libro
from sqlalchemy.orm import Session
from paq_modelo.IdiomaEsquema import IdiomaDatos 
from paq_modelo.idioma import Idioma
from fastapi import HTTPException
from resources import mensajes

def crear_libro(db: Session, libroEsquema: LibroEsquema):
    nuevo_libro = Libro(id=libroEsquema.codigo, nombre=libroEsquema.nombre)    
    db.add(nuevo_libro)
    db.commit()
    db.flush(nuevo_libro)
    return nuevo_libro

def get_libro_por_id(db: Session, id: int):
    return db.query(Libro).filter(Libro.id == id).first()


#eliminar libro
def remove_idioma(db: Session, obj_idioma: Idioma):
    db.delete(obj_idioma)
    db.commit()
    return True

def remove_idioma_por_id(db: Session, id: int):
    obj_idioma = get_libro_por_id(db, id=id)
    if obj_idioma is None:
        raise HTTPException(status_code=404, detail=mensajes.LIBRO_DOES_NOT_EXIST_ERROR)
    return remove_idioma(db, obj_idioma=obj_idioma)

#fin eliminar libro


#----->Inicio->IDIOMA
#create
def crear_idioma(db: Session, idioma_datos: IdiomaDatos):
     obj = Idioma(nombre=idioma_datos.nombre)
     db.add(obj)
     db.commit()
     db.flush(obj)
     return obj
#find por id
def get_idioma_por_id(db: Session, id: int):
    return db.query(Idioma).filter(Idioma.id == id).first()
#edit
def editar_idioma(db: Session, id: int, idioma_esquema: IdiomaDatos):
    obj = get_idioma_por_id(db, id=id)
    if(obj.id):
        obj.nombre=idioma_esquema.nombre
        db.commit()
        db.refresh(obj)
        return obj
#-->Fin IDIOMA
#-----> inicio ESTUDIANTE
#obtener todos los estudiantes
from paq_modelo.Estudiante import Estudiante
def get_estudiantes(db: Session):
    return db.query(Estudiante).all()