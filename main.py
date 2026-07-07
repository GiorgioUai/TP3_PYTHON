"""
TP Integrador Python - Análisis de ventas de videojuegos.

Programa principal del proyecto. Desde este archivo se muestra un menú por
consola y se llaman funciones definidas en el módulo funciones_analisis.py.
"""

from analizador_ventas import AnalizadorVentas
from funciones_analisis import (
    cargar_dataset,
    preparar_dataset,
    mostrar_primeras_filas,
    mostrar_resumen_estadistico,
    mostrar_ventas_por_categoria,
    filtrar_ventas_importantes,
    generar_graficos,
)


def mostrar_menu():
    """Muestra las opciones principales del programa."""
    print("\n====== ANÁLISIS DE VENTAS DE VIDEOJUEGOS ======")
    print("1. Ver primeras filas del dataset")
    print("2. Ver resumen estadístico")
    print("3. Ver ventas por categoría")
    print("4. Filtrar ventas importantes")
    print("5. Generar gráficos")
    print("6. Ver predicción simple")
    print("0. Salir")


def pedir_monto_minimo():
    """Solicita al usuario un monto mínimo para filtrar ventas."""
    entrada = input("Ingrese el monto mínimo de venta: ")

    try:
        return float(entrada)
    except ValueError:
        print("El valor ingresado no es válido. Se usará el monto mínimo 100000.")
        return 100000.0


def mostrar_prediccion(analizador):
    """Muestra la predicción simple generada por la clase AnalizadorVentas."""
    df_normalizado = analizador.normalizar_total_venta()
    resultado = analizador.predecir_ventas_proximo_periodo()

    print("\nPredicción simple de ventas")
    print("Algoritmo usado: regresión lineal simple con NumPy.")
    print("Variable de entrada: mes.")
    print("Variable a predecir: total vendido por mes.")
    print(f"Promedio mensual de ventas: ${resultado['promedio_mensual']:,.2f}")
    print(f"Pendiente calculada: {resultado['pendiente']:,.2f}")
    print(
        f"Predicción para el período {resultado['proximo_periodo']}: "
        f"${resultado['prediccion']:,.2f}"
    )

    print("\nEjemplo de columna normalizada con NumPy:")
    print(
        df_normalizado[["Producto", "Total_Venta", "Venta_Normalizada"]]
        .head(5)
        .to_string(index=False)
    )


def ejecutar_programa():
    """Ejecuta el menú principal del programa."""
    df_original = cargar_dataset()
    df = preparar_dataset(df_original)
    analizador = AnalizadorVentas(df)
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_primeras_filas(df)
        elif opcion == "2":
            mostrar_resumen_estadistico(df)
        elif opcion == "3":
            mostrar_ventas_por_categoria(df)
        elif opcion == "4":
            monto_minimo = pedir_monto_minimo()
            ventas_filtradas = filtrar_ventas_importantes(df, monto_minimo)
            print(f"\nVentas encontradas con total mayor o igual a ${monto_minimo:,.2f}:")
            print(ventas_filtradas.head(15).to_string(index=False))
            print(f"\nCantidad de ventas encontradas: {len(ventas_filtradas)}")
        elif opcion == "5":
            rutas_graficos = generar_graficos(df)
            print("\nGráficos generados correctamente:")

            for ruta in rutas_graficos:
                print(f"- {ruta}")
        elif opcion == "6":
            mostrar_prediccion(analizador)
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()
