from  pydantic import BaseModel
from .clientes import Cliente


class FacturaBase(BaseModel):
    fecha: str
    vr_total: float
    Cliente: Cliente

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    pass