import os
import mysql.connector


def init_db():
    """Create the database and users table using env vars if available."""
    conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', '127.0.0.1'),        
        port=int(os.getenv('MYSQL_PORT', '3306')),        
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'root')
    )
    database = os.getenv('MYSQL_DATABASE', 'testapp')
    cursor = conn.cursor()
    cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database}')
    cursor.execute(f'USE {database}')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    init_db()