"""
Funciones de apoyo para el TP Integrador de Python.

Este módulo concentra la carga, transformación y análisis básico del dataset.
De esta forma, main.py queda como programa principal y este archivo contiene
subrutinas reutilizables, cumpliendo con la separación pedida en la consigna.
"""

import pandas as pd


RUTA_DATASET = "data/ventas_videojuegos.csv"


def cargar_dataset(ruta_archivo=RUTA_DATASET):
    """Lee el archivo CSV y lo convierte en un DataFrame de Pandas."""
    return pd.read_csv(ruta_archivo)


def preparar_dataset(df):
    """
    Aplica transformaciones básicas sobre el DataFrame.

    Transformaciones realizadas:
    1. Renombra columnas para mejorar la presentación.
    2. Convierte la columna Fecha a tipo datetime.
    3. Crea la columna Total_Venta.
    4. Crea la columna Mes.
    5. Convierte Cliente_Frecuente a tipo bool.
    """
    df = df.rename(
        columns={
            "fecha": "Fecha",
            "producto": "Producto",
            "categoria": "Categoria",
            "precio_unitario": "Precio_Unitario",
            "cantidad": "Cantidad",
            "medio_pago": "Medio_Pago",
            "provincia": "Provincia",
            "cliente_frecuente": "Cliente_Frecuente",
            "descuento": "Descuento",
        }
    )

    df["Fecha"] = pd.to_datetime(df["Fecha"])
    df["Cliente_Frecuente"] = df["Cliente_Frecuente"].astype(bool)
    df["Total_Venta"] = (df["Precio_Unitario"] * df["Cantidad"]) - df["Descuento"]
    df["Mes"] = df["Fecha"].dt.month

    return df


def mostrar_primeras_filas(df, cantidad=10):
    """Muestra las primeras filas del dataset."""
    print("\nPrimeras filas del dataset:")
    print(df.head(cantidad).to_string(index=False))


def mostrar_resumen_estadistico(df):
    """Calcula y muestra métricas estadísticas básicas."""
    total_facturado = df["Total_Venta"].sum()
    promedio_venta = df["Total_Venta"].mean()
    venta_maxima = df["Total_Venta"].max()
    venta_minima = df["Total_Venta"].min()
    cantidad_operaciones = len(df)

    print("\nResumen estadístico:")
    print(f"Cantidad de operaciones: {cantidad_operaciones}")
    print(f"Total facturado: ${total_facturado:,.2f}")
    print(f"Promedio por venta: ${promedio_venta:,.2f}")
    print(f"Venta máxima: ${venta_maxima:,.2f}")
    print(f"Venta mínima: ${venta_minima:,.2f}")


def mostrar_ventas_por_categoria(df):
    """Agrupa las ventas por categoría y muestra el total facturado."""
    ventas_categoria = (
        df.groupby("Categoria")["Total_Venta"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nVentas por categoría:")

    for categoria, total in ventas_categoria.items():
        print(f"{categoria}: ${total:,.2f}")


def filtrar_ventas_importantes(df, monto_minimo):
    """Devuelve las ventas cuyo total supera un monto indicado."""
    return df[df["Total_Venta"] >= monto_minimo]
