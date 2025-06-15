from fastapi import APIRouter, Depends, HTTPException
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

@router.get("/{evento_id}", response_model=schemas.Evento)
def obtener_evento(evento_id: int, db: Session = Depends(database.get_db)):
    evento = db.query(models.Evento).get(evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return evento

@router.put("/{evento_id}", response_model=schemas.Evento)
def actualizar_evento(evento_id: int, evento: schemas.EventoCreate, db: Session = Depends(database.get_db)):
    db_evento = db.query(models.Evento).get(evento_id)
    if not db_evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    for field, value in evento.model_dump().items():
        setattr(db_evento, field, value)
    db.commit()
    db.refresh(db_evento)
    return db_evento

@router.delete("/{evento_id}")
def eliminar_evento(evento_id: int, db: Session = Depends(database.get_db)):
    evento = db.query(models.Evento).get(evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    db.delete(evento)
    db.commit()
    return {"ok": True}

@router.post("/{evento_id}/asistencias", response_model=schemas.Asistencia)
def registrar_asistencia(evento_id: int, asistencia: schemas.AsistenciaCreate, db: Session = Depends(database.get_db)):
    if not db.query(models.Socio).get(asistencia.socio_id):
        raise HTTPException(status_code=404, detail="Socio no encontrado")
    if not db.query(models.Evento).get(evento_id):
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    registro = models.Asistencia(socio_id=asistencia.socio_id, evento_id=evento_id)
    db.add(registro)
    db.commit()
    db.refresh(registro)
    return registro

@router.get("/{evento_id}/asistencias", response_model=list[schemas.Asistencia])
def listar_asistencias(evento_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Asistencia).filter_by(evento_id=evento_id).all()
