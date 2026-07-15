from datetime import datetime
from excepciones import ReservaInvalidaError


class Reserva:
    """
    Representa una reserva de un cliente para un servicio.
    """

    def __init__(self, cliente, servicio, duracion):
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"

    def registrar_log(self, mensaje):
        """
        Registra eventos y errores en logs.txt.
        """
        try:
            with open("logs.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"{datetime.now()} - {mensaje}\n")
        except OSError as error:
            print(f"No fue posible escribir en el archivo de logs: {error}")

    def confirmar(self):
        """
        Valida y confirma la reserva.
        """
        try:
            self._servicio.validar()

            if self._duracion <= 0:
                raise ValueError(
                    "La duración debe ser mayor que cero."
                )

            self._estado = "Confirmada"

            self.registrar_log(
                f"Reserva confirmada para {self._cliente._nombre}."
            )

        except Exception as error:
            self.registrar_log(
                f"Error al confirmar la reserva: {error}"
            )

            raise ReservaInvalidaError(
                "No fue posible confirmar la reserva."
            ) from error

    def cancelar(self):
        """
        Cancela una reserva confirmada.
        """
        if self._estado == "Cancelada":
            raise ReservaInvalidaError(
                "La reserva ya se encuentra cancelada."
            )

        self._estado = "Cancelada"

        self.registrar_log(
            f"Reserva cancelada para {self._cliente._nombre}."
        )

    def procesar(self):
        """
        Procesa la reserva usando try, except, else y finally.
        Retorna True si fue procesada correctamente.
        """
        resultado = False

        try:
            self.confirmar()

        except ReservaInvalidaError as error:
            print(f"Error controlado: {error}")
            self.registrar_log(f"Reserva rechazada: {error}")

        else:
            print("Reserva procesada correctamente.")
            resultado = True

        finally:
            self.registrar_log(
                "Finalizó el proceso de reserva."
            )

        return resultado

    def mostrar_reserva(self):
        """
        Retorna la información de la reserva.
        """
        return (
            f"Cliente: {self._cliente._nombre}\n"
            f"Servicio: {self._servicio._nombre}\n"
            f"Duración: {self._duracion} horas\n"
            f"Estado: {self._estado}"
        )