'''
This is the main file of the web application for newly divorced people.
'''
import tkinter as tk
from tkinter import messagebox
from app_logic import AppLogic
from user import UserModel
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Newly Divorced App")
        self.create_widgets()
        self.app_logic = AppLogic()
    def create_widgets(self):
        # Create and configure the GUI elements here
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()
        self.register_button = tk.Button(self.root, text="Register", command=self.register)
        self.register_button.pack()
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.app_logic.authenticate_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = UserModel(username, password)
        if self.app_logic.save_user(user):
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "Username already exists.")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = App()
    app.run()