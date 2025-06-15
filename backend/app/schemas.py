from pydantic import BaseModel, EmailStr, validator
from datetime import date, datetime


def validar_rut(rut: str) -> bool:
    rut = rut.replace('.', '').replace('-', '')
    if len(rut) < 2:
        return False
    cuerpo, verificador = rut[:-1], rut[-1].upper()
    suma = 0
    factor = 2
    for c in reversed(cuerpo):
        suma += int(c) * factor
        factor = 9 if factor == 2 else factor - 1
    dv = 11 - (suma % 11)
    dv = 'K' if dv == 10 else '0' if dv == 11 else str(dv)
    return dv == verificador

class PagoBase(BaseModel):
    monto: float
    fecha: datetime
    medio: str
    moneda: str = "CLP"
    referencia: str | None = None

class PagoCreate(PagoBase):
    socio_id: int

class Pago(PagoBase):
    id: int

    class Config:
        orm_mode = True

class SocioBase(BaseModel):
    nombre: str
    rut: str
    email: EmailStr
    telefono: str | None = None
    direccion: str | None = None
    fecha_ingreso: date
    estado: str = "activo"
    observaciones: str | None = None

    @validator('rut')
    def valida_rut(cls, v):
        if not validar_rut(v):
            raise ValueError('RUT invalido')
        return v

class SocioCreate(SocioBase):
    pass

class Socio(SocioBase):
    id: int
    activo: bool
    pagos: list[Pago] = []

    class Config:
        orm_mode = True

class EventoBase(BaseModel):
    nombre: str
    fecha: datetime
    descripcion: str | None = None
    pago_requerido: bool = False

class EventoCreate(EventoBase):
    pass

class Evento(EventoBase):
    id: int

    class Config:
        orm_mode = True
