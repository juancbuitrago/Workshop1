
import psycopg2
import json

def load_config(file_path):
    with open(file_path) as f:
        return json.load(f)

def connect_to_database(config):
    try:
        connection = psycopg2.connect(**config)
        connection.autocommit = True
        print("Successful connection to PostgreSQL!")
        return connection
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")

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


