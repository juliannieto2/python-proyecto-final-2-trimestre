from fastapi import FastAPI, HTTPException, status
from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar
from app.modelos.transacciones import Transaccion, TransaccionesCrear, TransaccionesEditar
from app.enrutadores import clientes
app = FastAPI()


lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

#incluir ruta de clientes 
app.include_router(clientes.rutas_clientes, tags=["clientes"])


#crear los endpoints para facturas
@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas

@app.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
      #recorrer la lista_facturas
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"la factura con id {factura_id}, no existe"
    )

@app.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos_factura: FacturaCrear):
    #buscar el cliente
    cliente_encontrado = None
    for cliente in lista_clientes:
        if cliente.id == cliente_id:
            cliente_encontrado = cliente
    #mensaje si el cliente no existe
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"el cliente con id {cliente_id}, no existe"
        )
    #validar datos de la factura
    factura_val = Factura.model_validate(datos_factura.model_dump())
    factura_val.cliente = cliente_encontrado

    #id de la factura
    factura_val.id = len(lista_facturas)+1 
    lista_facturas.append(factura_val)
    return factura_val

@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_factura(id_factura: int, datos_factura: Factura):
    pass

@app.delete("/facturas/{id_factura}", response_model=Factura)
async def eliminar_factura(id_factura):
    pass

#crear los endpoints de transacciones 

@app.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones

@app.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    pass

@app.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionesCrear):
    
    #buscar factura
    factura_encontrada = None
    for factura in lista_facturas:
        if factura.id == factura_id:
            factura_encontrada = factura
    #mensaje si no existe la factura
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"la factura con id {factura_id}, no existe"
        )
    #validar datos de la transaccion
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    transaccion_val.factura_id = factura_id
    factura_encontrada.transacciones.append(transaccion_val)

    #id de la transaccion
    transaccion_val.id = len(lista_transacciones)+1 
    return transaccion_val

    #falto agregar a la lista de transacciones
    lista_transacciones.append(transaccion_val)
    return transaccion_val


@app.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_transaccion: int, datos_transaccion: Transaccion):
    pass

@app.delete("/transacciones/{id_transaccion}", response_model= Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass