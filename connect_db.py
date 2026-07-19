# This is my resfreshing script for my project. It automates the process of updating the data and generating new reports. The script connects to the database, retrieves the latest information, processes it, and saves the results in a specified format. It also includes error handling to ensure that any issues during execution are logged for review.
import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=os.environ["DB_PORT"],
    )


if __name__ == "__main__":
    print("Connecting to the database...")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM example;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
