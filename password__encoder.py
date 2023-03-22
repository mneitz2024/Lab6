# Matt Neitz

def encoder(string):  # function to encode passwords
    encoded_string = ''
    for i in string:
        i = int(i)
        x = i + 3
        y = str(x)
        encoded_string += y
    return encoded_string
