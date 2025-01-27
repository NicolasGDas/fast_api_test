from api.routes import router as journeys_router
from fastapi import FastAPI

app = FastAPI()

# Incluir el router de las rutas
app.include_router(journeys_router, prefix="/api")
