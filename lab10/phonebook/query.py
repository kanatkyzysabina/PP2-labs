import psycopg2

from config import load_config

conn = psycopg2.connect(**load_config())
cursor = conn.cursor()
conn.autocommit = True

# select all info from "person" table
sql = f"SELECT * FROM person;"
cursor.execute(sql)
info = cursor.fetchall()
print("all data from person table:")
print(info)

# select where the first name starts with 'A'
sql = f"SELECT * FROM person WHERE first_name LIKE 'A%';"
cursor.execute(sql)
info = cursor.fetchall()
print("\nData with names starting with 'A':")
print(info)

# select all and order by first name in ascending order
sql = f"SELECT * FROM person ORDER BY first_name ASC;"
cursor.execute(sql)
info = cursor.fetchall()
print("\nData ordered by first name acs:")
print(info)

# select all and order by first name in descending order
sql = f"SELECT * FROM person ORDER BY first_name DESC;"
cursor.execute(sql)
info = cursor.fetchall()
print("\nData ordered by first name desc:")
print(info)

cursor.close()
conn.close()
