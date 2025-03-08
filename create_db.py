import mysql.connector

DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'foo',
    'password': 'foo',
    'database': 'routes_db'
}

def create_table():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS routes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            origin VARCHAR(255) NOT NULL,
            destination VARCHAR(255) NOT NULL,
            cost DECIMAL(10,2),
            time INT
        )
    """)
    conn.commit()
    conn.close()

create_table()
