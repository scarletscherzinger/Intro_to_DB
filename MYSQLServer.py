import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (update password if needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='G!bson7Sc@rletN59'  # replace with your actual MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
