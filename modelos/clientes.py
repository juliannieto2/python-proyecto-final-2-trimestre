from pydantic import BaseModel

#crear el modelo(id, nombre, email, descripcion)
class ClienteBase(BaseModel):
    nombre: str
    email: str
    descripcion: str

class ClienteCrear(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int | None = None