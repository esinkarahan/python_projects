"""
This python program asks whether a user wants to register or login.
If login option is selected, it checks whether password associated to a username is correct.
If register option is selected, it registers new username into the database.

This project is based on Robert Heaton's userlogin projects
https://robertheaton.com/2019/08/12/programming-projects-for-advanced-beginners-user-logins/
Written by Esin Karahan
October 2020
"""
from add_user import add_user
from is_valid_credentials import is_valid_credentials
num_invalid = 0
while True:
    option = input('Do you want to register (r) or login (l) ? : ').strip().lower()
    if option == 'r':
        add_user()
        break
    elif option == 'l':
        while True:
            name = input('Please enter your username: ')
            if not name == '':
                pw = input('Please enter your password: ')
                if is_valid_credentials(name, pw):  # matched credentials
                    print('You are good to proceed.')
                    break
                else:
                    num_invalid += 1
                    print('Your login info is wrong, try again.')
            if num_invalid >2:
                print('Your username is locked')
                break
        break
    else:
        print('Please type a valid response.')

#extensions:
# add a password-reset function to your database-driven program.
