"""
File: caesar.py
Name: DiCheng
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    With given secret and ciphered string, deciphering to original string.
    """
    key = int(check_format(input("Secret number: "), "int"))
    ciphered_string = check_format(input("What's the ciphered string? "), "str")
    print("The deciphered string is: " + decipher(ciphered_string, key))


def check_format(input_data, data_type):
    """
    input_data will be checked by the its own data type.
    :param input_data: str, the given key or ciphered string.
    :param data_type: str, indicate what kind of data type to check format.
    :return: str, input data all checked in legal format.
    """
    # extension: check secret number isdigit
    if data_type == "int":
        if not input_data.isdigit():
            input_data = check_format(input("Secret number should be a number, enter again: "), "int")
    else:
        # all upper
        input_data = input_data.upper()
    return input_data


def decipher(ciphered_string, key):
    """
    Using key to get deciphered index and reformed the string.
    :param ciphered_string: str, the given ciphered string to be deciphered.
    :param key: int, the given secret number as key to deciphered the string.
    :return: str, the string been deciphered.
    """
    deciphered_string = ""
    for char in ciphered_string:
        if char.isalpha():
            deciphered_index = deciphered_index_with_key(ALPHABET.find(char), key)
            deciphered_string += ALPHABET[deciphered_index]
        else:
            deciphered_string += char
    return deciphered_string


def deciphered_index_with_key(index, key):
    """
    Using key to find the deciphered index, which is the original alphabet.
    :param index: int, the index of each char of ciphered string in ALPHABET.
    :param key: int, the secret number to decided how many index position should move to deciphered.
    :return: int, the index been deciphered.
    """
    if index + key > 25:
        return index + key - 26
    return index + key


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
