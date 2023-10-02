from fastapi import FastAPI
from paq_ruta.ruta import ruta_libro, ruta_idioma, ruta_estudiante
app = FastAPI()


app.include_router(ruta_libro)
app.include_router(ruta_idioma)
app.include_router(ruta_estudiante)