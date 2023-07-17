import os
import sqlite3

import Models.usuarios

conexion = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ofuscamiento.db")


def bulk_create( table_name, records):
    # Establece la conexión a la base de datos SQLite
    conn = sqlite3.connect(conexion)
    cursor = conn.cursor()

    # Obtiene los nombres de las columnas de la tabla
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]

    # Construye la consulta SQL de inserción
    query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(columns))})"

    # Inserta los registros en lotes utilizando una transacción
    try:
        cursor.execute("BEGIN TRANSACTION")
        for record in records:
            values = [getattr(record, column.lower(), None) for column in columns]
            cursor.execute(query, values)
        conn.commit()
        print("Registros insertados exitosamente.")
    except Exception as e:
        conn.rollback()
        print("Error al insertar los registros:", str(e))
    finally:
        # Cierra la conexión a la base de datos
        cursor.close()
        conn.close()


def read_table(table_name):
    conn = sqlite3.connect(conexion)
    cursor = conn.cursor()
    rows = 0
    # Construye la consulta SQL de inserción
    query = f"select * from {table_name};"

    try:
        cursor.execute(query)
        data = cursor.fetchall()
        if table_name=="usuarios":
            rows = [Models.usuarios.Usuarios(*t) for t in data]
        if table_name=="clientes":
            rows = [Models.clientes.Clientes(*t) for t in data]
        if table_name=="empleados":
            rows = [Models.empleados.Empleados(*t) for t in data]


    except Exception as e:
        conn.rollback()
        print("Error al insertar los registros:", str(e))
    finally:
        cursor.close()
        conn.close()
    return rows

