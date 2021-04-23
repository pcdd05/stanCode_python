"""
File: similarity.py
Name: DiCheng
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    given 2 DNA sequences and find the best matched section.
    """
    long_seq = check_format(input("Please give me a DNA sequence to search: "))
    short_seq = check_format(input("What DNA sequence would you like to match: "))
    # extension: check both sequences length, make share it can be compared
    while len(long_seq) < len(short_seq):
        long_seq = check_format(input("1st DNA sequence(to search) should be longer, enter again: "))
        short_seq = check_format(input("2nd DNA sequence(to match) should be shorter, enter again: "))
    print("The best match is " + find_best_match(long_seq, short_seq))


def check_format(input_data):
    """
    input_data will be checked to upper case and whether is legal format or not.
    :param input_data: str, the given DNA sequence.
    :return: str, the DNA sequence with legal format.
    """
    # all upper
    input_data = input_data.upper()
    # extension: check character truly among A,T,C,G
    is_legal_format = True
    for char in input_data:
        if "ATCG".find(char) == -1:
            is_legal_format = False
    if not is_legal_format:
        input_data = check_format(input("Illegal DNA sequence, please enter among A,T,C,G only: "))
    return input_data


def find_best_match(long_seq, short_seq):
    """
    Using indexing to extract DNA sequence section by section, finding the best matched.
    :param long_seq: str, the given DNA sequence to be matched.
    :param short_seq: str, the given DNA sequence to match.
    :return: str, the best matched of DNA section.
    """
    best_match_score = 0
    best_match_index = 0
    for i in range(len(long_seq) - len(short_seq) + 1):
        match_score = 0
        for j in range(len(short_seq)):
            if long_seq[i+j] == short_seq[j]:
                match_score += 1
        if match_score > best_match_score:
            best_match_score = match_score
            best_match_index = i
    return long_seq[best_match_index:best_match_index + len(short_seq)]


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
