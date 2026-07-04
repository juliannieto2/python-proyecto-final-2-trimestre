from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from ..modelos.facturas import Factura
from ..modelos.transacciones import (
    Transaccion,
    TransaccionesCrear,
    TransaccionesEditar
)
from ..conexion_bd import Sesion_dependencias

rutas_transacciones = APIRouter()


# ==========================
# LISTAR TODAS LAS TRANSACCIONES
# ==========================
@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones(sesion: Sesion_dependencias):

    return sesion.exec(select(Transaccion)).all()


# ==========================
# LISTAR UNA TRANSACCION
# ==========================
@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(
    id_transaccion: int,
    sesion: Sesion_dependencias
):

    transaccion = sesion.get(Transaccion, id_transaccion)

    if not transaccion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La transacción no existe"
        )

    return transaccion


# ==========================
# CREAR TRANSACCION
# ==========================
@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(
    factura_id: int,
    datos_transaccion: TransaccionesCrear,
    sesion: Sesion_dependencias
):

    factura = sesion.get(Factura, factura_id)

    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La factura con id {factura_id} no existe"
        )

    datos = datos_transaccion.model_dump()
    datos["factura_id"] = factura_id

    transaccion = Transaccion.model_validate(datos)

    sesion.add(transaccion)
    sesion.commit()
    sesion.refresh(transaccion)

    return transaccion


# ==========================
# EDITAR TRANSACCION
# ==========================
@rutas_transacciones.patch(
    "/transacciones/{id_transaccion}",
    response_model=Transaccion
)
async def editar_transaccion(
    id_transaccion: int,
    datos_transaccion: TransaccionesEditar,
    sesion: Sesion_dependencias
):

    transaccion = sesion.get(Transaccion, id_transaccion)

    if not transaccion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La transacción no existe"
        )

    datos = datos_transaccion.model_dump(exclude_unset=True)

    for campo, valor in datos.items():
        setattr(transaccion, campo, valor)

    sesion.add(transaccion)
    sesion.commit()
    sesion.refresh(transaccion)

    return transaccion


# ==========================
# ELIMINAR TRANSACCION
# ==========================
@rutas_transacciones.delete("/transacciones/{id_transaccion}")
async def eliminar_transaccion(
    id_transaccion: int,
    sesion: Sesion_dependencias
):

    transaccion = sesion.get(Transaccion, id_transaccion)

    if not transaccion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La transacción no existe"
        )

    sesion.delete(transaccion)
    sesion.commit()

    return {
        "mensaje": "Transacción eliminada correctamente"
    }