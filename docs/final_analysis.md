# Análisis Final

## 6. ¿Cuáles son los tres hallazgos más importantes y por qué deberían interesarle a una gerencia?

1. **Las tarjetas concentran la mayor parte de las ventas y transacciones.** Esto muestra una fuerte dependencia de este medio de pago y puede ser relevante para evaluar comisiones, acuerdos con entidades financieras y riesgos de concentración.

2. **Red Bull 12oz es el producto con mayor venta total.** Esto permite identificar un producto con alta contribución a los ingresos, aunque antes de recomendar acciones debería contrastarse con margen, costo, stock y frecuencia de compra.

3. **Las tiendas con mayores ventas presentan resultados relativamente cercanos.** Esto sugiere que no existe una concentración extrema entre las principales ubicaciones y que el desempeño está relativamente distribuido.

## 7. ¿Qué indicador podría llevar a una conclusión equivocada si se observa solo? ¿Con qué otra métrica lo contrastaría?

La venta total podría llevar a una conclusión equivocada si se analiza de forma aislada.

Por ejemplo, una tienda puede presentar una venta total mayor que otra, pero esto no necesariamente significa que tenga un mejor desempeño. Puede ocurrir simplemente porque registró una mayor cantidad de transacciones.

Para interpretar mejor este indicador, lo contrastaría principalmente con:

- número de transacciones;
- ticket promedio;
- cantidad de productos vendidos;
- y, si estuviera disponible, margen de ganancia.

Por ejemplo, una tienda podría vender más en total porque recibe más compras, mientras que otra podría tener menos transacciones pero un ticket promedio más alto.

Por eso, analizar la venta total junto con otras métricas permite entender mejor qué está generando realmente el resultado observado.

## 8. ¿Qué producto, cliente, tienda o método de pago investigaría con mayor profundidad y qué dato adicional necesitaría antes de recomendar una acción?

Investigaría con mayor profundidad el producto `Red Bull 12oz`, ya que fue el producto con mayor venta total dentro del análisis realizado.

Sin embargo, una mayor venta total no significa necesariamente que sea el producto más rentable o que deba aumentarse automáticamente su stock.

Antes de recomendar una acción, necesitaría información adicional como:

- margen de ganancia;
- costo de compra;
- stock disponible;
- frecuencia de reposición;
- posibles quiebres de stock;
- comportamiento de las ventas a lo largo del tiempo.

Con esta información sería posible determinar si el producto representa realmente una oportunidad comercial importante o si su alta venta se debe principalmente a factores como precio, volumen o disponibilidad.

## 9. Si dos áreas obtuvieran valores distintos para Venta Total, ¿cómo investigaría cuál cálculo es correcto?

Compararía ambos cálculos bajo los mismos criterios:

- periodo de fechas;
- filtros aplicados;
- fuente de datos;
- campo utilizado;
- transacciones incluidas o excluidas;
- duplicados y transformaciones realizadas.

Después validaría el resultado directamente contra la fuente original y documentaría una definición única de Venta Total para futuros análisis.

## 10. Si este análisis comenzara a solicitarse todos los días, ¿lo mantendría como notebook/reporte puntual o propondría una solución recurrente? ¿Qué automatizaría y qué solicitaría al equipo de Ingeniería?

Si el análisis comenzara a solicitarse todos los días, propondría una solución recurrente en lugar de ejecutar manualmente el notebook cada vez.

Automatizaría principalmente:

- la carga o actualización de nuevos datos;
- las validaciones de calidad e integridad;
- el cálculo de los principales indicadores;
- la generación de resultados agregados;
- la actualización de la información utilizada por el dashboard o reporte.

También intentaría que el proceso trabaje principalmente con los datos nuevos o modificados, evitando reprocesar toda la información histórica diariamente.

Al equipo de Ingeniería le solicitaría apoyo para implementar un proceso programado que ejecute estas tareas automáticamente, gestione posibles errores y deje registros de ejecución.

El notebook se mantendría como herramienta de exploración, validación y análisis adicional, pero no como el mecanismo principal de un proceso diario.

## 11. Indique dónde utilizó IA, qué verificó personalmente y qué parte de la solución no confiaría completamente a una IA.

Utilicé IA como apoyo para estructurar el proyecto, revisar consultas de MongoDB, apoyar la construcción de Aggregation Pipelines y mejorar la documentación.

Verifiqué personalmente la estructura de los CSV, nulos, duplicados, claves, integridad referencial, cálculos, carga en MongoDB, índices, indicadores y visualizaciones.

No confiaría completamente a una IA la interpretación final de resultados ni las decisiones de negocio, ya que requieren contexto, validación de los datos y criterio humano.
