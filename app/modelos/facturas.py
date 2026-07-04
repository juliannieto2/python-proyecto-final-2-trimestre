from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import Cliente, ClienteLeer
from datetime import datetime


class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now())
    #cliente: Cliente   
    #transacciones: list[Transaccion] = []
    
    @computed_field
    @property
    def vr_total(self) -> float:
        total_factura = 0.0
        if self.transacciones == None:
            return total_factura
        #     return total_factura
        # #recorrer la listad de transacciones segun el factura id
        for transaccion in self.transacciones:
                 total_factura += transaccion.vr_unitario * transaccion.cantidad

        return total_factura

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    #crear relacione virtuale con cliente, transacciones - no en la bd
    cliente : Cliente = Relationship(back_populates="factura") 
    transacciones: list[Transaccion] = Relationship(back_populates="factura")


#crea modelo para consultar el usuario o cliente
class FacturaLeer(FacturaBase):
    id: int
    cliente:  ClienteLeer
    #puede ir aqui pero no es recomendable por las buenas practicas 
    #Transacciones: list[Transaccion] = []

class FacturaLeerCompuesta(FacturaLeer):
    transacciones: list[Transaccion] = []