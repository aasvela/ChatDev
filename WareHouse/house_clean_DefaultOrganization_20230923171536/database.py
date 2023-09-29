'''
This file handles the database operations for the web application.
'''
import sqlite3
from user import UserModel
class Database:
    def __init__(self):
        self.conn = sqlite3.connect("divorce_app.db")
        self.cursor = self.conn.cursor()
        self.create_tables()
    def create_tables(self):
        # Create the necessary tables in the database
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        self.conn.commit()
    def close(self):
        self.conn.close()
    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = self.cursor.fetchone()
        if user is not None:
            return UserModel(user[0], user[1])
        else:
            return None
    def save_user(self, user):
        self.cursor.execute("INSERT INTO users VALUES (?, ?)", (user.username, user.password))
        self.conn.commit()