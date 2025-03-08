import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

DB_CONFIG = {
    'host': '127.0.0.1',
    'user': 'foo',
    'password': 'foo',  # Replace with actual password
    'database': 'routes_db'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("✅ Connected to MySQL")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Database connection error: {err}")
        return None

@app.route("/routes", methods=["POST"])
def get_routes_between():
    data = request.json
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    
    if not latitude or not longitude:
        return jsonify({"error": "latitude and longitude are required"}), 400
    
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    try:
        query = """
            SELECT * FROM routes 
            WHERE latitude = %s AND longitude = %s
        """
        cursor.execute(query, (latitude, longitude))
        routes = cursor.fetchall()

        return jsonify(routes)
    except mysql.connector.Error as err:
        print(f"❌ Database query error: {err}")
        return jsonify({"error": "Query failed"}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(debug=True)