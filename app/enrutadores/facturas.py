from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from ..modelos.clientes import Cliente
from ..modelos.facturas import (
    Factura,
    FacturaCrear,
    FacturaEditar,
    FacturaLeerCompuesta
)
from ..conexion_bd import Sesion_dependencias

rutas_facturas = APIRouter()


# ==========================
# LISTAR TODAS LAS FACTURAS
# ==========================
@rutas_facturas.get("/facturas", response_model=list[FacturaLeerCompuesta])
async def listar_facturas(sesion: Sesion_dependencias):

    consulta = select(Factura)
    facturas = sesion.exec(consulta).all()

    return facturas


# ==========================
# LISTAR UNA FACTURA
# ==========================
@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int, sesion: Sesion_dependencias):

    factura = sesion.get(Factura, factura_id)

    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Factura no encontrada"
        )

    return factura


# ==========================
# CREAR FACTURA
# ==========================
@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(
    cliente_id: int,
    datos_factura: FacturaCrear,
    sesion: Sesion_dependencias
):

    cliente = sesion.get(Cliente, cliente_id)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado"
        )

    datos = datos_factura.model_dump()
    datos["cliente_id"] = cliente_id

    factura = Factura.model_validate(datos)

    sesion.add(factura)
    sesion.commit()
    sesion.refresh(factura)

    return factura


# ==========================
# EDITAR FACTURA
# ==========================
@rutas_facturas.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(
    id_factura: int,
    datos_factura: FacturaEditar,
    sesion: Sesion_dependencias
):

    factura = sesion.get(Factura, id_factura)

    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Factura no encontrada"
        )

    datos = datos_factura.model_dump(exclude_unset=True)

    for campo, valor in datos.items():
        setattr(factura, campo, valor)

    sesion.add(factura)
    sesion.commit()
    sesion.refresh(factura)

    return factura


# ==========================
# ELIMINAR FACTURA
# ==========================
@rutas_facturas.delete("/facturas/{id_factura}")
async def eliminar_factura(
    id_factura: int,
    sesion: Sesion_dependencias
):

    factura = sesion.get(Factura, id_factura)

    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Factura no encontrada"
        )

    sesion.delete(factura)
    sesion.commit()

    return {
        "mensaje": "Factura eliminada correctamente"
    }