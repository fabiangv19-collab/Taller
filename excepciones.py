"""
Archivo: excepciones.py

Contiene todas las excepciones personalizadas
del sistema Software FJ.
"""


class ClienteInvalidoError(Exception):
    """
    Se genera cuando los datos del cliente
    no cumplen las validaciones.
    """
    pass


class ServicioNoDisponibleError(Exception):
    """
    Se genera cuando un servicio no existe
    o no está disponible.
    """
    pass


class ReservaError(Exception):
    """
    Se genera cuando una reserva presenta
    errores durante el procesamiento.
    """
    pass