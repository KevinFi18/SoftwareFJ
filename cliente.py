from persona import Persona


class Cliente(Persona):
    """
    Clase que representa un cliente de Software FJ.
    """

    def __init__(self, nombre, documento, correo, telefono):
        super().__init__(nombre, documento, correo)

        if "@" not in correo or "." not in correo:
         raise ValueError("El correo electrónico no es válido.")
        if not documento.isdigit():
         raise ValueError("El documento solo debe contener números.")
        if len(documento) < 6:
         raise ValueError("Documento demasiado corto.")

        if not telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números.")

        self.__telefono = telefono

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        if not nuevo_telefono.isdigit():
            raise ValueError("El teléfono solo debe contener números.")
        self.__telefono = nuevo_telefono

    def mostrar_datos(self):
        return (
            f"Nombre: {self._nombre}\n"
            f"Documento: {self._documento}\n"
            f"Correo: {self._correo}\n"
            f"Teléfono: {self.__telefono}"
        )