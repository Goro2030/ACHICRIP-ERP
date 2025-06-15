from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Socio(Base):
    __tablename__ = "socios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    rut = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, nullable=False)
    telefono = Column(String)
    direccion = Column(String)
    fecha_ingreso = Column(Date)
    estado = Column(String, default="activo")
    observaciones = Column(String)
    activo = Column(Boolean, default=True)
    pagos = relationship("Pago", back_populates="socio")

    asistencias = relationship("Asistencia", back_populates="socio")


class Pago(Base):
    __tablename__ = "pagos"
    id = Column(Integer, primary_key=True, index=True)
    socio_id = Column(Integer, ForeignKey("socios.id"))
    monto = Column(Float, nullable=False)
    fecha = Column(DateTime)
    medio = Column(String)
    moneda = Column(String, default="CLP")
    referencia = Column(String)
    socio = relationship("Socio", back_populates="pagos")

class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha = Column(DateTime)
    descripcion = Column(String)
    pago_requerido = Column(Boolean, default=False)

    asistencias = relationship("Asistencia", back_populates="evento")

