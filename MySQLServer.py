#!/usr/bin/env python3
"""
Script to create a MySQL database named 'alx_book_store'.
If it exists, it doesn't fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update host/user/password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # <-- Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
