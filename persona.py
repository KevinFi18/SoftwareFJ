from abc import ABC, abstractmethod

class Persona(ABC):
    """
    Clase abstracta que representa una persona del sistema.
    """

    def __init__(self, nombre, documento, correo):
        self._nombre = nombre
        self._documento = documento
        self._correo = correo

    @abstractmethod
    def mostrar_datos(self):
        pass
    