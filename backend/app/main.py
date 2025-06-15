from fastapi import FastAPI
from .database import Base, engine
from .routes import socios, pagos, eventos

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestor de Socios")

app.include_router(socios.router)
app.include_router(pagos.router)
app.include_router(eventos.router)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al Gestor de Socios"}
