from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/eventos", tags=["eventos"])

@router.post("/", response_model=schemas.Evento)
def crear_evento(evento: schemas.EventoCreate, db: Session = Depends(database.get_db)):
    nuevo = models.Evento(**evento.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[schemas.Evento])
def listar_eventos(db: Session = Depends(database.get_db)):
    return db.query(models.Evento).all()
