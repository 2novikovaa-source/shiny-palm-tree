# This is my resfreshing script for my project. It automates the process of updating the data and generating new reports. The script connects to the database, retrieves the latest information, processes it, and saves the results in a specified format. It also includes error handling to ensure that any issues during execution are logged for review.
import psycopg2

print( "Connecting to the database...")
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="mysecretpassword",
    port=5431
)

cursor = conn.cursor();
cursor.execute("SELECT * FROM example;")
rows = cursor.fetchall()
for row in rows:
    print(row)
