# PROG8850Template

Environment with MySQL, Python and Selenium tests

This repository contains a small Flask application backed by a MySQL
database.  A Selenium based test is included in `tests/test_login.py`.


## Installation

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the MySQL service and configure the default user:

   ```bash
   sudo service mysql start
   sudo mysql
   ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
   FLUSH PRIVILEGES;
   EXIT;
   ```

3. Initialize the database schema (creates the `testapp` database and a
   `users` table):

   ```bash
   python init_db.py
   ```

## Running the application

Launch the Flask application on the default port (5000):

```bash
python app.py
```

Visit `http://localhost:5000/` in your browser.  Submitting the form will
store the username and password in the MySQL database.

## Running the Selenium tests

The Selenium test automatically starts the Flask server on a random port
and verifies that submitting the login form inserts a record into the
database.

Then simply run:

```bash
pytest -q
```

The test script `tests/test_login.py` will take care of launching and
terminating the application.

## Screenshots

![ss1](screenshots/Screenshot(875).png)
![ss2](screenshots/Screenshot(876).png)
![ss3](screenshots/Screenshot(877).png)
![ss4](screenshots/Screenshot(878).png)