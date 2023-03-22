# lab 06 by Diego Valdivia

def encode(password_input):

    password_list = []

    for i in range(0, len(password_input)):
        password_list.append(3 + int(password_input[i]))

        if password_list[i] > 10:
            password_list[i] = password_list[i] % 10

    password_encoded = ''

    for j in range(0, len(password_list)):
        password_encoded += str(password_list[j])

    return password_encoded


# Jett Nguyen
def decode(encoded):
    password_decoded = ''
    for char in encoded:
        password_decoded += (str(int(char) - 3))  # subtracts 3 to each number in the password
    return password_decoded


def main():

    menu_title = "Menu\n-------------"

    option_1 = "\n1. Encode"
    option_2 = "\n2. Decode"
    option_3 = "\n3. Quit"

    table = menu_title + option_1 + option_2 + option_3

    start = True

    password_encoded = ''

    while start:

        print(table)

        decision = int(input("Please enter an option: "))

        if decision == 1:

            password_input = input("Please enter your password to encode: ")

            password_encoded = encode(password_input)
            print("Your password has been encoded and stored!\n")

        elif decision == 2:

            password_decoded = decode(password_encoded)
            print(f"The encoded password is {password_encoded}, and the original password is {password_decoded}.\n")

        elif decision == 3:
            break


if __name__ == '__main__':
    main()
