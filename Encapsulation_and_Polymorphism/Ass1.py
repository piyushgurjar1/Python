class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password  

    def set_password(self, new_password):
            self.__password = new_password 

    def display_username(self):
        return self.username

user = User("Piyush", "123456")
print("Username:", user.display_username())
print("Current password:", user.get_password())
user.set_password("newPassword")