from clase_abstracta_entidad import Entidad


class Cliente(Entidad):

    def __init__(self, id_cliente, nombre, correo):

        super().__init__(id_cliente)

        self.__id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor.strip()) < 3:
            raise ValueError("El nombre es inválido")
        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if "@" not in valor:
            raise ValueError("Correo inválido")
        self.__correo = valor

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}"
