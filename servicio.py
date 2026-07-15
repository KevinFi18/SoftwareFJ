from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Clase abstracta que representa un servicio de Software FJ.
    """

    def __init__(self, nombre, precio_base):
        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._nombre = nombre
        self._precio_base = precio_base

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def validar(self):
        pass

    # Sobrecarga simulada mediante parámetros opcionales
    def calcular_costo(self, impuesto=0, descuento=0):
        """
        Calcula el costo final del servicio aplicando
        impuestos y descuentos opcionales.
        """
        total = self._precio_base
        total += total * (impuesto / 100)
        total -= total * (descuento / 100)
        return total