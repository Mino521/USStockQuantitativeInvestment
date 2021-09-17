import mysql.connector
from mysql.connector import errorcode
import logging


def create_database(cursor, DB_NAME):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def create_table(cursor, DB_NAME, TABLES):
    cursor.execute("USE {}".format(DB_NAME))
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")


def write_to_database(conn, cursor, sql, values, DB_NAME):
    cursor.execute("USE {}".format(DB_NAME))
    cursor.execute(sql, values)
    conn.commit()
