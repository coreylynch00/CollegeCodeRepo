while True:
    print("Password must be at least 8 characters with at "
          "least 1 digit and 1 uppercase letter")
    password = input("Password >>> ")
    if len(password) >= 8:
        uppers = 0
        digits = 0
        i = 0
        while i < len(password):
            if password[i].isupper():
                uppers += 1
            elif password[i].isdigit():
                digits += 1
            i += 1

        if uppers >= 1 and digits >= 1:
            break

print("Thank you - your password is now", password)



