# Preguntas de Criterio Técnico

## 1. ¿Por qué eligió ese modelo?

Se eligió un modelo referenciado porque el dataset presenta de manera natural una estructura de hechos y dimensiones.

La colección `sales` representa las transacciones y contiene las medidas principales de negocio, como:

- `quantity`
- `unit_price`
- `total_price`

Además, mantiene referencias hacia las colecciones:

- `customers`
- `items`
- `stores`
- `times`
- `payments`

mediante sus respectivas claves.

Se decidió mantener estas entidades separadas para evitar duplicación innecesaria de información.

Por ejemplo, si un mismo cliente realiza cientos de compras, no es necesario repetir su nombre, número de contacto o identificación dentro de cada documento de venta. En su lugar, `sales` almacena únicamente `customer_key`.

También se consideró que este modelo facilita la validación de integridad y mantiene una separación clara entre información descriptiva y datos transaccionales.

## 2. ¿Qué información mantendría referenciada y qué información podría estar embebida?

Mantendría referenciadas las entidades que pueden aparecer en una gran cantidad de transacciones y que poseen información propia.

Estas son:

- clientes;
- productos;
- tiendas;
- métodos de pago;
- dimensión temporal.

Por ejemplo, una venta almacena:

```json
{
  "customer_key": "C004510",
  "item_key": "I00001",
  "store_key": "S0001",
  "time_key": "T049189",
  "payment_key": "P026"
}
```

en lugar de copiar todos los atributos de esas entidades dentro del mismo documento.

Esto evita repetir información como:

- nombre del cliente;
- nombre del producto;
- proveedor;
- ubicación de la tienda;
- banco;
- información temporal.

Sin embargo, en un escenario futuro de optimización, algunos atributos pequeños y consultados con mucha frecuencia podrían ser candidatos a estar embebidos.

Por ejemplo:

- year
- month
- quarter

Esto podría ser útil si estos campos se utilizan constantemente en los análisis, ya que permitiría acceder a esa información directamente desde la colección de ventas.

La decisión entre mantener la información referenciada o embebida debería depender principalmente de cómo se consultan los datos, del volumen de información y de la frecuencia con la que cambian esos atributos.

## 3. ¿Qué revisaría primero si el volumen creciera a millones de registros?

Si el volumen de información creciera significativamente, lo primero que revisaría sería la forma en que se están realizando las consultas y los índices disponibles en MongoDB.

Revisaría principalmente:

- Qué campos se utilizan con mayor frecuencia para buscar o filtrar información.
- Si esos campos cuentan con índices adecuados.
- Si las consultas están trayendo más información de la necesaria.
- Si es posible realizar cálculos directamente en MongoDB antes de enviar los resultados a Python o Pandas.
- Si algunos análisis frecuentes podrían almacenarse previamente para evitar calcularlos nuevamente cada vez.

También evitaría cargar millones de documentos completos en Pandas cuando solamente se necesita un resultado resumido.

Por ejemplo, si se quisiera conocer la venta total por tienda, sería más conveniente realizar primero ese cálculo en MongoDB y enviar a Pandas únicamente el resultado final por tienda, en lugar de enviar todas las transacciones.

Si el volumen continuara creciendo, también evaluaría índices adicionales o combinaciones de índices según las consultas que se utilicen con mayor frecuencia.

## 4. ¿Qué cálculos decidió realizar en MongoDB y cuáles realizó posteriormente con Python/Pandas? Explique por qué.

Los cálculos principales se realizaron directamente en MongoDB mediante Aggregation Pipelines.

En MongoDB se calcularon:

- venta total;
- número de transacciones;
- clientes únicos;
- ticket promedio;
- evolución mensual de ventas;
- ventas por tienda;
- ventas por producto;
- cantidad vendida por producto;
- ventas por método de pago;
- valores mínimo, máximo y promedio de las ventas.

También se utilizaron relaciones entre colecciones para obtener información descriptiva de tiendas, productos, fechas y métodos de pago.

Se decidió realizar estos cálculos en MongoDB porque la colección `sales` contiene 1,000,000 de documentos. De esta manera se reduce la cantidad de información que debe trasladarse posteriormente a Python.

Pandas se utilizó principalmente para:

- convertir los resultados agregados en DataFrames;
- ordenar y preparar información para visualizaciones;
- realizar agrupaciones adicionales sobre resultados ya resumidos;
- construir campos necesarios para los gráficos.

Por ejemplo, para analizar la evolución mensual de ventas, MongoDB realizó la relación con la dimensión temporal, la agrupación por año y mes y la suma de las ventas.

Python/Pandas recibió únicamente el resultado mensual para preparar las fechas y generar la visualización.

Este enfoque permite aprovechar MongoDB para procesar grandes volúmenes de información y utilizar Pandas principalmente para análisis y presentación de resultados.

## 5. Si la base tuviera 20 millones de transacciones, ¿qué cambiaría en su forma de consultar y procesar la información?

Mantendría el mismo principio utilizado durante este análisis: realizar la mayor parte de los filtros, agrupaciones y cálculos directamente en MongoDB y llevar a Python/Pandas únicamente los resultados necesarios.

Por ejemplo, para comparar tiendas, MongoDB procesa las transacciones y devuelve solamente el resultado agrupado por tienda. Pandas recibe posteriormente este conjunto reducido de datos para facilitar su análisis y visualización.

Con 20 millones de transacciones sería aún más importante evitar cargar toda la colección directamente en Pandas.

Además, revisaría con mayor atención los índices utilizados, los campos solicitados en cada consulta y los filtros aplicados para evitar procesar información innecesaria.

Si algunos indicadores fueran consultados constantemente, también evaluaría almacenar resultados previamente resumidos para no tener que procesar las 20 millones de transacciones en cada consulta.

El objetivo sería mantener el procesamiento pesado dentro de MongoDB y trasladar a Python únicamente la información necesaria para el análisis y la visualización.
