# Especificación Conceptual de API

## Endpoint 1: Resumen general de ventas

### Ruta propuesta

`GET /api/v1/analytics/sales-summary`

### Parámetros

- `start_date`
- `end_date`
- `store_key`

### Información que devolvería

El endpoint devolvería los principales indicadores generales de ventas:

- venta total;
- número de transacciones;
- clientes únicos;
- ticket promedio.

### Cálculo previo

Antes de responder, la API debería ejecutar una agregación sobre la colección `sales` para:

1. aplicar los filtros solicitados;
2. sumar `total_price`;
3. contar las transacciones;
4. contar clientes únicos;
5. calcular el ticket promedio.

### Ejemplo de respuesta

```json
{
  "total_sales": 105401435.75,
  "transactions": 1000000,
  "unique_customers": 9191,
  "average_ticket": 105.4
}
```

## Endpoint 2: Ventas por tienda

### Ruta propuesta

`GET /api/v1/analytics/sales-by-store`

### Parámetros

- `start_date`
- `end_date`
- `limit`

### Información que devolvería

El endpoint devolvería los principales indicadores generales de ventas:

- identificador de tienda;
- ubicación;
- venta total;
- número de transacciones.

### Cálculo previo

Antes de responder, la API debería:

1. agrupar las ventas por `store_key`;
2. sumar `total_price`;
3. contar las transacciones;
4. relacionar cada resultado con la información de la tienda;
5. ordenar de mayor a menor venta total.

### Ejemplo de respuesta

```json
{
  "stores": [
    {
      "store_key": "SXXXX",
      "upazila": "JURI",
      "total_sales": 159409.0,
      "transactions": 1480
    }
  ]
}
```

# ¿Por qué solicitar estos endpoints en lugar de entregar acceso directo a todas las transacciones?

Solicitar endpoints específicos permite controlar qué información consume cada aplicación y evita exponer directamente toda la colección de ventas.

También ayuda a:

- mantener una definición única de los indicadores;
- reducir la cantidad de información transferida;
- evitar que cada sistema tenga que procesar millones de transacciones;
- mejorar seguridad y control de acceso;
- desacoplar el dashboard de la estructura interna de la base de datos.

De esta manera, el dashboard recibe únicamente los resultados que necesita en lugar de acceder directamente a todas las transacciones.
