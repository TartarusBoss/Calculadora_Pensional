import sys
sys.path.append("C:/Users/ASUS/Calculadora_Pensional-2")
from interfaz_grafica.calculadora_app import CalculadoraPensionalApp
from src.main import main

def seleccionar_interfaz(opcion):
    if opcion == "1":
        main()
    elif opcion == "2":
        # Ejecutar la interfaz gráfica
        app = CalculadoraPensionalApp()
        app.run()
    else:
        print("Opción inválida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    opcion = input("Seleccione una opción: (1 para interfaz por consola, 2 para interfaz gráfica): ")
    seleccionar_interfaz(opcion)
