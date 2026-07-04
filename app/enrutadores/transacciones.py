from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura
from ..modelos.transacciones import Transaccion, TransaccionesCrear, TransaccionesEditar
from ..listas import lista_facturas, lista_transacciones
from ..conexion_bd import Sesion_dependencias
from sqlmodel import select

rutas_transacciones = APIRouter()

#lista_facturas: list[Factura] = []
#lista_transacciones: list[Transaccion] = []


#crear los endpoints de transacciones

@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones(sesion: Sesion_dependencias):
    # consulta = select(Transaccion)
    # lista_transacciones = sesion.exec(consulta).all()
    # return lista_transacciones
    return sesion.exec(select(Transaccion)).all()

@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass


@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionesCrear, sesion: Sesion_dependencias):

    #buscar factura
    factura_encontrada = sesion.get(Factura, factura_id)
    #mensaje si no existe la factura
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"la factura con id {factura_id}, no existe"
        )

    #validar datos de la transaccion- json, y pasamos a dict
    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["factura_id"] = factura_id
    transaccion_val = Transaccion.model_validate(transaccion_dict)
    #guardar en bd 
    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)
    return transaccion_val


@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: TransaccionesEditar):
    pass


@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass