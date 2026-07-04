from datetime import datetime

from pydantic import computed_field
from sqlmodel import Field, Relationship, SQLModel

from .clientes import Cliente, ClienteLeer
from .transacciones import Transaccion


# ==========================
# MODELO BASE
# ==========================
class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)

    @computed_field
    @property
    def vr_total(self) -> float:
        total = 0.0

        transacciones = getattr(self, "transacciones", [])

        for transaccion in transacciones:
            total += transaccion.cantidad * transaccion.vr_unitario

        return total


# ==========================
# CREAR
# ==========================
class FacturaCrear(FacturaBase):
    pass


# ==========================
# EDITAR
# ==========================
class FacturaEditar(SQLModel):
    fecha: datetime | None = None


# ==========================
# TABLA
# ==========================
class Factura(FacturaBase, table=True):

    id: int | None = Field(default=None, primary_key=True)

    cliente_id: int = Field(foreign_key="cliente.id")

    cliente: Cliente = Relationship(back_populates="factura")

    transacciones: list[Transaccion] = Relationship(
        back_populates="factura"
    )


# ==========================
# RESPUESTA
# ==========================
class FacturaLeer(FacturaBase):

    id: int

    cliente: ClienteLeer


class FacturaLeerCompuesta(FacturaLeer):

    transacciones: list[Transaccion] = []