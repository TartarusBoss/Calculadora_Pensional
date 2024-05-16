import sys
sys.path.append("C:/Users/ASUS/testCalculadora/Calculadora_Pensional-3")
import unittest
from src.model.User import Usuario

from src.controller.app_controller import ControladorUsuarios
class ControladorUsuariosTest(unittest.TestCase):

    def setUp(self):
        self.controlador = ControladorUsuarios()

    def testInsertarUsuarioNormal(self):
        usuario_prueba = Usuario(nombre="Pepito", apellido="Perez", sexo="masculino", edad=30)
        self.controlador.InsertarUsuario(usuario_prueba)
        usuarios = self.controlador.ObtenerUsuarios()
        nombres_insertados = [usuario.nombre for usuario in usuarios]
        self.assertIn(usuario_prueba.nombre, nombres_insertados)

    def testInsertarUsuarioError(self):
        with self.assertRaises(ValueError):
            usuario_prueba = Usuario(nombre="", apellido="Perez", sexo="masculino", edad=30)
            self.controlador.InsertarUsuario(usuario_prueba)

    def testModificarUsuarioNormal(self):
        self.controlador.EliminarTodosUsuarios()        
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

    def testModificarUsuarioError(self): #ID INEXISTENTE
        usuario_original = Usuario(nombre="Juan", apellido="Perez", sexo="masculino", edad=30)
        id_usuario_insertado = self.controlador.InsertarUsuario(usuario_original)
        id_usuario_inexistente = 99999
        usuario_modificado = Usuario(nombre="Juan Carlos", apellido="Gomez", sexo="masculino", edad=35)
        with self.assertRaises(ValueError):
            self.controlador.ModificarUsuario(id_usuario_inexistente, usuario_modificado.nombre, usuario_modificado.apellido, usuario_modificado.sexo, usuario_modificado.edad)

    def testEliminarUsuarioNormal(self):

        usuario_prueba = Usuario(nombre="Nuevo", apellido="Usuario", sexo="masculino", edad=25)
        self.controlador.InsertarUsuario(usuario_prueba)
        usuarios_antes = self.controlador.ObtenerUsuarios()
        self.assertGreater(len(usuarios_antes), 0, "No hay usuarios disponibles para eliminar.")
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

    def test_ListarUsuariosNormal(self):

        usuario_prueba = Usuario(nombre="Pepito", apellido="Perez", sexo="masculino", edad=30)
        self.controlador.InsertarUsuario(usuario_prueba)
        usuarios = self.controlador.ObtenerUsuarios()
        self.assertGreater(len(usuarios), 0)

    def testListarUsuariosVacia(self):
        self.controlador.EliminarTodosUsuarios()
        usuarios = self.controlador.ObtenerUsuarios()        
        self.assertFalse(usuarios, "Se esperaba una lista de usuarios vacía")

    def testObtenerCalculoNormal(self):
        self.controlador.EliminarTodosUsuarios()
        usuario_prueba = Usuario(nombre="Matias", apellido="Herrera", sexo="masculino", edad=30)
        self.controlador.InsertarUsuario(usuario_prueba)       
        id_usuario = self.controlador.ObtenerUsuarios()[0].id
        tipo_calculo = "ahorro_pensional"
        resultado = 50000
        self.controlador.InsertarResultadoCalculo(id_usuario, tipo_calculo, resultado)
        resultados_calculo = self.controlador.ObtenerResultadosCalculo(id_usuario)
        self.assertIsNotNone(resultados_calculo)
        self.assertGreater(len(resultados_calculo), 0)

    def testObtenerCalculoError(self):
        id_usuario_inexistente = 99999
        with self.assertRaises(ValueError):
            # Esto debería lanzar una excepción porque el usuario no existe
            self.controlador.ObtenerResultadosCalculo(id_usuario_inexistente)

    def testHistorialNormal(self):
        self.controlador.EliminarTodosUsuarios()
        usuario_prueba = Usuario(nombre="Matias", apellido="Perez", sexo="masculino", edad=30)
        self.controlador.InsertarUsuario(usuario_prueba)
        id_usuario = self.controlador.ObtenerUsuarios()[0].id
        tipo_calculo = "ahorro_pensional"
        resultado = 80000
        self.controlador.InsertarResultadoCalculo(id_usuario, tipo_calculo, resultado)
        historial = self.controlador.ObtenerHistorialCalculos()
        self.assertIsNotNone(historial)
        self.assertGreater(len(historial), 0)

    def testHistorialError(self):
        self.controlador.EliminarTodosUsuarios()
        historial = self.controlador.ObtenerHistorialCalculos()
        self.assertIsNotNone(historial)
        self.assertEqual(len(historial), 0)

if __name__ == '__main__':
    unittest.main()
