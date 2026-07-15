from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva


def main():

    print("========== SOFTWARE FJ ==========\n")

    clientes = []
    servicios = []
    reservas = []

    # OPERACIÓN 1: Registrar cliente válido
    try:
        cliente1 = Cliente(
            "Kevin Figueroa",
            "123456789",
            "kevin@gmail.com",
            "3001234567"
        )

        clientes.append(cliente1)

        print("OPERACIÓN 1")
        print("Cliente registrado correctamente.\n")

    except Exception as error:
        print(f"Error al registrar cliente: {error}\n")

    # OPERACIÓN 2: Registrar cliente inválido
    try:
        cliente2 = Cliente(
            "Juan Pérez",
            "987654321",
            "juan@gmail.com",
            "ABC123"
        )

        clientes.append(cliente2)

    except Exception as error:
        print("OPERACIÓN 2")
        print(f"Error controlado: {error}\n")

    # OPERACIÓN 3: Crear una reserva de sala válida
    try:
        sala = ReservaSala(
            "Sala Premium",
            120000,
            20
        )

        sala.validar()
        servicios.append(sala)

        print("OPERACIÓN 3")
        print("Servicio de sala creado correctamente.\n")

    except Exception as error:
        print("OPERACIÓN 3")
        print(f"Error controlado: {error}\n")

    # OPERACIÓN 4: Crear un alquiler de equipo válido
    try:
        equipo = AlquilerEquipo(
            "Alquiler de portátil",
            80000,
            "Computador portátil"
        )

        equipo.validar()
        servicios.append(equipo)

        print("OPERACIÓN 4")
        print("Servicio de alquiler creado correctamente.\n")

    except Exception as error:
        print("OPERACIÓN 4")
        print(f"Error controlado: {error}\n")

    # OPERACIÓN 5: Crear una asesoría válida
    try:
        asesoria = AsesoriaEspecializada(
            "Asesoría en programación",
            150000,
            "Desarrollo de software"
        )

        asesoria.validar()
        servicios.append(asesoria)

        print("OPERACIÓN 5")
        print("Servicio de asesoría creado correctamente.\n")

    except Exception as error:
        print("OPERACIÓN 5")
        print(f"Error controlado: {error}\n")
            # OPERACIÓN 6: Mostrar todos los servicios (Polimorfismo)
    print("OPERACIÓN 6")
    print("Servicios registrados:\n")

    for servicio in servicios:
        print(servicio.descripcion())
        print(f"Costo normal: ${servicio.calcular_costo()}")
        print(f"Costo con IVA (19%): ${servicio.calcular_costo(impuesto=19)}")
        print("-" * 40)

    print()
            # OPERACIÓN 7: Crear una reserva válida
    print("OPERACIÓN 7")

    reserva1 = Reserva(cliente1, sala, 2)

    if reserva1.procesar():
        reservas.append(reserva1)
        print("Reserva agregada correctamente.\n")
    else:
        print("La reserva no fue agregada.\n")


    # OPERACIÓN 8: Crear una reserva inválida
    print("OPERACIÓN 8")

    reserva2 = Reserva(cliente1, equipo, -3)

    if reserva2.procesar():
        reservas.append(reserva2)
        print("Reserva agregada correctamente.\n")
    else:
        print("La reserva inválida no fue agregada.\n")


    # OPERACIÓN 9: Cancelar una reserva
    print("OPERACIÓN 9")

    reserva1.cancelar()

    print("Reserva cancelada correctamente.\n")


    # OPERACIÓN 10: Mostrar todas las reservas
    print("OPERACIÓN 10")
    print("Listado de reservas:\n")

    for reserva in reservas:
        print(reserva.mostrar_reserva())
        print("-" * 40)

    print("\n========== FIN DEL PROGRAMA ==========")
if __name__ == "__main__":
    main()