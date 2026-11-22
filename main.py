"""
Archivo principal del sistema 

Este archivo ejecuta diferentes pruebas para
demostrar el funcionamiento del sistema y el
manejo de excepciones.
"""

import logging

from clase_cliente import Cliente
from Servicio_reservar_sala import ReservaSala
from Servicio_alquiler_equipo import AlquilerEquipo
from Servicio_asesoria_especializada import AsesoriaEspecializada
from reserva import Reserva


# ==================================
# CONFIGURACIÓN DEL LOG
# ==================================

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("===== SOFTWARE FJ =====\n")

# ==================================
# CLIENTES
# ==================================

try:
    cliente1 = Cliente(
        1,
        "Juan Perez",
        "juan@email.com"
    )

    print("Cliente 1 creado correctamente")

except Exception as e:

    print("Error:", e)
    logging.error(e)

try:

    cliente2 = Cliente(
        2,
        "Maria Lopez",
        "maria@email.com"
    )

    print("Cliente 2 creado correctamente")

except Exception as e:

    print("Error:", e)
    logging.error(e)

# ==================================
# CLIENTE INVÁLIDO
# ==================================

try:

    cliente3 = Cliente(
        3,
        "Al",
        "correo"
    )

except Exception as e:

    print("Error controlado:", e)
    logging.error(e)

# ==================================
# SERVICIOS
# ==================================

sala = ReservaSala(
    "Sala Ejecutiva",
    50000
)

equipo = AlquilerEquipo(
    "Portatil Empresarial",
    80000
)

asesoria = AsesoriaEspecializada(
    "Consultoria Python",
    120000
)

print("\nServicios creados correctamente")

# ==================================
# RESERVA EXITOSA
# ==================================

try:

    reserva1 = Reserva(
        cliente1,
        sala,
        4
    )

    costo = reserva1.procesar()

    print(
        f"\nReserva realizada. Costo: ${costo}"
    )

except Exception as e:

    logging.error(e)
    print(e)

# ==================================
# RESERVA CON ERROR
# ==================================

try:

    reserva2 = Reserva(
        cliente2,
        equipo,
        -5
    )

    reserva2.procesar()

except Exception as e:

    print(
        "Error controlado en reserva:",
        e
    )

    logging.error(e)

# ==================================
# SERVICIO INEXISTENTE
# ==================================

try:

    reserva3 = Reserva(
        cliente1,
        None,
        2
    )

    reserva3.procesar()

except Exception as e:

    print(
        "Error controlado:",
        e
    )

    logging.error(e)

# ==================================
# TRY - EXCEPT - ELSE
# ==================================

try:

    reserva1.confirmar()

except Exception as e:

    logging.error(e)

else:

    print(
        "\nReserva confirmada correctamente"
    )

# ==================================
# TRY - EXCEPT - FINALLY
# ==================================

try:

    archivo = open(
        "logs.txt",
        "r",
        encoding="utf-8"
    )

except Exception as e:

    print(e)

finally:

    print(
        "\nBloque FINALLY ejecutado"
    )

    try:
        archivo.close()
    except:
        pass

# ==================================
# FIN
# ==================================

print("\nSistema finalizado correctamente")