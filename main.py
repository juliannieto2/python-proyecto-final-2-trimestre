from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#crear el modelo(id, nombre, email, descripcion)

class Cliente(BaseModel):
    id: int
    nombre: str
    email: str
    descripcion: str

lista_clientes: list[Cliente] = []


#endpoint. para listar todos los clientes
@app.get("/clientes")
def listar_clientes():
    return lista_clientes

#endpoint. para listar un solo cliente cliente de la lista
@app.get("/clientes/{cliente_id}")
def listar_clientes(cliente_id: int):
    #recorrer la lista_clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.get("id") == cliente_id:
            return obj_cliente
        
#enpoint, para crear un cliente y agregar a la lista 
@app.post("/clientes")
def crear_clientes(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)        
    return datos_cliente