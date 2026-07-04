from pydantic import BaseModel

class TransaccionesBase(BaseModel):
    cantidad: int
    vr_unitario: float
    factura_id: int

class TransaccionesCrear(TransaccionesBase):
    pass

class Transacciones(TransaccionesBase):
    id: int | None = None