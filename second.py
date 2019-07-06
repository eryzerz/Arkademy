import re

def is_username_valid(username):
    unameRegex = re.compile(r'^[^0-9][0-9a-zA-Z]{5,9}$')
    match = unameRegex.search(username)
    if match:
        return True
    else:
        return False


def is_password_valid(password):
    passRegex = re.compile(
        r'^(?=.*[@]+.*)(?=.*[0-9]+.*)(?=.*[A-Z]+.*)(?=.*[!@#\$%\^\&*\)\(+=._-]+.*)[0-9a-zA-Z!@#\$%\^\&*\)\(+=._-]{8,}$')
    match = passRegex.search(password)
    if match:
        return True
    else:
        return False


def main():
    username = input('Username: ')
    print(is_username_valid(username))
    password = input('Password: ')
    print(is_password_valid(password))
    return


if __name__ == '__main__':
    main()