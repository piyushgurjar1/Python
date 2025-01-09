from userAuth.verification import verify
from userAuth.logging import log

username = input("Enter username: ")
password = input("Enter password: ")

if verify(username, password):
    print("Login successful!")
    log(username, "Login successful")
else:
    print("Login failed!")
    log(username, "Failed login attempt")