This python program asks whether a user wants to register or login.

* If login option is selected, it checks whether password associated to a username is correct. If not, it asks again. If there are more than two
unsuccessfull attempts, username is locked.

* If register option is selected, it checks whether username is already registered, if not then it registers new username into the database.
For registration, password should have min 8 characters and contains at least one number, one letter and punctuation mark.

Run program by
`python user_login.py`

To setup a new database run
`python setup_db.py`

name of the new database file should be written in `databasefile.json`

