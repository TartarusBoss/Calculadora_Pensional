# Título del proyecto
Calculadora pensional

# Desarrolladores
Matías Herrera - Daniel Alzate   
Estudiantes de ingeniería en sistemas - UdeM  
Entrega #3 de Código Limpio

## Descripción - Propósito
Este proyecto tiene como objetivo proporcionar una herramienta alternativa para calcular el ahorro pensional y la pensión esperada de los usuarios en el contexto de Colombia. Esta calculadora recopila una variedad de datos permitiendo estimar cuánto es el ahorro pensional en el momento, y cuál es la pensión que se podría recibir en un futuro. Es parte de la práctica 2 de código limpio.

## Arquitectura
El proyecto tiene una arquitectura modular y estructurada, con una separación entre la lógica de negocio, la interfaz de usuario, las interfaces gráficas y las pruebas. Está hecho en Python con Kivy para la interfaz gráfica, y unittest para las pruebas. y usa principalmente los principios de la POO.

### Bibliotecas y Dependencias
El proyecto utiliza una tres bibliotecas de Python para su funcionamiento, las cuales son:

-sys: módulo de python que sirve para encontrar rutas o modulos dentro del proyecto
- kivy: gestor de la interfaz gráfica
- unittest: Se usa para escribir, gestionar y ejecutar las pruebas unitarias del programa.



### IMPORTANTE:  -------> Tutorial de instalación: https://youtu.be/QbtQUw8Toc8
Al ser un proyecto modular, puede que hayan mínimos inconvenientes con las carpetas o módulos, especialmente errores encontrando los módulos, para manejar eso utilizamos sys
En el archivo interfaz_grafica/calculadora_app; se utiliza sys.path.append("C:/Users/ASUS/Calculadora_Pensional-2") para agregar la carpeta en la que está ubicado el archivo al path.
Dicho paso es obligatorio, ten en cuenta que tienes que reemplazar la ruta "C:/Users/ASUS/Calculadora_Pensional-2" por la ruta en la cual está ubicado el proyecto localmente, lo mismo con seleccionar_interfaz/selector_interfaz -> repetir el mismo paso (cambiar la ruta por la que está en tu PC) igualmente con src/main.py y tests/PensionTests.py



# Instrucciones de uso
## Para ejecutar el código sin editor de código
- Tener instalado Python en el sistema.
- Darle al botón de "Code" en el repositorio, descargar el código de Github en formato ZIP: [Repositorio en Github](https://github.com/TartarusBoss/Calculadora_Pensional.git)
- Extraer el ZIP y abrir la carpeta.
- Ya ubicados en la carpeta llamada "Calculadora_Pensional" damos clic al archivo "selector_interfaz.py".
- Digitar la opción que desea, (1 para consola, 2 para interfaz gráfica).
- Disfrute del programa!

## Para ejecutarlo desde consola (CMD)
- Abrir la consola o terminal.
- Cambiarse al directorio donde está ubicado el script "selector_interfaz" (Está en la carpeta del ZIP previamente extraído). En mi caso es este: `C:\Users\ASUS\Calculadora_Pensional`,
dicho paso se hace de la siguiente manera -> cd C:\Users\ASUS\Calculadora_Pensional-2
- Para ejecutar el programa se escribe: `python selector_interfaz.py`.
- Interactuar con la interfaz (seleccione la interfaz que desee.

## Para ejecutarlo desde VsCode (u otro editor)
- Instalar y extraer el Zip del proyecto.
- Abrir con el editor.
- Ejecutar el archivo de selector_interfaz para la interfaz, y el de PensionTests para las pruebas.

## Para clonarlo
- Presionar el botón "Code" en el repositorio y copiar el enlace.
- Clonar el repositorio.
- Ejecutar el archivo main.py.

## Para ejecutar las pruebas
- Agregar la carpeta que contiene el proyecto al path usando -> sys.path.append("C:/Users/b12s304.B12_304_01/Calculadora_Pensional") 
- IMPORTANTE - Tener en cuenta que está ruta en el código: sys.path.append("C:/Users/b12s304.B12_304_01/Calculadora_Pensional") tiene que
ser personalizada, coloca la ruta en la cuál está ubicado el código en tu propio PC
- Por ejemplo en mi caso, cambié esa instrucción por sys.path.append("C:/Users/ASUS/PycharmProjects/Calculadora_Pensional")
- Abrir la terminal o cmd, cd hasta la carpeta de tests (Donde esté ubicado en tu PC) -> En mi caso: cd C:\Users\ASUS\Calculadora_Pensional-2/tests
- Correr las pruebas con la instruccción python PensionTests.py

## Licencia
Este proyecto está bajo la licencia MIT.

## Contactos
- Matías Herrera: Estudiante Ing. Sistemas
- Daniel Alzate: Estudiante Ing. Sistemas

¡Gracias!
