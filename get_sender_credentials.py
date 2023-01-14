def read_email_from_file():
    try:
        file = open('sender_email.txt', "r")
    except FileNotFoundError:
        raise Exception("EmailNotProvidedError: Provide a sender email in a file in the same directory with the name 'sender_email.txt' ")
    email = file.read().strip()
    return email


def read_password_from_file():
    try:
        file = open('sender_password.txt', "r")
    except FileNotFoundError:
        raise Exception("PasswordNotProvidedError: Provide a sender password in a file in the same directory with the name 'sender_password.txt' ")
    password = file.read().strip()
    return password
