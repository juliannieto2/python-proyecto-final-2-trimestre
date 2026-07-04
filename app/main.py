from fastapi import FastAPI

from app.enrutadores import clientes, facturas, transacciones

app = FastAPI()

app.include_router(clientes.rutas_clientes, tags=["Clientes"])
app.include_router(facturas.rutas_facturas, tags=["Facturas"])
app.include_router(transacciones.rutas_transacciones, tags=["Transacciones"])

