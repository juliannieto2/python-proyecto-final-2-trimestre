from fastapi import APIRouter, HTTPException, status
from ..modelos.clientes import Cliente
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar, FacturaLeer
from ..listas import lista_clientes, lista_facturas
from ..conexion_bd import Sesion_dependencias
from sqlmodel import select


rutas_facturas = APIRouter()

#lista_clientes: list[Cliente] = []#vacio
#lista_facturas: list[Factura] = []


#crear los endpoints para facturas
@rutas_facturas.get("/facturas", response_model=list[FacturaLeer])
async def listar_facturas(sesion: Sesion_dependencias):
    #select * from factura
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas


@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    #recorrer la lista_facturas
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"la factura con id {factura_id}, no existe"
    )


@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear, sesion: Sesion_dependencias):
    #buscar el cliente en base de datos 

    cliente_encontrado = sesion.get(Cliente, cliente_id)
    #mensaje si el cliente no existe
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"el cliente con id {cliente_id}, no existe"
        )

    #validar datos de la factura-json, pasarlo dict
    factura_dict =  datos_factura.model_dump()
    factura_dict ["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)
    #guardar en bd
    sesion.add(factura_val)
    sesion.commit()
    sesion.refresh(factura_val)
    return factura_val


@rutas_facturas.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: FacturaEditar):
    pass


@rutas_facturas.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura: int):
    pass