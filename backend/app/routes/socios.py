from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/socios", tags=["socios"])

@router.post("/", response_model=schemas.Socio)
def crear_socio(socio: schemas.SocioCreate, db: Session = Depends(database.get_db)):
    db_socio = db.query(models.Socio).filter(models.Socio.rut == socio.rut).first()
    if db_socio:
        raise HTTPException(status_code=400, detail="Socio ya existe")
    nuevo = models.Socio(**socio.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[schemas.Socio])
def listar_socios(db: Session = Depends(database.get_db)):
    return db.query(models.Socio).all()

@router.get("/{socio_id}", response_model=schemas.Socio)
def obtener_socio(socio_id: int, db: Session = Depends(database.get_db)):
    socio = db.query(models.Socio).get(socio_id)
    if not socio:
        raise HTTPException(status_code=404, detail="Socio no encontrado")
    return socio

@router.put("/{socio_id}", response_model=schemas.Socio)
def actualizar_socio(socio_id: int, socio: schemas.SocioCreate, db: Session = Depends(database.get_db)):
    db_socio = db.query(models.Socio).get(socio_id)
    if not db_socio:
        raise HTTPException(status_code=404, detail="Socio no encontrado")
    for field, value in socio.model_dump().items():
        setattr(db_socio, field, value)
    db.commit()
    db.refresh(db_socio)
    return db_socio

@router.delete("/{socio_id}")
def eliminar_socio(socio_id: int, db: Session = Depends(database.get_db)):
    socio = db.query(models.Socio).get(socio_id)
    if not socio:
        raise HTTPException(status_code=404, detail="Socio no encontrado")
    socio.activo = False
    db.commit()
    return {"ok": True}
