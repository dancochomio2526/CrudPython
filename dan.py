import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("marvel.db")
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    poder TEXT NOT NULL
)
""")
conexion.commit()


# CREATE - Agregar héroe
def agregar_heroe():
    nombre = input("Nombre del superhéroe: ")
    poder = input("Poder del superhéroe: ")

    cursor.execute(
        "INSERT INTO heroes (nombre, poder) VALUES (?, ?)",
        (nombre, poder)
    )
    conexion.commit()

    print(f"\n{nombre} agregado correctamente.\n")


# READ - Mostrar catálogo
def mostrar_catalogo():
    cursor.execute("SELECT * FROM heroes")
    heroes = cursor.fetchall()

    if not heroes:
        print("\nEl catálogo está vacío.\n")
        return

    print("\n=== CATÁLOGO DE PODERES MARVEL ===")
    print("ID | HÉROE | PODER")
    print("-" * 40)

    for heroe in heroes:
        print(f"{heroe[0]} | {heroe[1]} | {heroe[2]}")

    print()


# UPDATE - Actualizar poder
def actualizar_heroe():
    id_heroe = input("Ingresa el ID del héroe a actualizar: ")
    nuevo_poder = input("Ingresa el nuevo poder: ")

    cursor.execute(
        "UPDATE heroes SET poder = ? WHERE id = ?",
        (nuevo_poder, id_heroe)
    )
    conexion.commit()

    if cursor.rowcount > 0:
        print("\nPoder actualizado correctamente.\n")
    else:
        print("\nNo se encontró un héroe con ese ID.\n")


# DELETE - Eliminar héroe
def eliminar_heroe():
    id_heroe = input("Ingresa el ID del héroe a eliminar: ")

    cursor.execute(
        "DELETE FROM heroes WHERE id = ?",
        (id_heroe,)
    )
    conexion.commit()

    if cursor.rowcount > 0:
        print("\nHéroe eliminado correctamente.\n")
    else:
        print("\nNo se encontró un héroe con ese ID.\n")


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
        conexion.close()  # Cerrar la conexión con SQLite
        break

    else:
        print("\nOpción no válida. Intenta nuevamente.\n")