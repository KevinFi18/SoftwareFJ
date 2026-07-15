from servicio import Servicio


class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)
        self._capacidad = capacidad

    def calcular_costo(self, impuesto=0, descuento=0):
        return super().calcular_costo(impuesto, descuento)

    def descripcion(self):
        return f"Reserva de sala para {self._capacidad} personas."

    def validar(self):
        if self._capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, tipo_equipo):
        super().__init__(nombre, precio_base)
        self._tipo_equipo = tipo_equipo

    def calcular_costo(self, impuesto=0, descuento=0):
        return super().calcular_costo(impuesto, descuento)

    def descripcion(self):
        return f"Alquiler del equipo: {self._tipo_equipo}"

    def validar(self):
        if self._tipo_equipo.strip() == "":
            raise ValueError("Debe indicar el tipo de equipo.")


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, especialidad):
        super().__init__(nombre, precio_base)
        self._especialidad = especialidad

    def calcular_costo(self, impuesto=0, descuento=0):
        return super().calcular_costo(impuesto, descuento)

    def descripcion(self):
        return f"Asesoría especializada en {self._especialidad}"

    def validar(self):
        if self._especialidad.strip() == "":
            raise ValueError("Debe indicar la especialidad.")