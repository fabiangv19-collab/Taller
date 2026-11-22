from clase_abstracta_servicio import Servicio


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, valor_dia):
        super().__init__(nombre)
        self.valor_dia = valor_dia

    def calcular_costo(self, dias):
        return self.valor_dia * dias

    def descripcion(self):
        return "Servicio de alquiler de equipos"