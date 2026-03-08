users = {
    "farmer1": "1234",
    "farmer2": "abcd"
}

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("✅ Login Successful")
        return True
    else:
        print("❌ Invalid username or password")
        return False