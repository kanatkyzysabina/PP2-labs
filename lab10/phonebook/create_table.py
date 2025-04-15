import psycopg2
from config import load_config

def create_tables():
    """Create the phonebook table in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS person (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            person_id INTEGER REFERENCES person(id),
            phone_number VARCHAR(20)
        )
        """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
            print("Table created successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
