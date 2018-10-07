import sqlite3
from sqlite3 import Error
 
 
def db_connect(db_file):

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    finally:
        # conn.close()
        pass

    return None


def create_table(conn, create_table_sql):
    # creates new table in the db called 'TestTable' with fields 'id INT PRIMARY KEY' and 'excerpt VARCHAR(255)'
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_into_db(conn, string):
    # receives a string as param and inserts a new row in 'TestTable' and saves the param under the field 'excerpt'
    sql = "INSERT INTO TestTable(excerpt) VALUES(?)"
    try:
        c = conn.cursor()
        c.execute(sql, string)
    except Error as e:
        print(e)
