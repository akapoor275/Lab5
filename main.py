def encode(password):
    encoded_list = []
    for char in password:
        encoded_char = chr(ord(char) + 3)
        encoded_list.append(encoded_char)
    return ''.join(encoded_list)


while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    user_input = input("Please enter an option: ")
    if user_input == 1:
        password = input("Please enter you password to encode: ")
        encoded_password = encode(password)
        # print("Encoded password:", encoded_password)
        print("Your password has been encoded and stored")
    # if user_input == 2:
    #
    elif user_input == 3:
        break

