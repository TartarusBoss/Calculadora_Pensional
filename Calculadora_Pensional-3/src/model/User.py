class Usuario:
    def __init__(self, nombre, apellido, sexo, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad

    def EsIgual(self, comparar_con):
        assert(self.nombre == comparar_con.nombre)
        assert(self.apellido == comparar_con.apellido)        
        assert(self.sexo == comparar_con.sexo)
        assert(self.edad == comparar_con.edad)

        