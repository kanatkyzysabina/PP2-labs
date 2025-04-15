import psycopg2
from connection import connect
from config import load_config

config = load_config()
conn = connect(config)
con = conn.cursor()
conn.autocommit = True

id_old = input("Enter the current ID (from person table): ")

sql_person_check = """SELECT * FROM person WHERE id = %s"""
con.execute(sql_person_check, (id_old,))
person_info = con.fetchall()

if len(person_info) > 0:
    new_first = input("Enter the new first name: ")
    new_last = input("Enter the new last name: ")
    new_phone = input("Enter the new phone number: ")

    sql_update_person = """UPDATE person SET first_name = %s, last_name = %s WHERE id = %s"""
    con.execute(sql_update_person, (new_first, new_last, id_old))

    sql_update_phonebook = """UPDATE phonebook SET phone_number = %s WHERE person_id = %s"""
    con.execute(sql_update_phonebook, (new_phone, id_old))

    print("successfully updated!!")
else:
    print("no such information found in the \"person\" table.")

conn.commit()
conn.close()
