import sys
sys.path.append(".")
from src.view.interface.calculadora_app import CalculadoraPensionalApp
from src.view.console.consola_aplicacion import main


def ejecutar_consola():
    main()
def ejecutar_interfaz_grafica():
    app = CalculadoraPensionalApp
    app.run()
    
def seleccionar_interfaz(opcion):
    if opcion == "1":
        ejecutar_consola()
    elif opcion == "2":
        ejecutar_interfaz_grafica()
    else:
        print("Opción inválida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    opcion = input("Seleccione una opción: (1 para interfaz por consola, 2 para interfaz gráfica): ")
    seleccionar_interfaz(opcion)
