import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS alx_book_store"
        )
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

def connect_to_mysql():
    try:
        cnx = mysql.connector.connect(
            user='your_username',    # replace with your MySQL username
            password='your_password' # replace with your MySQL password
        )
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        else:
            print(err)
        return None

def main():
    cnx = connect_to_mysql()
    if cnx:
        cursor = cnx.cursor()
        create_database(cursor)
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    main()
