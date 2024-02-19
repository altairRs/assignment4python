class UserService:
    def __init__(self):
        self.users = {'admin': 'admin123'}

    def register(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose another one.")
            return False
        else:
            self.users[username] = password
            print("Registration successful.")
            return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Login successful.")
            return True, username
        else:
            print("Invalid username or password. Please try again.")
            return False, None

    def view_user_info(self):
        print("User Information:")
        for username, password in self.users.items():
            print(f"Username: {username}, Password: {password}")
