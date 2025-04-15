import psycopg2
import csv

conn = psycopg2.connect(
    host = 'localhost',
    database = 'PhoneBook',
    user =  'postgres',
    password = '210706'
)

cursor = conn.cursor()

# == creating tables == 

cursor.execute('''
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        phone_number VARCHAR(30)
    )
''')

conn.commit()


# == inserting data ==

    # -csv file method-
def csv_reader(file):
    try:
        with open(file) as f:
            reader = csv.reader(f)
            for row in reader:
                first, last, phone = row
                cursor.execute("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first, last, phone))
            conn.commit()
        print("insertion through csv reader is DONE!")
    except (psycopg2.DatabaseError, Exception) as error:
            print(error)


    # -console method-
def console_insertion():
    print("To insert from console, write next data:")
    first = input("Name: ")
    last = input("Surname: ")
    phone = input("Phone number: ")
    try:
        cursor.execute("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first, last, phone))
        conn.commit()
        print("Insertion through console is DONE!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


# == updatind data == 

def update_data():
    person_id = int(input("Id of a person you want to change: "))
    print("Choose what to change: \n1 - Name \n2 - Phone Number")
    choice = int(input("Print your choice(1 or 2): "))

    if choice == 1:
        new_name = input("Print new name: ")
        cursor.execute('''UPDATE phonebook SET first_name = %s WHERE id = %s''', 
                       (new_name, person_id))
        conn.commit()
        print("Data updated!")
    
    elif choice == 2:
        new_phone_num = input("Print new phone number: ")
        cursor.execute('''UPDATE phonebook SET phone_number = %s WHERE id = %s''', 
                       (new_phone_num, person_id))
        conn.commit()
        print("Data updated!")
    else:
        print("Invalid choice!!")

# == query data ==

def query_data():
    print("Choose filter for your dara: ")
    print("1 - Ascending order by 'First Name' ")
    print("2 - Descending order by 'First Name' ")
    print("3 - Select all people with name starting with 'A' ")
    print("4 - quit")
    conn.autocommit = True
    choice = int(input("Print your choice(1-4): "))
    if choice == 1:
        cursor.execute('''SELECT * FROM phonebook ORDER BY first_name ASC;''')
        filtered_data = cursor.fetchall()
        print("All data ordered by ASC first name: ")
        print(filtered_data)
    elif choice == 2:
        cursor.execute('''SELECT * FROM phonebook ORDER BY first_name DESC; ''')
        filtered_data = cursor.fetchall()
        print("All data ordered by DESC first name: ")
        print(filtered_data)
    elif choice == 3:
        cursor.execute("SELECT * FROM phonebook WHERE first_name LIKE 'A%';")
        filtered_data = cursor.fetchall()
        print("All data ordered by DESC first name: ")
        print(filtered_data)
    elif choice == 4:
        print("No filter applied. You quit.")

# == delete data == 

def delete_data():
    print("How do you want to delete data: ")
    choice = int(input("1 - By First Name \n2 - By Phone Number \nYour choice(1 or 2): " ))
    if choice == 1:
        name = input("Print first name you want to DELETE: ")
        cursor.execute('''DELETE FROM phonebook WHERE first_name = %s;''', (name, ))
        conn.commit()
        print(f"Data with name {name} was deleted successfully!")
    elif choice == 2:
        number = input("Print Phone Number you want to DELETE: ")    
        cursor.execute('''DELETE FROM phonebook WHERE phone_number = %s;''', (number, ))
        conn.commit()
        print(f"Data with phone number {number} was deleted successfully!")
        
# == choosing == 

print("Choose what you want to do with the table: ")
print("1 - INSERT DATA \n2 - UPDATE DATA \n3 - QUERY DATA \n4 - DELETE DATA")
choice = int(input("Print your choice(1-4): "))
if choice == 1:
    print("Choose method to insert data \n1 - CSV file \n2 - Console")
    choice_insert = int(input("Print your choice(1 or 2): "))
    if choice_insert == 1:
        file_name = input("Print your CSV file name(filename.csv): ")
        csv_reader(file_name)
    elif choice_insert == 2:
        console_insertion()
elif choice == 2:
    update_data()
elif choice == 3:
    query_data()
elif choice == 4:
    delete_data()
else:
    print("Invalid Choice.")

cursor.close()
conn.close()




        


    
    







                