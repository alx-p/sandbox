import os
import time
import random
import psycopg2
from datetime import datetime

def generate_data():
    return {
        "id": random.randint(1, 1000),
        "value": random.random() * 100,
        "timestamp": datetime.now().isoformat()
    }

def create_table():
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"]
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_data (
            id INTEGER,
            value FLOAT,
            timestamp TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_data(data):
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"]
    )
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO test_data (id, value, timestamp)
        VALUES (%s, %s, %s)
    """, (data["id"], data["value"], data["timestamp"]))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    interval = int(os.environ.get("INTERVAL", 10))
    create_table()
    while True:
        data = generate_data()
        insert_data(data)
        print(f"Inserted data: {data}")
        time.sleep(interval)