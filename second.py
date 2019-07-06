import re


def is_username_valid(username):
    # Seharusnya begini, karena tertulis di soal hanya
    # kombinasi huruf besar, kecil, dan angka.
    # Tanpa menyebutkan setidaknya harus ada huruf besar
    # unameRegex = re.compile(r'^[^0-9][0-9a-zA-Z]{5,9}$')
    unameRegex = re.compile(r'^(?=.*[A-Z]+.*)[^0-9][0-9a-zA-Z]{5,9}$')
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

    print(is_username_valid('zeronull'))
    print(is_username_valid('Ayu99v'))
    print(is_password_valid('p@ssW0rd#'))
    print(is_password_valid('C0d3YourFuture!#'))


if __name__ == '__main__':
    main()
