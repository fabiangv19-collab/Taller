"""
Archivo: reserva.py

Clase que administra las reservas
realizadas por los clientes.
"""

from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        """
        Confirma la reserva.
        """
        self.estado = "Confirmada"

    def cancelar(self):
        """
        Cancela la reserva.
        """
        self.estado = "Cancelada"

    def procesar(self):
        """
        Procesa la reserva y calcula el costo.
        """

        try:

            if self.duracion <= 0:
                raise ReservaError(
                    "La duración debe ser mayor a cero."
                )

            if self.servicio is None:
                raise ReservaError(
                    "No existe un servicio asociado."
                )

            costo = self.servicio.calcular_costo(
                self.duracion
            )

            self.estado = "Procesada"

            return costo

        except Exception as e:

            raise ReservaError(
                "Error al procesar la reserva."
            ) from e