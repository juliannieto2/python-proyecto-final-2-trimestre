from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship

class TransaccionesBase(SQLModel):
    cantidad: int = Field(default=0)
    vr_unitario: float = Field(default=0.0)
    descripcion: str = Field(default=None)
    

class TransaccionesCrear(TransaccionesBase):
    pass

class TransaccionesEditar(TransaccionesBase):
    pass

class Transaccion(TransaccionesBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura_id: int | None = Field(default=None, foreign_key="factura.id")
    #aqui va la relacion virtual con el modelo factura
    #opcional
    factura: "Factura" = Relationship(back_populates="transacciones")

#crea modelo para consultar el usuario o cliente
class TransaccionLeer(TransaccionesBase):
    id: int