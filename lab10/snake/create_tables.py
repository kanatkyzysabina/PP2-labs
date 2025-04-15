import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    database='Snake',
    user='postgres',
    password='210706',
    host='localhost',
    port='5432'
)
conn.autocommit = True
cursor = conn.cursor()

# users table
create_users = '''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);
'''

# user_score table
create_user_score = '''
CREATE TABLE IF NOT EXISTS user_score (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    score INT,
    level INT
);
'''

# Execute queries
cursor.execute(create_users)
cursor.execute(create_user_score)

print("Tables have been created successfully!")

# Close the connection
cursor.close()
conn.close()
