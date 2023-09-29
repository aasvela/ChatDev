'''
This file handles user-related operations for the web application.
'''
from database import Database
from user_logic import UserLogic
class UserModel:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def login(self):
        # Implement the login functionality here
        user_logic = UserLogic()
        result = user_logic.login(self.username, self.password)
        return result
    def register(self):
        # Implement the user registration functionality here
        user_logic = UserLogic()
        result = user_logic.register(self.username, self.password)
        return result