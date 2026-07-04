from  pydantic import BaseModel


class FacturaBase(BaseModel):
    fecha: str
    vr_total: float
    Cliente: Cliente

class FacturaCrear(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None