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

@router.get("/{pago_id}", response_model=schemas.Pago)
def obtener_pago(pago_id: int, db: Session = Depends(database.get_db)):
    pago = db.query(models.Pago).get(pago_id)
    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return pago

@router.put("/{pago_id}", response_model=schemas.Pago)
def actualizar_pago(pago_id: int, pago: schemas.PagoCreate, db: Session = Depends(database.get_db)):
    db_pago = db.query(models.Pago).get(pago_id)
    if not db_pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    for field, value in pago.model_dump().items():
        setattr(db_pago, field, value)
    db.commit()
    db.refresh(db_pago)
    return db_pago

@router.delete("/{pago_id}")
def eliminar_pago(pago_id: int, db: Session = Depends(database.get_db)):
    pago = db.query(models.Pago).get(pago_id)
    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    db.delete(pago)
    db.commit()
    return {"ok": True}