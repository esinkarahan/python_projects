import sqlite3
import hashlib
#from getpass import getpass
import json
import re

def ask_password():
    #this does not work on pycharm
#    password = getpass('Enter your password ')
    invalidpw = True
    while True:
        while invalidpw:
            pw = input('Enter your password: ')
            invalidpw = is_password_valid(pw)
        pw2 = input('Confirm your password: ')
        if not pw == pw2:
            print('Your password is not confirmed. Try again.')
            invalidpw = True
        else:
            break
#    pw = input('Enter your password: ')
#    while is_password_valid(pw):
#        pw = input('Enter your password: ')
    print('Your username is added in the system!')
    password_hash = hashlib.sha256(pw.encode()).hexdigest()
    return password_hash

def is_password_valid(pw):
    # Require a minimum length(8), at least one number and letter,
    # and at least one punctuation mark.
    if len(pw) < 8 | (re.search('[^a-zA-Z0-9_]',pw) == None) | \
            (re.search('[0-9]',pw) == None) | \
            (re.search('[a-zA-Z]',pw) == None):
        print('Please select a password with minimum 8 characters, '
              'at least one number and letter, at least one punctuation mark')
        return True
    else:
        return False

def confirm_password(pw):
    pwc = input('Confirm your password: ')
    if not hashlib.sha256(pwc.encode()).hexdigest() == pw:
        print('Password is not confirmed!')
        return 0
    else:
        return 1

def sql_add_user_fun(conn, cur, username, password_hash):
    sql_add_user = """ INSERT INTO users (username,password_hash)
                        VALUES(?,?)"""
    cur.execute(sql_add_user, (username, password_hash))


def sql_check_user_fun(conn, cur, username):
    # check whether username is already taken
    sql_check_user = """ SELECT username
                          FROM users
                          WHERE username = ?"""
    cur.execute(sql_check_user, (username, ))
    return cur.fetchone() is not None


def add_user():
    with open("databasefile.json", 'r') as f:
          database = json.load(f)
    conn = sqlite3.connect(database['filename'])
    cur = conn.cursor()
    while True:
        username = input('Please enter username: ')
        repeat = sql_check_user_fun(conn, cur, username)
        if repeat:
            print('This username is used, select another one: ')
        else:
            break
    password_hash = ask_password()
    # add user name and password to the users table
    sql_add_user_fun(conn, cur, username, password_hash)
    conn.commit()
    conn.close()

#if __name__ == '__main__':
#    with open("databasefile.json", 'r') as f:
#        database = json.load(f)
#    add_user(database['filename'])

