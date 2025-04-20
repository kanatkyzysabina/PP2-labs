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
        print("All data with names starting with A: ")
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


# == functions ==
def create_function_or_procedure(command):
    try:
        cursor.execute(command)
        conn.commit()
        print("Function was created successfully")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

phone_num_with09_function = """CREATE OR REPLACE FUNCTION phone_num_with09()
                    RETURNS TABLE (id INTEGER, first_name VARCHAR(255),
                    last_name VARCHAR(255), phone_number VARCHAR(30)) 
                    AS
                    $$
                    BEGIN
                        RETURN QUERY
                        SELECT * FROM phonebook WHERE phonebook.phone_number LIKE '%09';
                    END;
                    $$
                    LANGUAGE plpgsql;"""



pagination_function = """CREATE OR REPLACE FUNCTION pagination_func(page_limit INT, page_offset INT)
                    RETURNS TABLE (id INTEGER, first_name VARCHAR(255),
                    last_name VARCHAR(255), phone_number VARCHAR(30))
                    AS
                    $$
                    BEGIN
                        RETURN QUERY
                        SELECT * FROM phonebook ORDER BY id
                        LIMIT page_limit OFFSET page_offset;
                    END;
                    $$
                    LANGUAGE plpgsql;"""


def phone_num_function():
    try:
        cursor.execute("SELECT * FROM phone_num_with09()")
        conn.commit()
        print("Results: ")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def pag_function():
    limit = int(input("Enter how many results you want to see(LIMIT): "))
    offset = int(input("Enter how many you want to skip(OFFSET): "))
    try:
        cursor.execute("SELECT * FROM pagination_func(%s, %s)", (limit, offset))
        conn.commit()
        print("Results: ")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# == procedures == 

insertion_procedure = """CREATE OR REPLACE PROCEDURE insert_user(
                        f_name VARCHAR,
                        l_name VARCHAR,
                        p_number VARCHAR
                        )
                        LANGUAGE plpgsql
                        AS $$
                        BEGIN
                            IF EXISTS(
                            SELECT 1 FROM phonebook WHERE first_name = f_name AND last_name = l_name) THEN
                                UPDATE phonebook SET phone_number = p_number WHERE first_name = f_name AND last_name = l_name;
                            ELSE
                                INSERT INTO phonebook (first_name,last_name, phone_number) VALUES (f_name,l_name,p_number);
                            END IF;
                        END;
                        $$;
                        """
def call_insertion_procedure():
    name = input("Enter name you want to insert: ")
    surname = input("Enter surname you want to insert: ")
    phone = input("Enter phone number you want to insert: ")
    try:
        cursor.execute("CALL insert_user(%s, %s, %s)", (name, surname, phone))
        conn.commit()
        print("Procedure was called successfully")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

#create_function_or_procedure(phone_num_with09_function)
#create_function_or_procedure(pagination_function)


# == choosing == 


print("Choose what you want to do with the table: ")
print("1 - INSERT DATA \n2 - UPDATE DATA \n3 - QUERY DATA \n4 - DELETE DATA \n5 - CALL FUNCTION")
choice = int(input("Print your choice(1-5): "))
if choice == 1:
    print("Choose method to insert data \n1 - CSV file \n2 - Console \n3 - Procedure Insertion")
    choice_insert = int(input("Print your choice(1 or 2): "))
    if choice_insert == 1:
        file_name = input("Print your CSV file name(filename.csv): ")
        csv_reader(file_name)
    elif choice_insert == 2:
        console_insertion()
    elif choice_insert == 3:
        create_function_or_procedure(insertion_procedure)
        call_insertion_procedure()

elif choice == 2:
    update_data()
elif choice == 3:
    query_data()
elif choice == 4:
    delete_data()
elif choice == 5:
    print("Choose what function to call: \n1 - Function that outputs data with phone number ending with '09' \n2 - Pagination Function")
    func_choice = int(input("Your choice(1 or 2): "))
    if func_choice == 1:
        phone_num_function()
    elif func_choice == 2:
        pag_function()
    else:
        print("Invalid Choice.")
else:
    print("Invalid Choice.")

cursor.close()
conn.close()




        


    
    







                