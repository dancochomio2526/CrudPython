from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Crear la base de datos y la tabla
def inicializar_db():
    conexion = sqlite3.connect('marvel.db')
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS heroes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        poder TEXT NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()


# CREATE - Agregar héroe
@app.route('/heroes', methods=['POST'])
def agregar_heroe():
    datos = request.get_json()

    conexion = sqlite3.connect('marvel.db')
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO heroes (nombre, poder) VALUES (?, ?)",
        (datos['nombre'], datos['poder'])
    )

    conexion.commit()

    nuevo_id = cursor.lastrowid
    conexion.close()

    return jsonify({
        "id": nuevo_id,
        "nombre": datos['nombre'],
        "poder": datos['poder']
    }), 201


# READ - Obtener todos los héroes
@app.route('/heroes', methods=['GET'])
def obtener_heroes():
    conexion = sqlite3.connect('marvel.db')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM heroes")
    heroes = cursor.fetchall()

    conexion.close()

    resultado = []

    for heroe in heroes:
        resultado.append({
            "id": heroe[0],
            "nombre": heroe[1],
            "poder": heroe[2]
        })

    return jsonify(resultado)


# UPDATE - Actualizar héroe
@app.route('/heroes/<int:id>', methods=['PUT'])
def actualizar_heroe(id):
    datos = request.get_json()

    conexion = sqlite3.connect('marvel.db')
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE heroes SET nombre = ?, poder = ? WHERE id = ?",
        (datos['nombre'], datos['poder'], id)
    )

    conexion.commit()

    if cursor.rowcount == 0:
        conexion.close()
        return jsonify({"mensaje": "Héroe no encontrado"}), 404

    conexion.close()

    return jsonify({
        "mensaje": "Héroe actualizado correctamente"
    })


# DELETE - Eliminar héroe
@app.route('/heroes/<int:id>', methods=['DELETE'])
def eliminar_heroe(id):
    conexion = sqlite3.connect('marvel.db')
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM heroes WHERE id = ?",
        (id,)
    )

    conexion.commit()

    if cursor.rowcount == 0:
        conexion.close()
        return jsonify({"mensaje": "Héroe no encontrado"}), 404

    conexion.close()

    return jsonify({
        "mensaje": "Héroe eliminado correctamente"
    })


if __name__ == '__main__':
    inicializar_db()
    app.run(debug=True)