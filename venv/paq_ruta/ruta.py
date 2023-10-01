from fastapi import APIRouter, Depends, HTTPException
from paq_modelo.libroEsquema import LibroEsquema
from paq_servicio import crud
from paq_infraestructura.Conexion import Base, engine, localSession
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
ruta_libro = APIRouter()


def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

#LIBRO
@ruta_libro.post("/libro")
def ingresar_libro(libro: LibroEsquema, db: Session = Depends(get_db)):
    return crud.crear_libro(db=db, libroEsquema=libro)

@ruta_libro.get("/libro/{idLibro:int}")
def consultar_libro_por_id(idLibro, db: Session = Depends(get_db)):
    libro_por_id = crud.get_libro_por_id(db=db, id=idLibro) 
    if libro_por_id:
        return libro_por_id 
    raise HTTPException(status_code=404, detail='User not Found!!')

@ruta_libro.delete("/libro/{id}")
def eliminar_libro(id, db: Session = Depends(get_db)):
    crud.remove_idioma_por_id(db=db, id=id)


#IDIOMA
from paq_modelo.IdiomaEsquema import IdiomaDatos
ruta_idioma = APIRouter()

@ruta_idioma.post("/idioma")
def ingresar_idioma(idioma_datos: IdiomaDatos, db: Session = Depends(get_db)):
    return crud.crear_idioma(db=db,idioma_datos=idioma_datos)

@ruta_idioma.get("/idioma/{id}")
def obtener_idioma_por_id(id, db: Session = Depends(get_db)):
    idioma_por_id = crud.get_idioma_por_id(db=db, id=id)
    if idioma_por_id:
        return idioma_por_id
    raise HTTPException(status_code=404, detail='User not Found!!')

#Estudiante
ruta_estudiante = APIRouter()

@ruta_estudiante.get("/estudiante")
def obtenet_todos_estudiantes(db: Session = Depends(get_db)):
    return crud.get_estudiantes(db=db)    







