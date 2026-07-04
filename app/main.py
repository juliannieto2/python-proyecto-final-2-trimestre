from fastapi import FastAPI, HTTPException, status
from .enrutadores.clientes import rutas_clientes
from app.enrutadores.facturas import rutas_facturas
from app.enrutadores.transacciones import rutas_transacciones
from app.enrutadores import clientes, facturas, transacciones
from .conexion_bd import crear_tablas


app = FastAPI(lifespan=crear_tablas) 

app.include_router(clientes.rutas_clientes, tags=["Clientes"])
app.include_router(facturas.rutas_facturas, tags=["Facturas"])
app.include_router(transacciones.rutas_transacciones, tags=["Transacciones"])

