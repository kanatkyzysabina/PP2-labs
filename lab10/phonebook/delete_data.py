import psycopg2
from config import load_config
from connection import connect

def delete_data():
    config = load_config()
    conn = connect(config)
    cursor = conn.cursor()
    conn.autocommit = True

    print("Delete by:\n1)Name\n2)Phone number")
    choice = input("Choose 1 or 2: ")

    if choice == "1":
        first = input("Enter first name: ")
        last = input("Enter last name: ")

        cursor.execute("SELECT id FROM person WHERE first_name = %s AND last_name = %s", (first, last))
        person = cursor.fetchone()

        if person:
            person_id = person[0]
            cursor.execute("DELETE FROM phonebook WHERE person_id = %s", (person_id,))
            cursor.execute("DELETE FROM person WHERE id = %s", (person_id,))
            print("deleted successfully!")
        else:
            print("no such person found")

    elif choice == "2":
        phone = input("Enter phone number: ")

        cursor.execute("SELECT person_id FROM phonebook WHERE phone_number = %s", (phone,))
        result = cursor.fetchone()

        if result:
            person_id = result[0]
            cursor.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
            cursor.execute("DELETE FROM person WHERE id = %s", (person_id,))
            print("deleted successfully!")
        else:
            print("no such phone number found")
    else:
        print("invalid option.")

    cursor.close()
    conn.close()

if __name__ == '__main__':
    delete_data()
