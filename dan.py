# Catálogo de poderes de superhéroes de Marvel

catalogo = []

# CREATE - Agregar un héroe
def agregar_heroe():
    nombre = input("Nombre del superhéroe: ")
    poder = input("Poder del superhéroe: ")

    heroe = {
        "nombre": nombre,
        "poder": poder
    }

    catalogo.append(heroe)
    print(f"\n{nombre} agregado correctamente.\n")


# READ - Mostrar el catálogo
def mostrar_catalogo():
    if len(catalogo) == 0:
        print("\nEl catálogo está vacío.\n")
        return

    print("\n=== CATÁLOGO DE PODERES MARVEL ===")
    for i, heroe in enumerate(catalogo, start=1):
        print(f"{i}. {heroe['nombre']} - {heroe['poder']}")
    print()


# UPDATE - Actualizar un poder
def actualizar_heroe():
    nombre = input("Ingresa el nombre del héroe a actualizar: ")

    for heroe in catalogo:
        if heroe["nombre"].lower() == nombre.lower():
            nuevo_poder = input("Ingresa el nuevo poder: ")
            heroe["poder"] = nuevo_poder

            print(f"\nPoder de {nombre} actualizado correctamente.\n")
            return

    print("\nHéroe no encontrado.\n")


# DELETE - Eliminar un héroe
def eliminar_heroe():
    nombre = input("Ingresa el nombre del héroe a eliminar: ")

    for heroe in catalogo:
        if heroe["nombre"].lower() == nombre.lower():
            catalogo.remove(heroe)

            print(f"\n{nombre} eliminado del catálogo.\n")
            return

    print("\nHéroe no encontrado.\n")


# Menú principal
while True:
    print("=== CRUD CATÁLOGO MARVEL ===")
    print("1. Agregar héroe")
    print("2. Mostrar catálogo")
    print("3. Actualizar poder")
    print("4. Eliminar héroe")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_heroe()

    elif opcion == "2":
        mostrar_catalogo()

    elif opcion == "3":
        actualizar_heroe()

    elif opcion == "4":
        eliminar_heroe()

    elif opcion == "5":
        print("\n¡Hasta luego!")
        break

    else:
        print("\nOpción no válida. Intenta nuevamente.\n")
        