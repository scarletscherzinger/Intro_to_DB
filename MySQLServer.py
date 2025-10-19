import mysql.connector

def main():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="G!bson7Sc@rletN59"  # replace with your real MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # EXACT database name required by the assignment:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            try:
                cursor.close()
            except Exception:
                pass
            connection.close()

if __name__ == "__main__":
    main()
