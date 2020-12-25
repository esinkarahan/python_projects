import os
import sqlite3
import json


def connect_db(dbname):
    # create a database ppab6.db
    conn = sqlite3.connect(dbname)
    return conn

def sql_count_rows_fun(conn):
    sql_count_rows = """SELECT username, COUNT (*) 
                        FROM users"""
    cur = conn.cursor()
    nrow = cur.execute(sql_count_rows).fetchall()[0][1]
    return nrow

def create_table(conn):
    # create table
    sql_create_table = """ CREATE TABLE users(
                            username VARCHAR,
                            password_hash VARCHAR
                            );"""
    cur = conn.cursor()
    cur.execute(sql_create_table)


def setup_db(dbname):
    # check whether db exist
    conn = connect_db(dbname)
    if os.path.isfile(dbname):
        nrow = sql_count_rows_fun(conn)
        print(dbname, " already exists with ", str(nrow), " rows")
        conn.close()
        res = input("Do you want to delete and recreate it? y/n ")
        if res.lower() == 'y':
            os.remove(dbname)
            conn = connect_db(dbname)
            create_table(conn)
        else:
            exit(0)
    else:
        print('Creating database')
        create_table(conn)
    conn.close()


if __name__ == '__main__':
    with open("databasefile.json", 'r') as f:
        database = json.load(f)
    setup_db(database['filename'])