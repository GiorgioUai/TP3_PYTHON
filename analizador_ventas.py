"""
Clase principal de análisis para el TP Integrador.

La clase AnalizadorVentas se usa para cumplir el punto opcional de POO.
Guarda internamente un DataFrame y ofrece métodos propios para analizar,
normalizar y realizar una predicción simple sobre las ventas.
"""

import numpy as np


class AnalizadorVentas:
    """Analiza ventas de videojuegos a partir de un DataFrame de Pandas."""

    def __init__(self, dataframe):
        """Guarda una copia del DataFrame como atributo interno."""
        self.df = dataframe.copy()

    def obtener_ventas_mensuales(self):
        """Devuelve el total vendido agrupado por mes."""
        return self.df.groupby("Mes")["Total_Venta"].sum().sort_index()

    def normalizar_total_venta(self):
        """
        Normaliza la columna Total_Venta usando NumPy.

        La normalización lleva los valores a una escala entre 0 y 1.
        Sirve para comparar ventas de distinto tamaño en una misma escala.
        """
        valores = self.df["Total_Venta"].to_numpy(dtype=float)
        valor_minimo = np.min(valores)
        valor_maximo = np.max(valores)

        if valor_maximo == valor_minimo:
            self.df["Venta_Normalizada"] = 0
        else:
            self.df["Venta_Normalizada"] = (valores - valor_minimo) / (valor_maximo - valor_minimo)

        return self.df

    def predecir_ventas_proximo_periodo(self):
        """
        Predice las ventas del próximo período con regresión lineal simple.

        Para mantener el trabajo simple y defendible, se usa NumPy con polyfit.
        El algoritmo toma como entrada los meses y como salida esperada el total
        vendido en cada mes. Luego estima el valor del período siguiente.
        """
        ventas_mensuales = self.obtener_ventas_mensuales()

        meses = ventas_mensuales.index.to_numpy(dtype=float)
        totales = ventas_mensuales.values.astype(float)

        pendiente, ordenada_origen = np.polyfit(meses, totales, 1)
        proximo_periodo = int(meses.max() + 1)
        prediccion = (pendiente * proximo_periodo) + ordenada_origen

        if prediccion < 0:
            prediccion = 0

        return {
            "proximo_periodo": proximo_periodo,
            "prediccion": float(prediccion),
            "pendiente": float(pendiente),
            "ordenada_origen": float(ordenada_origen),
            "promedio_mensual": float(np.mean(totales)),
        }
