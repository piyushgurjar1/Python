from userAuth.hashing import hash
db = {
    "user1": 12345,
}

def verify(username, password):
    if username in db:
        stored_password_hash = int(db[username])
        input_password_hash = int(hash(password))
        print(stored_password_hash), print(input_password_hash)
        if input_password_hash == stored_password_hash:
            print("Password match")
            return True
    return False