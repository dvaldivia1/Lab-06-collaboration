def encoder(password_input):

    password_list = []

    for i in range(0, len(password_input)):
        password_list.append(3 + int(password_input[i]))

        if password_list[i] > 10:
            password_list[i] = password_list[i] % 10

    password_encoded = ''

    for j in range(0, len(password_list)):
        password_encoded += str(password_list[j])

    return password_encoded


def decoder(password_encoded):

    password_decoded_list = []

    for i in range(0, len(password_encoded)):
        password_decoded_list.append(int(password_encoded[i]) - 3)

        if password_decoded_list[i] < 0:
            password_decoded_list[i] = password_decoded_list[i] + 10

    password_decoded = ''

    for j in range(0, len(password_decoded_list)):
        password_decoded += str(password_decoded_list[j])

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

            password_encoded = encoder(password_input)
            print("Your password has been encoded and stored!")

        elif decision == 2:

            password_decoded = decoder(password_encoded)
            print(f"The encoded password is {password_encoded}, and the original password is {password_decoded}")

        elif decision == 3:
            break


if __name__ == '__main__':
    main()
