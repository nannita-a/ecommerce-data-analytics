# E-Commerce Data Analytics

Proyecto de análisis de datos desarrollado como prueba técnica para construir una primera capa analítica a partir de un dataset de comercio electrónico.

El flujo implementado es:

```text
CSV
↓
Perfilamiento y validación
↓
MongoDB
↓
Aggregation Pipelines
↓
Python / Pandas
↓
Visualizaciones
↓
Hallazgos de negocio
```

## Objetivo

Transformar un conjunto de archivos CSV en una solución analítica reproducible que permita:

- validar calidad e integridad de los datos;
- cargar la información en MongoDB;
- calcular indicadores mediante Aggregation Pipelines;
- analizar resultados con Python y Pandas;
- generar visualizaciones ejecutivas;
- identificar hallazgos relevantes para negocio;
- proponer una capa conceptual de API para consumo de indicadores.

## Dataset

El proyecto utiliza los siguientes archivos:

- `customer_dim.csv`
- `item_dim.csv`
- `store_dim.csv`
- `time_dim.csv`
- `Trans_dim.csv`
- `fact_table.csv`

La estructura original corresponde a una tabla de hechos y cinco dimensiones.

## Arquitectura de datos

Los archivos fueron migrados a MongoDB utilizando las siguientes colecciones:

| CSV                | MongoDB     |
| ------------------ | ----------- |
| `customer_dim.csv` | `customers` |
| `item_dim.csv`     | `items`     |
| `store_dim.csv`    | `stores`    |
| `time_dim.csv`     | `times`     |
| `Trans_dim.csv`    | `payments`  |
| `fact_table.csv`   | `sales`     |

La colección `sales` funciona como núcleo transaccional y mantiene referencias hacia las demás colecciones.

El modelo completo se encuentra documentado en:

`docs/data_model.md`

Diagrama:

![Modelo MongoDB](diagrams/mongodb_model.png)

## Tecnologías utilizadas

- Python 3.11
- MongoDB 8.3
- MongoDB Compass
- PyMongo
- Pandas
- Matplotlib
- Jupyter Notebook
- Requests
- Git / GitHub

## Estructura del proyecto

```text
ecommerce-data-analytics/
│
├── data/
│   └── raw/
│       ├── customer_dim.csv
│       ├── fact_table.csv
│       ├── item_dim.csv
│       ├── store_dim.csv
│       ├── time_dim.csv
│       └── Trans_dim.csv
│
├── diagrams/
│   └── mongodb_model.png
│
├── docs/
│   ├── api_specification.md
│   ├── data_model.md
│   ├── final_analysis.md
│   └── technical_questions.md
│
├── notebooks/
│   └── ecommerce_analysis.ipynb
│
├── src/
│   ├── create_indexes.py
│   ├── inspect_data.py
│   ├── load_mongodb.py
│   └── validate_mongodb.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Preparación del entorno

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## MongoDB

El proyecto utiliza una instancia local de MongoDB:

```text
mongodb://localhost:27017
```

La base de datos utilizada es:

```text
ecommerce_analytics
```

Antes de ejecutar los scripts, verificar que el servicio de MongoDB esté activo.

En Windows:

```powershell
Get-Service MongoDB
```

## Ejecución

### 1. Perfilamiento inicial

```bash
python src/inspect_data.py
```

Este script revisa:

- estructura de los CSV;
- tipos de datos;
- valores nulos;
- duplicados;
- unicidad de claves;
- integridad referencial;
- reglas básicas de negocio.

### 2. Carga a MongoDB

```bash
python src/load_mongodb.py
```

La carga se realiza por lotes para evitar insertar el millón de transacciones en una sola operación.

### 3. Validación de carga

```bash
python src/validate_mongodb.py
```

Se comparan los registros de los CSV con los documentos almacenados en MongoDB.

Resultado esperado:

| Colección   | Registros |
| ----------- | --------: |
| `customers` |     9,191 |
| `items`     |       264 |
| `stores`    |       726 |
| `times`     |    99,999 |
| `payments`  |        39 |
| `sales`     | 1,000,000 |

### 4. Creación de índices

```bash
python src/create_indexes.py
```

Se crean índices únicos en las dimensiones e índices de consulta sobre los campos de referencia de `sales`.

### 5. Análisis

Abrir:

```text
notebooks/ecommerce_analysis.ipynb
```

y ejecutar todas las celdas utilizando Jupyter Notebook o VS Code con el kernel del entorno `.venv`.

## Indicadores calculados

El análisis incluye:

- venta total;
- número de transacciones;
- clientes únicos;
- ticket promedio;
- evolución mensual de ventas;
- comparación de tiendas;
- comparación de productos;
- análisis por método de pago;
- valores mínimo, máximo y promedio de las ventas.

## Resultados principales

Los principales resultados obtenidos fueron:

- Venta total: `105,401,435.75`
- Transacciones: `1,000,000`
- Clientes únicos: `9,191`
- Ticket promedio: `105.40`
- Producto con mayor venta total: `Red Bull 12oz`
  Método de pago predominante: `card`

Las conclusiones completas se encuentran en:

`docs/final_analysis.md`

## API conceptual

Se propusieron dos endpoints para consumo de indicadores:

- `GET /api/v1/analytics/sales-summary`
- `GET /api/v1/analytics/sales-by-store`

La especificación completa se encuentra en:

`docs/api_specification.md`

## Decisiones técnicas

Las respuestas relacionadas con:

- modelo referenciado;
- referencias vs embedding;
- escalabilidad;
- MongoDB vs Pandas;
- escenario con 20 millones de transacciones;

se encuentran en:

`docs/technical_questions.md`

## Reproducibilidad

El notebook fue ejecutado de principio a fin utilizando `Run All`, comprobando que los resultados pueden reconstruirse a partir de MongoDB sin copiar manualmente resultados intermedios.

## Uso de IA

La IA fue utilizada como apoyo para estructuración del proyecto, revisión de consultas, construcción de Aggregation Pipelines y documentación.

Las validaciones de datos, resultados, integridad, indicadores y visualizaciones fueron revisadas durante la ejecución del proyecto.
