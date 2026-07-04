# Proyecto Clientes - FastAPI

## Descripción

Este proyecto consiste en el desarrollo de una API REST utilizando FastAPI para administrar clientes, facturas y transacciones.

La aplicación implementa operaciones CRUD (Crear, Consultar, Editar y Eliminar) sobre cada uno de los módulos, utilizando SQLite como base de datos y SQLModel como ORM.

---

## Tecnologías utilizadas

- Python 3
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- Pydantic
- Git
- GitHub

---

## Estructura del proyecto

```
Proyecto_clientes
│
├── app
│   ├── enrutadores
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── modelos
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── conexion_bd.py
│   ├── listas.py
│   └── main.py
│
├── bd_clientes.sqlite3
├── requirements.txt
└── README.md
```

---

## Instalación

Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Ingresar al proyecto

```bash
cd Proyecto_clientes
```

Crear entorno virtual

```bash
python -m venv .mi_env
```

Activar entorno virtual

Windows

```bash
.mi_env\Scripts\activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar el proyecto

Iniciar el servidor

```bash
fastapi dev app/main.py
```

o

```bash
uvicorn app.main:app --reload
```

---

## Documentación automática

Swagger

```
http://127.0.0.1:8000/docs
```

Redoc

```
http://127.0.0.1:8000/redoc
```

---

# Funcionalidades

## Clientes

- Crear cliente
- Consultar todos los clientes
- Consultar cliente por ID
- Editar cliente
- Eliminar cliente

---

## Facturas

- Crear factura asociada a un cliente
- Consultar facturas
- Consultar factura por ID
- Editar factura
- Eliminar factura

---

## Transacciones

- Crear transacción asociada a una factura
- Consultar transacciones
- Consultar transacción por ID
- Editar transacción
- Eliminar transacción

---

# Base de datos

La aplicación utiliza SQLite.

Nombre de la base de datos

```
bd_clientes.sqlite3
```

La conexión se realiza mediante SQLModel.

Relaciones implementadas:

- Un cliente puede tener muchas facturas.
- Una factura pertenece a un cliente.
- Una factura puede tener muchas transacciones.
- Una transacción pertenece a una factura.

---

# Flujo del desarrollo

Durante el desarrollo del proyecto se realizó el siguiente proceso:

1. Creación del proyecto FastAPI.
2. Creación de los modelos.
3. Implementación de los CRUD utilizando listas.
4. Organización del proyecto en carpetas.
5. Integración con SQLite.
6. Implementación de SQLModel.
7. Creación de relaciones entre tablas.
8. Validaciones mediante Pydantic.
9. Pruebas de funcionamiento desde Swagger.

---

# Ejemplos de endpoints

## Clientes

```
GET /clientes
GET /clientes/{id}
POST /clientes
PATCH /clientes/{id}
DELETE /clientes/{id}
```

## Facturas

```
GET /facturas
GET /facturas/{id}
POST /facturas/{cliente_id}
PATCH /facturas/{id}
DELETE /facturas/{id}
```

## Transacciones

```
GET /transacciones
GET /transacciones/{id}
POST /transacciones/{factura_id}
PATCH /transacciones/{id}
DELETE /transacciones/{id}
```

---

# Control de versiones

El proyecto fue desarrollado utilizando Git y GitHub, realizando commits durante cada etapa del desarrollo.

Ejemplo de commits realizados:

```
Inicialización del proyecto FastAPI

Creación de modelos

Implementación CRUD de clientes

Organización del proyecto por módulos

Integración con SQLite

Implementación CRUD de facturas

Implementación CRUD de transacciones

Relaciones entre tablas

Corrección de errores

Versión final del proyecto
```

---

# Autor

Juan Sebastian Barragan Sierra

Proyecto realizado como evidencia de aprendizaje utilizando FastAPI, SQLModel, SQLite, Git y GitHub.