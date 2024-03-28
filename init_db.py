import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


conn = psycopg2.connect (
    host="localhost",
    database="improvement_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'],
    port="5432"
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table

# Insert data into the table
cur.execute('INSERT INTO users (name, password, email)'
            'VALUES (%s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             'cnsjnc@123',
             )
            )

conn.commit()

cur.close()
conn.close()