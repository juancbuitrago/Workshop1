import psycopg2
import pandas as pd
from psycopg2 import OperationalError
from config import load_config, connect_to_database, create_database, table_exists

def main():
    config = load_config('../data/config.json')

    try:
        connection = connect_to_database(config["no_db"])

        cursor = connection.cursor()
        create_database(cursor, 'candidates')

        connection = connect_to_database(config["with_db"])
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

        data = pd.read_csv('../data/candidates.csv', sep=';')

        with open('../data/candidates.csv', 'r') as f:
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
        print(f"An error occurred: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Closed connection")

if __name__ == "__main__":
    main()
