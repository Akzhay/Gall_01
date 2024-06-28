
import sqlite3
import logging
from logger_config import log_message

def connect_to_database(db_name):
    """
    Connects to the specified SQLite database.
    :param db_name: The name of the database.
    :return: Connection object or None.
    """
    try:
        conn = sqlite3.connect(db_name)
        log_message(f"Successfully connected to database: {db_name}")
        return conn
    except sqlite3.Error as e:
        log_message(f"Error connecting to database: {e}", level=logging.ERROR)
        return None

def create_table(conn):
    """
    Creates a table in the SQLite database.
    :param conn: The Connection object.
    """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CICLINT 
            (
                CICLINT_CLIENT_NUM TEXT PRIMARY KEY,                
                CICLINT_TSTAMP TEXT,
                CICLINT_STATUS_CODE TEXT,
                CICLINT_STATUS_DATE TEXT,
                CICLINT_ORG_NAME1 TEXT,
                CICLINT_ORG_NAME2 TEXT,
                CICLINT_ADDRESS1 TEXT,
                CICLINT_ADDRESS2 TEXT,
                CICLINT_ADDRESS3 TEXT,
                CICLINT_CITY TEXT,
                CICLINT_STATE TEXT,
                CICLINT_CNTRY_CODE TEXT,
                CICLINT_POSTAL_CODE TEXT,
                CICLINT_NAME_SORT TEXT,
                CICLINT_TAX_ID_TYPE TEXT,
                CICLINT_TAX_ID TEXT,
                CICLINT_PHONE TEXT,
                CICLINT_TELEX TEXT,
                CICLINT_FAX TEXT
                
            )
    ''')
        conn.commit()
        log_message("Table 'users' created successfully.")
    except sqlite3.Error as e:
        log_message(f"Error creating table: {e}", level=logging.ERROR)

