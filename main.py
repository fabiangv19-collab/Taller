"""
Archivo principal del sistema de gestión de clientes,
servicios y reservas.

Este archivo tiene como objetivo demostrar el uso de:

- Programación Orientada a Objetos.
- Abstracción.
- Herencia.
- Polimorfismo.
- Encapsulación.
- Manejo de excepciones.
- Registro de eventos y errores en archivos de log.
"""

# Importación del módulo logging para registrar
# eventos y errores ocurridos durante la ejecución.
import logging

# Importación de la clase Cliente.
from clase_cliente import Cliente

# Importación de los tres servicios especializados.
from servicio_reservar_sala import ReservaSala
from servicio_alquiler_equipo import AlquilerEquipo
from servicio_asesoria_especializada import AsesoriaEspecializada

# Importación de la clase Reserva.
from reserva import Reserva


# ==================================================
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# ==================================================
#
# filename:
# Nombre del archivo donde se almacenarán
# los eventos y errores.
#
# level:
# Indica el nivel mínimo de mensajes que serán
# registrados.
#
# format:
# Define el formato en que se guardarán los datos.
#
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Título principal mostrado al usuario.
print("===== SOFTWARE RESERVAR SALAS=====\n")


# ==================================================
# REGISTRO DE CLIENTE VÁLIDO 1
# ==================================================
#
# Se intenta crear un cliente con información válida.
#
try:

    cliente1 = Cliente(
        1,
        "Juan Perez",
        "juan@email.com"
    )

    print("Cliente 1 creado correctamente")

    # Registro exitoso en el log.
    logging.info("Cliente 1 registrado correctamente")

except Exception as e:

    # Captura cualquier error ocurrido durante la creación.
    print("Error:", e)

    # Registro del error en el log.
    logging.error(e)


# ==================================================
# REGISTRO DE CLIENTE VÁLIDO 2
# ==================================================
#
# Segundo cliente con datos correctos.
#
try:

    cliente2 = Cliente(
        2,
        "Maria Lopez",
        "maria@email.com"
    )

    print("Cliente 2 creado correctamente")

    logging.info("Cliente 2 registrado correctamente")

except Exception as e:

    print("Error:", e)

    logging.error(e)


# ==================================================
# REGISTRO DE CLIENTE INVÁLIDO
# ==================================================
#
# Se intenta registrar un cliente con un nombre
# demasiado corto para activar una excepción.
#
try:

    cliente3 = Cliente(
        3,
        "Al",
        "correo"
    )

except Exception as e:

    print("Error controlado:", e)

    logging.error(e)


# ==================================================
# CREACIÓN DE SERVICIOS
# ==================================================
#
# Se crean los tres servicios exigidos por el ejercicio.
#
# Servicio de reserva de salas.
sala = ReservaSala(
    "Sala Ejecutiva",
    50000
)

# Servicio de alquiler de equipos.
equipo = AlquilerEquipo(
    "Portatil Empresarial",
    80000
)

# Servicio de asesoría especializada.
asesoria = AsesoriaEspecializada(
    "Consultoria Python",
    120000
)

print("\nServicios creados correctamente")

logging.info("Servicios registrados correctamente")


# ==================================================
# RESERVA EXITOSA
# ==================================================
#
# Se crea una reserva válida para demostrar
# el funcionamiento correcto del sistema.
#
try:

    reserva1 = Reserva(
        cliente1,
        sala,
        4
    )

    # Procesamiento de la reserva.
    costo = reserva1.procesar()

    print(
        f"\nReserva realizada. Costo: ${costo}"
    )

    logging.info(
        f"Reserva exitosa. Costo: {costo}"
    )

except Exception as e:

    logging.error(e)

    print(e)


# ==================================================
# RESERVA INVÁLIDA
# ==================================================
#
# Se intenta realizar una reserva con duración
# negativa para activar una excepción.
#
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


# ==================================================
# SERVICIO INEXISTENTE
# ==================================================
#
# Se intenta crear una reserva sin servicio
# asociado para generar un error controlado.
#
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


# ==================================================
# DEMOSTRACIÓN DE TRY / EXCEPT / ELSE
# ==================================================
#
# ELSE se ejecuta solamente cuando no ocurre
# ninguna excepción dentro del bloque TRY.
#
try:

    reserva1.confirmar()

except Exception as e:

    logging.error(e)

else:

    print(
        "\nReserva confirmada correctamente"
    )

    logging.info(
        "Reserva confirmada"
    )


# ==================================================
# DEMOSTRACIÓN DE TRY / EXCEPT / FINALLY
# ==================================================
#
# FINALLY siempre se ejecuta, incluso cuando se
# produce un error.
#
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


# ==================================================
# RESUMEN GENERAL DEL SISTEMA
# ==================================================
#
# Mensaje final que indica que la ejecución
# terminó correctamente.
#
print(
    "\nSistema finalizado correctamente"
)

logging.info(
    "Sistema finalizado correctamente"
)