from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from ..modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from ..conexion_bd import Sesion_dependencias

rutas_clientes = APIRouter()


# ==========================
# LISTAR TODOS LOS CLIENTES
# ==========================
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes(sesion: Sesion_dependencias):

    return sesion.exec(select(Cliente)).all()


# ==========================
# LISTAR UN CLIENTE
# ==========================
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(
    cliente_id: int,
    sesion: Sesion_dependencias
):

    cliente = sesion.get(Cliente, cliente_id)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El cliente con id {cliente_id} no existe"
        )

    return cliente


# ==========================
# CREAR CLIENTE
# ==========================
@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_cliente(
    datos_cliente: ClienteCrear,
    sesion: Sesion_dependencias
):

    cliente = Cliente.model_validate(datos_cliente.model_dump())

    sesion.add(cliente)
    sesion.commit()
    sesion.refresh(cliente)

    return cliente


# ==========================
# EDITAR CLIENTE
# ==========================
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(
    cliente_id: int,
    datos_cliente: ClienteEditar,
    sesion: Sesion_dependencias
):

    cliente = sesion.get(Cliente, cliente_id)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El cliente con id {cliente_id} no existe"
        )

    datos = datos_cliente.model_dump(exclude_unset=True)

    cliente.sqlmodel_update(datos)

    sesion.add(cliente)
    sesion.commit()
    sesion.refresh(cliente)

    return cliente


# ==========================
# ELIMINAR CLIENTE
# ==========================
@rutas_clientes.delete("/clientes/{cliente_id}")
async def eliminar_cliente(
    cliente_id: int,
    sesion: Sesion_dependencias
):

    cliente = sesion.get(Cliente, cliente_id)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El cliente con id {cliente_id} no existe"
        )

    # Verificar si el cliente tiene facturas asociadas
    if cliente.factura:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se puede eliminar el cliente porque tiene facturas asociadas."
        )

    sesion.delete(cliente)
    sesion.commit()

    return {
        "mensaje": "Cliente eliminado correctamente"
    }