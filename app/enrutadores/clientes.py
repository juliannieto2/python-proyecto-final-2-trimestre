from fastapi import APIRouter, HTTPException
from ..modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from ..listas import lista_clientes

rutas_clientes = APIRouter()

# lista_clientes: list[Cliente] = []

#endpoint. para listar todos los clientes
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_cliente():
    return lista_clientes

#endpoint. para listar un solo cliente cliente de la lista
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    #recorrer la lista_clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
    raise HTTPException(
        status_code=400, detail=f"el cliente con id {cliente_id}, no existe"
    )
#enpoint, para crear un cliente y agregar a la lista 
@rutas_clientes.post("/clientes", response_model=Cliente)
async def crear_clientes(datos_cliente: ClienteCrear):
    Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    id_cliente = len(lista_clientes)+1
    Cliente_val.id = id_cliente
    lista_clientes.append(Cliente_val)        
    return Cliente_val

#enpoint, para editar un cliente y agregar a la lista 
@rutas_clientes.patch("/clientes/{cliente_id}", response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            #validar cliente
            Cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            Cliente_val.id = cliente_id
            lista_clientes[i] = Cliente_val
            return Cliente_val
    raise HTTPException(
            status_code=400, detail=f"El cliente con id {cliente_id}, no existe"
        )


#enpoint eliminar cliente
@rutas_clientes.delete("/clientes/{cliente_id}", response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(1)
            return cliente_eliminado
    raise HTTPException(
        status_code=400, detail=f"El cliente con id {cliente_id}, no existe"
    )