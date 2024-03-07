import psycopg2
import os 
from psycopg2 import sql

def get_db_connection():
    # Database connection parameters
    db_name = os.environ.get("DB_NAME")
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASS")
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_pass,
        host=db_host,
        port=db_port
    )
    return conn

def create_db():
    # SQL statement to create a new database
    db_name = os.environ.get("DB_NAME")
    create_db_query = f"CREATE DATABASE {db_name};"
    db_conn = get_db_connection()
    # Executing the SQL statement to create the new database
    cursor = db_conn.cursor()
    cursor.execute(sql.SQL(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'"))
    exists = cursor.fetchone()

    # If the database does not exist, create it
    if not exists:
        try:
            cursor.execute(create_db_query)
            db_conn.commit()
            print("Database created successfully.")
        except psycopg2.Error as e:
            print("Error creating database:", e)

        finally:
            cursor.close()
            db_conn.close()

def create_table():
    conn = get_db_connection()
    # SQL statements to create tables
    create_tasks_query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            message VARCHAR(255),
            done Boolean
        );
    """
    cursor = conn.cursor()
    cursor.execute(create_tasks_query)
    conn.commit()
    print("Tables created successfully.")

def insert_message_into_db(message):
    # Creating a cursor object using the connection
    conn = get_db_connection()
    cursor = conn.cursor()
    # Inserting records into the tables
    try:
        # SQL statements to insert records
        insert_query = f"INSERT INTO tasks (message, done) VALUES ('{message}', False);"
        cursor.execute(insert_query)
        conn.commit()
        print("Records inserted successfully.")

    except psycopg2.Error as e:
        print("Error inserting records:", e)

    finally:
        cursor.close()
        conn.close()

def update_record_status(message_id):
    # Creating a cursor object using the connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Inserting records into the tables
    try:
        # SQL statements to update record
        update_query = f"UPDATE tasks done VALUES True WHERE id = {message_id};"
        cursor.execute(update_query)
        conn.commit()
        print("Records inserted successfully.")
    except psycopg2.Error as e:
        print("Error inserting records:", e)

    finally:
        cursor.close()
        conn.close()

def get_record(message_id):
    conn = get_db_connection()
    # Creating a cursor object using the connection
    cursor = conn.cursor()

    # Inserting records into the tables
    try:
        # SQL statements to update record
        select_query = f"SELECT message tasks done VALUES True WHERE id = {message_id};"
        cursor.execute(select_query)
        print("Records inserted successfully.")
    except psycopg2.Error as e:
        print("Error inserting records:", e)

    finally:
        cursor.close()
        conn.close()
