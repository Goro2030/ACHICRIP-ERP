from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/pagos", tags=["pagos"])

@router.post("/", response_model=schemas.Pago)
def crear_pago(pago: schemas.PagoCreate, db: Session = Depends(database.get_db)):
    socio = db.query(models.Socio).get(pago.socio_id)
    if not socio:
        raise HTTPException(status_code=404, detail="Socio no encontrado")
    nuevo = models.Pago(**pago.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[schemas.Pago])
def listar_pagos(db: Session = Depends(database.get_db)):
    return db.query(models.Pago).all()
