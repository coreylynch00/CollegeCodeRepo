while True:
    password = input("Password (at least 8 characters) >>> ")
    if len(password) >= 8:
        break

print("Thank you - your password is now", password)