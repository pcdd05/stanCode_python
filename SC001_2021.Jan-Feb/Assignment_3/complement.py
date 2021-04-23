"""
File: complement.py
Name: DiCheng
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""

# for DNA strand complement indexing.
COMPLEMENT = "ACTG"


def main():
    """
    Program will check the format of given DNA strand, and if it's legal, building the complement of it.
    """
    input_data = check_format(input("Please give me a DNA strand and I'll find the complement: "))
    print("The complement of " + input_data + " is " + build_complement(input_data))


def check_format(input_data):
    """
    input_data will be checked to upper case and whether is legal format or not.
    :param input_data: str, the given DNA strand.
    :return: str, the DNA strand with legal format.
    """
    # all upper
    input_data = input_data.upper()
    # extension: check character truly among A,T,C,G
    is_legal_format = True
    for char in input_data:
        if COMPLEMENT.find(char) == -1:
            is_legal_format = False
    if not is_legal_format:
        input_data = check_format(input("Illegal DNA strand, please enter among A,T,C,G only: "))
    return input_data


def build_complement(input_data):
    """
    using for-each to find the index of every DNA strand's char in COMPLEMENT, and mapping the complement char.
    :param input_data: str, the DNA strand to be complement.
    :return: str, the DNA strand complement result.
    """
    result = ""
    for char in input_data:
        i = COMPLEMENT.find(char)
        if i < 2:
            i += 2
        else:
            i -= 2
        result += COMPLEMENT[i]
    return result


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
