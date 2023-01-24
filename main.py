import tkinter as tk
from db import Database

db = Database()

class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("400x300")

        # Create the account label and entry
        account_label = tk.Label(self, text="Account:")
        account_label.pack()
        self.account_entry = tk.Entry(self)
        self.account_entry.pack()

        # Create the password label and entry
        password_label = tk.Label(self, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Create the url label and entry
        url_label = tk.Label(self, text="URL:")
        url_label.pack()
        self.url_entry = tk.Entry(self)
        self.url_entry.pack()

        # Create the add password button
        add_password_button = tk.Button(self, text="Add Password", command=self.add_password)
        add_password_button.pack()

        # Create the get password button
        get_password_button = tk.Button(self, text="Get Password", command=self.get_password)
        get_password_button.pack()

        # Create the update password button
        update_password_button = tk.Button(self, text="Update Password", command=self.update_password)
        update_password_button.pack()

        # Create the history button
        history_button = tk.Button(self, text="History", command=self.history)
        history_button.pack()

    def add_password(self):
        account = self.account_entry.get()
        password = self.password_entry.get()
        url = self.url_entry.get()
        db.add_password(account, password, url)
        self.account_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.url_entry.delete(0, tk.END)

if __name__ == '__main__':
    app = PasswordManager()
    app.mainloop()
