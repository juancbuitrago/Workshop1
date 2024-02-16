import psycopg2
from psycopg2 import OperationalError

def table_exists(cursor, table_name):
    """
    Verifica si la tabla ya existe en la base de datos.
    """
    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (table_name,))
    return cursor.fetchone()[0]

try:
    # Conexión a la base de datos PostgreSQL
    connection = psycopg2.connect(
        dbname="candidates",
        user="postgres",
        password="",
        host="localhost",
        port="5432",
        client_encoding='utf-8'
    )

    # Creación de un cursor para ejecutar comandos SQL
    cursor = connection.cursor()

    table_name = "candidates"

    # Verificar si la tabla ya existe
    if not table_exists(cursor, table_name):
        # Comando SQL para crear una tabla
        create_table_query =''' CREATE TABLE candidates (
            "First Name" VARCHAR(255),
            "Last Name" VARCHAR(255),
            "Email" VARCHAR(255),
            "Application Date" DATE,
            "Country" VARCHAR(255),
            "YOE" INTEGER,
            "Seniority" VARCHAR(255),
            "Technology" VARCHAR(255),
            "Code Challenge Score" INTEGER,
            "Technical Interview Score" INTEGER
        );'''

        # Ejecución del comando SQL
        cursor.execute(create_table_query)
        connection.commit()
        print("Tabla creada exitosamente en PostgreSQL")
    else:
        print("La tabla ya existe en la base de datos")

    # Cargar datos desde el archivo CSV
    with open('candidates.csv', 'r') as f:
        next(f)  # Salta la primera fila (cabecera)
        cursor.copy_from(f, 'candidates', sep=';', null='', columns=("First Name", "Last Name", "Email", "Application Date", "Country", "YOE", "Seniority", "Technology", "Code Challenge Score", "Technical Interview Score"))
        connection.commit()  # Confirma la transacción

    print("Datos insertados exitosamente en la tabla")

except OperationalError as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Cierre de la conexión y el cursor
    if connection:
        cursor.close()
        connection.close()
        print("Conexión cerrada")
