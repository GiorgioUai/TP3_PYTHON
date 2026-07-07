"""
TP Integrador Python - Análisis de ventas de videojuegos.

Este archivo será el punto de entrada del proyecto.
En las próximas iteraciones se agregará la carga del CSV, las transformaciones,
las métricas, los gráficos y la predicción simple.
"""


def mostrar_menu():
    """Muestra las opciones principales del programa."""
    print("\n====== ANÁLISIS DE VENTAS DE VIDEOJUEGOS ======")
    print("1. Ver primeras filas del dataset")
    print("2. Ver resumen estadístico")
    print("3. Ver ventas por categoría")
    print("4. Generar gráficos")
    print("5. Ver predicción simple")
    print("0. Salir")


def ejecutar_programa():
    """Ejecuta el menú principal del programa."""
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Esta opción se completará cuando agreguemos el dataset.")
        elif opcion == "2":
            print("Esta opción se completará cuando agreguemos las métricas.")
        elif opcion == "3":
            print("Esta opción se completará cuando agreguemos el análisis por categoría.")
        elif opcion == "4":
            print("Esta opción se completará cuando agreguemos los gráficos.")
        elif opcion == "5":
            print("Esta opción se completará cuando agreguemos la predicción simple.")
        elif opcion == "0":
            print("Programa finalizado.")
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()
