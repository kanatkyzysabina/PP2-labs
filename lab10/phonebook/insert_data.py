import psycopg2
import csv
from config import load_config

conn = psycopg2.connect(**load_config())
cur = conn.cursor()

mode = input("Insert mode (1 - console, 2 - csv): ")

if mode == '1':
    first = input("Name: ")
    last = input("Surname: ")
    phone = input("Phone number: ")

    cur.execute("INSERT INTO person (first_name, last_name) VALUES (%s, %s) RETURNING id", (first, last))
    person_id = cur.fetchone()[0]
    cur.execute("INSERT INTO phonebook (person_id, phone_number) VALUES (%s, %s)", (person_id, phone))

elif mode == '2':
    file = input("CSV filename: ")
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            first, last, phone = row
            cur.execute("INSERT INTO person (first_name, last_name) VALUES (%s, %s) RETURNING id", (first, last))
            person_id = cur.fetchone()[0]
            cur.execute("INSERT INTO phonebook (person_id, phone_number) VALUES (%s, %s)", (person_id, phone))

conn.commit()
print("Done!")
conn.close()
