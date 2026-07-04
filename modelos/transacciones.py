from pydantic import BaseModel

class TransaccionesBase(BaseModel):
    cantidad: int
    vr_unitario: float
    

class TransaccionesCrear(TransaccionesBase):
    pass

class TransaccionesEditar(TransaccionesBase):
    pass

class Transaccion(TransaccionesBase):
    id: int | None = None
    factura_id: int | None = None