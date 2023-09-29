'''
This file handles user-related operations for the web application.
'''
from database import Database
class UserLogic:
    def __init__(self):
        self.db = Database()
    def login(self, username, password):
        # Implement the login functionality here
        user = self.db.get_user(username)
        if user is not None and user.password == password:
            return True
        else:
            return False
    def register(self, username, password):
        # Implement the user registration functionality here
        user = self.db.get_user(username)
        if user is None:
            self.db.save_user(UserModel(username, password))
            return True
        else:
            return False