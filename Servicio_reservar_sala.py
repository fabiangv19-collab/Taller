from clase_abstracta_servicio import Servicio


class ReservaSala(Servicio):

    def __init__(self, nombre, valor_hora):
        super().__init__(nombre)
        self.valor_hora = valor_hora

    def calcular_costo(self, horas):
        return self.valor_hora * horas

    def descripcion(self):
        return "Servicio de alquiler de salas"
