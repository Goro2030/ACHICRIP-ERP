from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import socios, pagos, eventos, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gestor de Socios")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(socios.router)
app.include_router(pagos.router)
app.include_router(eventos.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al Gestor de Socios"}
