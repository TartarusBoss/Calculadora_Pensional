import sys
sys.path.append("C:/Users/ASUS/testCalculadoraCalculadora_Pensional-3")
import unittest
from src.model.User import Usuario

from src.controller.app_controller import ControladorUsuarios
class ControladorUsuariosTest(unittest.TestCase):

    def setUp(self):
        self.controlador = ControladorUsuarios()

    def test_InsertarUsuarioNormal(self):

        usuario_prueba = Usuario(nombre="Pepito", apellido="Perez", sexo="masculino", edad=30)
        self.controlador.InsertarUsuario(usuario_prueba)
        usuarios = self.controlador.ObtenerUsuarios()
        nombres_insertados = [usuario.nombre for usuario in usuarios]
        self.assertIn(usuario_prueba.nombre, nombres_insertados)

    def test_InsertarUsuarioError(self):

        with self.assertRaises(ValueError):
            usuario_prueba = Usuario(nombre="", apellido="Perez", sexo="masculino", edad=30)
            self.controlador.InsertarUsuario(usuario_prueba)

    def testModificarUsuarioNormal(self):
        usuario_original = Usuario(nombre="Juan", apellido="Perez", sexo="masculino", edad=30)
        self.controlador.InsertarUsuario(usuario_original)
        usuarios = self.controlador.ObtenerUsuarios()
        usuario_insertado = usuarios[0] 
        usuario_modificado = Usuario(nombre="JuanCarlos", apellido="Gomez", sexo="masculino", edad=35)

        self.controlador.ModificarUsuario(usuario_insertado.id, usuario_modificado.nombre, usuario_modificado.apellido, usuario_modificado.sexo, usuario_modificado.edad)
        usuario_actualizado = self.controlador.ObtenerUsuarioPorID(usuario_insertado.id)
        self.assertEqual(usuario_actualizado.nombre, usuario_modificado.nombre)
        self.assertEqual(usuario_actualizado.apellido, usuario_modificado.apellido)
        self.assertEqual(usuario_actualizado.sexo, usuario_modificado.sexo)
        self.assertEqual(usuario_actualizado.edad, usuario_modificado.edad)

    def testModificarUsuarioError(self):
        usuario_original = Usuario(nombre="Juan", apellido="Perez", sexo="masculino", edad=30)
        id_usuario_insertado = self.controlador.InsertarUsuario(usuario_original)
        id_usuario_inexistente = 99999
        usuario_modificado = Usuario(nombre="Juan Carlos", apellido="Gomez", sexo="masculino", edad=35)
        with self.assertRaises(ValueError):
            self.controlador.ModificarUsuario(id_usuario_inexistente, usuario_modificado.nombre, usuario_modificado.apellido, usuario_modificado.sexo, usuario_modificado.edad)

    def testEliminarUsuarioNormal(self):

        usuarios_antes = self.controlador.ObtenerUsuarios()
        self.assertGreater(len(usuarios_antes), 0, "No hay usuarios disponibles para eliminar.")

        # Seleccionar un usuario existente para eliminar
        usuario_a_eliminar = usuarios_antes[0]
        self.controlador.EliminarUsuario(usuario_a_eliminar.id)
        usuarios_despues = self.controlador.ObtenerUsuarios()
        nombres_usuarios = [usuario.nombre for usuario in usuarios_despues]
        self.assertNotIn(usuario_a_eliminar.nombre, nombres_usuarios)

    def testEliminarUsuarioInexistente(self):

        usuarios = self.controlador.ObtenerUsuarios()
        ids_usuarios_existentes = [usuario.id for usuario in usuarios]
        id_usuario_inexistente = max(ids_usuarios_existentes) + 1 if ids_usuarios_existentes else 1
        self.assertNotIn(id_usuario_inexistente, ids_usuarios_existentes)
        with self.assertRaises(ValueError, msg="No se lanzó la excepción esperada al intentar eliminar un usuario inexistente"):
            self.controlador.EliminarUsuario(id_usuario_inexistente)

    def testListarUsuariosNormal(self):
        """Prueba que la lista de usuarios se obtenga correctamente."""
        # Insertar algunos usuarios de prueba
        usuario1 = Usuario(nombre="Juan", apellido="Perez", sexo="masculino", edad=30)
        usuario2 = Usuario(nombre="Maria", apellido="Gomez", sexo="femenino", edad=25)
        self.controlador.InsertarUsuario(usuario1)
        self.controlador.InsertarUsuario(usuario2)

        # Obtener la lista de usuarios
        usuarios = self.controlador.ObtenerUsuarios()

        # Verificar que la lista contenga los usuarios insertados
        nombres_usuarios = [usuario.nombre for usuario in usuarios]
        self.assertIn(usuario1.nombre, nombres_usuarios)
        self.assertIn(usuario2.nombre, nombres_usuarios)



    def testListarUsuariosError(self):
        """Prueba el manejo de errores cuando la función ObtenerUsuarios() devuelve un resultado inesperado."""
        # Simular un escenario donde la función ObtenerUsuarios() devuelve un resultado inesperado
        resultado_inesperado = "usuarios incorrectos"
        self.controlador.usuarios = resultado_inesperado  # Sobrescribir el atributo usuarios con el resultado inesperado

        # Llamar a la función que se está probando
        usuarios = self.controlador.ObtenerUsuarios()

        # Verificar que el resultado no sea una lista
        self.assertNotIsInstance(usuarios, list, "El resultado no debería ser una lista")

        # Verificar que el resultado sea igual al valor inesperado
        self.assertEqual(usuarios, resultado_inesperado, "El resultado debería ser igual al valor inesperado")

    def testRealizarCalculoNormal(self):
        """Prueba el cálculo normal de una operación."""
        # Supongamos un escenario de cálculo específico y probemos el resultado
        pass

    def testRealizarCalculoError(self):
        """Prueba que se maneje correctamente un error durante el cálculo."""
        # Probemos un escenario donde el cálculo debería fallar y verifiquemos que se maneje adecuadamente
        pass

    def testHistorialNormal(self):
        """Prueba que el historial de cálculos se obtenga correctamente."""
        # Insertar un usuario de prueba en la base de datos
        usuario_prueba = Usuario(nombre="Prueba", apellido="Usuario", sexo="masculino", edad=30)
        id_usuario_prueba = self.controlador.InsertarUsuario(usuario_prueba)

        # Insertar un resultado de cálculo para el usuario
        self.controlador.InsertarResultadoCalculo(id_usuario_prueba, "ahorro_pensional", 5000)

        # Obtener el historial de cálculos
        historial = self.controlador.ObtenerHistorialCalculos()

        # Verificar que el historial sea una lista
        self.assertIsInstance(historial, list, "El historial de cálculos debe ser una lista")

        # Verificar que el historial contenga el resultado de cálculo insertado
        resultado_esperado = (None, id_usuario_prueba, f"{usuario_prueba.nombre} {usuario_prueba.apellido}", "ahorro_pensional", 5000, None)
        self.assertIn(resultado_esperado, historial, "El resultado de cálculo insertado no se encuentra en el historial")

        # Limpiar el usuario de prueba insertado
        self.controlador.EliminarUsuario(id_usuario_prueba)

    def testHistorialError(self):

        pass

if __name__ == '__main__':
    unittest.main()
