from fastapi import APIRouter, HTTPException, status
from ..modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from ..listas import lista_clientes
from ..conexion_bd import Sesion_dependencias
from sqlmodel import select

rutas_clientes = APIRouter()

# lista_clientes: list[Cliente] = []

#endpoint. para listar todos los clientes
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_cliente(sesion: Sesion_dependencias):
    lista_cli = sesion.exec(select(Cliente)).all()
    return lista_cli

#endpoint. para listar un solo cliente cliente de la lista
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int, mi_sesion: Sesion_dependencias):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"el cliente con id {cliente_id}, no existe"
        )
    return cliente_bd 

#enpoint, para crear un cliente y agregar a la lista 
@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_clientes(datos_cliente: ClienteCrear, mi_sesion: Sesion_dependencias):
    Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(Cliente_val)
    mi_sesion.commit()
    mi_sesion.refresh(Cliente_val)
    return Cliente_val

#enpoint, para editar un cliente y agregar a la lista 
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar, mi_sesion: Sesion_dependencias):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"el cliente con id {cliente_id}, no existe"
        )
    cliente_dic = datos_cliente.model_dump(exclude_unset=True)
    cliente_bd.sqlmodel_update(cliente_dic)
    mi_sesion.add(cliente_bd)
    mi_sesion.commit()
    mi_sesion.refresh(cliente_bd)
    return cliente_bd


#enpoint eliminar cliente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int, mi_sesion: Sesion_dependencias):
    cliente_bd = mi_sesion.get(Cliente, cliente_id)
    if not cliente_bd:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"el cliente con id {cliente_id}, no existe"
        )
    mi_sesion.delete(cliente_bd)
    mi_sesion.commit()
    #retornar un mensaje, debe quitar el response model
    return cliente_bd