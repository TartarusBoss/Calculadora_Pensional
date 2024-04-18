import sys
sys.path.append("C:/Users/ASUS/Calculadora_Pensional-2")  
from src.CodigoPension import CalculadoraPensional

def main():
    calculadora = CalculadoraPensional()

    print("Bienvenido a la calculadora pensional")

    """Inicializamos el menú con 3 opciones"""
    while True:
        print("\nSeleccione una opción: ")
        print("1. Calcular ahorro pensional. ")
        print("2. Calcular pensión. ")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        """En este try se intenta retornar el ahorro pensional, y si hay mensaje de error también se retorna"""
        if opcion == "1":
            try:
                edad = int(input("Ingrese su edad (1-90): "))
                salario = float(input("Ingrese su salario mensual: "))
                semanas_laboradas = int(input("Ingrese el número de semanas laboradas: "))
                rentabilidad_fondo = float(input("Ingrese la rentabilidad del fondo (Como decimal (0.04)): "))
                tasa_administracion = float(input("Ingrese la tasa de administración (Como decimal (0.02)): "))

                ahorro_pensional, mensaje_error = calculadora.calculo_ahorro_pensional(edad, salario, semanas_laboradas, rentabilidad_fondo, tasa_administracion)

                if ahorro_pensional is not None:
                    print(f"El ahorro pensional esperado es: {ahorro_pensional}, {mensaje_error}")
                else: 
                    print(f"Error en el cálculo del ahorro pensional: {mensaje_error}")
            except (ValueError, TypeError) as e:
                print(f"Error, Ha ingresado un dato inválido. {e}")
                
            """En este try se maneja el calculo pensional de la misma manera, se retorna la pension y si hay mensaje de error, también lo hace"""
        elif opcion == "2":
            try:
                edad = int(input("Ingrese su edad (1-90): "))
                ahorro_pensional_esperado = float(input("Ingrese el ahorro pensional esperado: "))         
                esperanza_vida = int(input("Ingrese su esperanza de vida: "))   
                sexo = input("Ingrese su sexo ('masculino' o 'femenino'): ")
                estado_civil = input("Ingrese su estado civil ('soltero' o 'casado'): ") 

                pension, mensaje_error = calculadora.calculo_pension(edad, ahorro_pensional_esperado, sexo, estado_civil, esperanza_vida)            

                if pension is not None:
                    print(f"La pensión esperada es: {pension}, {mensaje_error}")
                else:
                    print(f"Error en el cálculo de la pensión: {mensaje_error}")
            except (ValueError, TypeError) as e:
                print(f"Error, Ha ingresado un dato inválido. {e}")

        elif opcion == "3":
            print("Gracias por usar la calculadora pensional!")
            break

        else:
            print("Opción no válida, seleccione una opción válida. ")    


if __name__ == "__main__":
    main()
