import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Raghav@2003"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS house_db")

cursor.execute("USE house_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(
    id INT AUTO_INCREMENT PRIMARY KEY,
    area INT,
    bedrooms INT,
    bathrooms INT,
    floors INT,
    age INT,
    location_score INT,
    predicted_price DOUBLE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

print("Database Ready Successfully")