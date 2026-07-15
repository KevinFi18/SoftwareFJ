class ClienteInvalidoError(Exception):
    """Excepción para clientes inválidos."""
    pass


class ServicioNoDisponibleError(Exception):
    """Excepción para servicios no disponibles."""
    pass


class ReservaInvalidaError(Exception):
    """Excepción para reservas inválidas."""
    pass


class CostoInvalidoError(Exception):
    """Excepción para costos inválidos."""
    pass