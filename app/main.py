from api.routes import router as journeys_router
from fastapi import FastAPI

app = FastAPI()

# Incluir el router de las rutas
app.include_router(journeys_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "API de búsqueda de vuelos funcionando correctamente"}