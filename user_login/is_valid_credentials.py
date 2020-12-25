import hashlib
import json
import sqlite3


def json_open_database():
    with open("credentials.json", 'r') as f:
        database = json.load(f)
    return database


def sql_open_database():
    # name of the database file is stored in this file
    with open("databasefile.json", 'r') as f:
        database = json.load(f)
    conn = sqlite3.connect(database['filename'])
    cur = conn.cursor()
    return conn, cur


def sql_check_pw_fun(conn, cur, username, password_hash):
    # check whether username is already taken
    sql_check_user = """ SELECT *
                          FROM users
                          WHERE username = ? AND password_hash = ? """
    cur.execute(sql_check_user, (username, password_hash))
    return cur.fetchone() is not None


def is_valid_credentials(name,pw):
    ##check whether password matches with the database
    pw_hash = hashlib.sha256(pw.encode()).hexdigest()
    ##load config file: sql
    conn, cur = sql_open_database()
    return sql_check_pw_fun(conn, cur, name, pw_hash)


