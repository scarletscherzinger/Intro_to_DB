import mysql.connector
from mysql.connector import Error

def main():
    try:
        # Connect to MySQL server (replace password if you set one)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='G!bson7Sc@rletN59'  # <-- replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # EXACT database name required by the assignment:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Print error message when failing to connect or execute
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Ensure we close cursor and connection if they exist/open
        if 'connection' in locals() and connection.is_connected():
            try:
                cursor.close()
            except Exception:
                pass
            connection.close()

if __name__ == "__main__":
    main()
