COSTO_PREMIUM = 100000
COSTO_REGULAR = COSTO_PREMIUM * 0.2

hotel = {
    piso: {habitacion: {"estado": "libre", "costo": COSTO_PREMIUM if piso == 5 else COSTO_REGULAR} for habitacion in range(1, 9)}
    for piso in range(1, 6)
}
def reservar_habitacion(hotel):
    piso = int(input("Ingrese el número de piso (1-5): "))
    habitacion = int(input("Ingrese el número de habitación (1-8): "))
    if 1 <= piso <= 5 and 1 <= habitacion <= 8:
        if hotel[piso][habitacion]["estado"] == "libre":
            hotel[piso][habitacion]["estado"] = "reservada"
            print(f"Habitación {habitacion} del piso {piso} ha sido reservada.")
        else:
            print(f"La habitación {habitacion} del piso {piso} ya está reservada.")
    else:
        print("Número de piso o habitación inválido.")
def buscar_habitacion(hotel):
    piso = int(input("Ingrese el número de piso (1-5): "))
    habitacion = int(input("Ingrese el número de habitación (1-8): "))
    if 1 <= piso <= 5 and 1 <= habitacion <= 8:
        info = hotel[piso][habitacion]
        print(f"Piso: {piso}, Habitación: {habitacion}, Estado: {info['estado']}, Costo: {info['costo']} pesos")
    else:
        print("Número de piso o habitación inválido.")
def ver_estado_habitaciones(hotel):
    for piso, habitaciones in hotel.items():
        print(f"\nPiso {piso}:")
        for habitacion, detalles in habitaciones.items():
            print(f"  Habitación {habitacion} - Estado: {detalles['estado']}, Costo: {detalles['costo']} pesos")
def totalizar_ventas(hotel):
    total = 0
    for piso, habitaciones in hotel.items():
        for detalles in habitaciones.values():
            if detalles["estado"] == "reservada":
                total += detalles["costo"]
    print(f"Total de ventas del día: {total} pesos")
def guardar_informacion(hotel):
    with open("hotel.txt", "w") as file:
        for piso, habitaciones in hotel.items():
            file.write(f"Piso {piso}:\n")
            for habitacion, detalles in habitaciones.items():
                file.write(f"  Habitación {habitacion} - Estado: {detalles['estado']}, Costo: {detalles['costo']} pesos\n")
    print("Información guardada en hotel.txt")
def menu():
    while True:
        print("\nMenú Principal")
        print("1. Reservar habitaciones")
        print("2. Buscar habitación")
        print("3. Ver estado de las habitaciones")
        print("4. Totalizar ventas del día")
        print("5. Guardar información en archivo")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            reservar_habitacion(hotel)
        elif opcion == "2":
            buscar_habitacion(hotel)
        elif opcion == "3":
            ver_estado_habitaciones(hotel)
        elif opcion == "4":
            totalizar_ventas(hotel)
        elif opcion == "5":
            guardar_informacion(hotel)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


menu()
