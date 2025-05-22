def check_lenght(password):
    return len(password) >= 8
def check_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False
def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False
def check_special(password):
    special_chars = "!@#$%^&*()"
    for char in password:
        if char in special_chars:
            return True
    return False

def main():
    while True:
        password = input("Enter password: ")

        if not check_lenght(password):
            print("Password must contain at least 8 characters")
        elif not check_upper(password):
            print("Password must contain at least one uppercase letter")
        elif not check_digit(password):
            print("Password must contain at least one number")
        elif not check_special(password):
            print("Password must contain at least one special character")
        else:
            print(password , "Your password is valid")
            break

if __name__ == "__main__":
    main()



