# Jett Nguyen
def decode(encoded):
    password_decoded = ''
    for char in encoded:
        password_decoded += (str(int(char) - 3))  # subtracts 3 to each number in the password
    return password_decoded
