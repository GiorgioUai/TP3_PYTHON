# TP Integrador Python - Análisis de ventas de videojuegos

Proyecto para el trabajo práctico integrador de Python con análisis de datos.

## Tema elegido

El proyecto analiza ventas simuladas de una tienda de videojuegos durante el año 2025.
A partir de un archivo `.csv`, el programa carga los datos con Pandas, realiza transformaciones, calcula métricas estadísticas y genera gráficos con Matplotlib.

## Objetivos del proyecto

- Leer un dataset en formato CSV.
- Convertir el dataset en un DataFrame de Pandas.
- Aplicar transformaciones sobre los datos.
- Calcular métricas estadísticas.
- Generar gráficos con Matplotlib.
- Usar estructuras básicas de Python: variables, listas, tuplas, diccionarios, condicionales y bucles.
- Separar el programa principal de los módulos auxiliares.
- Implementar una clase propia para organizar parte del análisis.
- Incorporar NumPy para cálculos numéricos.
- Aplicar una predicción simple de ventas usando regresión lineal.

## Estructura del proyecto

```text
TP3_PYTHON/
│
├── main.py
├── funciones_analisis.py
├── analizador_ventas.py
├── requirements.txt
├── README.md
├── data/
│   └── ventas_videojuegos.csv
└── graficos/
```

## Dataset

El archivo principal de datos se encuentra en:

```text
data/ventas_videojuegos.csv
```

El dataset contiene ventas simuladas con las siguientes columnas:

- fecha
- producto
- categoria
- precio_unitario
- cantidad
- medio_pago
- provincia
- cliente_frecuente
- descuento

Durante la ejecución se crean columnas calculadas como `Total_Venta`, `Mes` y `Venta_Normalizada`.

## Instalación de dependencias

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Funcionalidades del menú

Al ejecutar el programa se muestra un menú por consola con estas opciones:

1. Ver primeras filas del dataset.
2. Ver resumen estadístico.
3. Ver ventas por categoría.
4. Filtrar ventas importantes.
5. Generar gráficos.
6. Ver predicción simple.
0. Salir.

## Gráficos generados

La opción de gráficos genera archivos PNG en la carpeta `graficos`:

- `ventas_por_categoria.png`
- `ventas_por_mes.png`
- `histograma_importes.png`

## Técnicas utilizadas

- Pandas para lectura, transformación y análisis del DataFrame.
- Matplotlib para visualización de datos.
- NumPy para normalización y regresión lineal simple.
- Programación orientada a objetos mediante la clase `AnalizadorVentas`.
