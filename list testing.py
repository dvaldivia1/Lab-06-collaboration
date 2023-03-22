# password_input = input("Enter password: ")
# password_list = []
#
# for i in range(0,len(password_input)):
#     password_list.append(int(password_input[i]))
#
# print(password_list)
#
# print("Element 3 of your list is:", password_list[2])

password_input = input("Enter password: ")
password_list = []
encoded_password = ''

for i in range(0, len(password_input)):
    encoded_digit = 3 + int(password_input[i])

    password_list.append(encoded_digit)

for j in range(0, len(password_list)):

    encoded_password += str(3 + int(password_input[j]))

print(encoded_password)
