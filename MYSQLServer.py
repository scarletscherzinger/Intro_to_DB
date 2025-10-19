import mysql.connector
from mysql.connector import Error

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='G!bson7Sc@rletN59'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
