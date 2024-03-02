import json
import os
import psycopg2

from psycopg2 import OperationalError

def create_database(cursor, database_name):
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{database_name}'")
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(f"CREATE DATABASE {database_name};")
        print(f"Database '{database_name}' created successfully in PostgreSQL!")
    else:
        print(f"Database '{database_name}' already exists in PostgreSQL!")

def table_exists(cursor, table_name):
    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (table_name,))
    exists = cursor.fetchone()[0]
    if exists:
        print(f"The table '{table_name}' already exists in the database")
    else:
        print(f"The table '{table_name}' has been created successfully!")
        
    return exists

with open('config.json') as f:
    config = json.load(f)

try:
    connection = psycopg2.connect(**config["no_db"])
    connection.autocommit = True  # Establecer autocommit a True
    print("Successful connection to postgresql!")

    cursor = connection.cursor()
    create_database(cursor, 'candidates')

    connection = psycopg2.connect(**config["with_db"])
    print("Successful connection to the 'candidates' database!")

    cursor = connection.cursor()

    table_name = "candidates"

    if not table_exists(cursor, table_name):
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

        cursor.execute(create_table_query)
        connection.commit()


    with open('candidates.csv', 'r') as f:
        next(f)
        cursor.copy_from(f, 'candidates', sep=';', null='', columns=("First Name", "Last Name", "Email", "Application Date", "Country", "YOE", "Seniority", "Technology", "Code Challenge Score", "Technical Interview Score"))
        connection.commit()
        
        table_name = "candidates_hired"
        
        if not table_exists(cursor, table_name):
            

                create_new_table_query = '''CREATE TABLE candidates_hired AS
                SELECT *,
                    CASE WHEN "Code Challenge Score" >= 7 AND "Technical Interview Score" >= 7 THEN TRUE ELSE FALSE END AS hired
                FROM candidates;'''

                cursor.execute(create_new_table_query)
                connection.commit()

    print("Data successfully inserted in the table")

except OperationalError as e:
    print(f"An error ocurred: {e}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Closed connection")
