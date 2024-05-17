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



### IMPORTANTE:  
Al ser un proyecto modular, puede que hayan mínimos inconvenientes con las carpetas o módulos, especialmente errores encontrando los módulos, para manejar eso utilizamos sys
En los archivos app_controller, consola_controlador, consola_aplicacion, calculadora_app, ControladorTests y PensionTests se debe agregar la ruta en la cual descargaste el repositorio, en mi caso es esta
sys.path.append("C:/Users/ASUS/testCalculadora/Calculadora_Pensional-3")
Dicho paso es obligatorio, ten en cuenta que tienes que reemplazar la ruta "C:/Users/ASUS/Calculadora_Pensional-3" por la ruta en la cual está ubicado el proyecto localmente en tu computador, el problema ahí es que intentamos usar la ruta "../Calculadora-Pensional-3" Que se supone que agrega todo el directorio, pero se bugea con el src, por lo tanto es obligatorio hacer el paso anterior


# Instrucciones de uso
## Para ejecutar el código sin editor de código
- Tener instalado Python en el sistema.
- Darle al botón de "Code" en el repositorio, descargar el código de Github en formato ZIP: [Repositorio en Github](https://github.com/TartarusBoss/Calculadora_Pensional.git)
- Extraer el ZIP y abrir la carpeta.
- Ya ubicados en la carpeta llamada "Calculadora_Pensional-3" copiamos la ruta del directorio

## Para ejecutarlo desde consola (CMD)
- Abrir la consola o terminal.
- Cambiarse al directorio donde está ubicado el script que desea ejecutar. En mi caso es este: `C:\Users\ASUS\Downloads\Calculadora_Pensional-main\Calculadora_Pensional-3`,
dicho paso se hace de la siguiente manera -> cd C:\Users\ASUS\Downloads\Calculadora_Pensional-main\Calculadora_Pensional-3
- Para ejecutar la consola del programa vamos al directorio console asi -> cd C:\Users\ASUS\testCalculadora\Calculadora_Pensional-3\src\view\console (No olvides cambiar tu ruta), y ejecutamos consola_aplicacion asi ->  python consola_aplicacion.py, ahi podrás interactuar con la consola
- Para ejecutar la consola del controlador (base de datos) es en el mismo directorio que la consola de la aplicación, solo que ejecutaremos un archivo distinto, en este caso se coloca python consola_controlador.py. posteriormente podrás interactuar con la consola de la base de datos
- Para ejecutar la interfaz gráfica del programa hay que moverse al directorio donde está ubicado el archivo, que sería "interface", se escribe cd C:\Users\ASUS\testCalculadora\Calculadora_Pensional-3\src\view\interface (NO OLVIDES REEMPLAZAR TU RUTA), posteriormente se escribe python calculadora_app.py y se interactua con la consola

## Para ejecutarlo desde VsCode (u otro editor)
- Instalar y extraer el Zip del proyecto.
- Abrir con el editor.
- Ejecutar el archivo deseado

## Para clonarlo
- Presionar el botón "Code" en el repositorio y copiar el enlace.
- Clonar el repositorio.

## Para ejecutar las pruebas del programa
Cambiar la carpeta que contiene el proyecto al path usando -> sys.path.append("C:/Users/ASUS/testCalculadora/Calculadora_Pensional-3") 
- IMPORTANTE - Tener en cuenta que está ruta en el código: sys.path.append("C:/Users/ASUS/testCalculadora/Calculadora_Pensional-3") tiene que
ser personalizada, coloca la ruta en la cuál está ubicado el código en tu propio PC
- Por ejemplo en mi caso, cambié esa instrucción por sys.path.append("C:/Users/ASUS/testCalculadora/Calculadora_Pensional-3")
- Abrir la terminal o cmd, cd hasta la carpeta de tests (Donde esté ubicado en tu PC) -> En mi caso: cd C:\Users\ASUS\Calculadora_Pensional-3/tests
- Correr las pruebas con la instruccción python PensionTests.py

## Para ejecutar las pruebas del controlador
- Nos movemos al directorio donde están ubicadas nuestras pruebas, en mi caso es cd C:\Users\ASUS\testCalculadora\Calculadora_Pensional-3\tests\    -> Escribimos ControladorTests.py y esperamos a que carguen
-Visualizar las pruebas


## Licencia
Este proyecto está bajo la licencia MIT.

## Contactos
- Matías Herrera: Estudiante Ing. Sistemas

¡Gracias!
