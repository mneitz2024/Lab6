# Matt Neitz

def encoder(string):  # function to encode passwords
    encoded_string = ''
    for i in string:
        i = int(i)
        x = i + 3
        y = str(x)
        encoded_string += y
    return encoded_string


def decoder(string):
    decoded_string = ''
    for i in string:
        i = int(i)
        x = i - 3
        y = str(x)
        decoded_string += y
    return decoded_string


if __name__ == '__main__':
    condition = True
    while condition is True:
        print('Menu')
        print('------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        print('')

        option = int(input('Please enter an option:'))

        if option == 1:  # takes option variable and uses in for loop to encode, decode, or quit the program
            password = input('Please enter your password to encode:')
            encoded_password = encoder(password)
            print('Your password has been encoded and stored!')
        if option == 3:
            condition = False
