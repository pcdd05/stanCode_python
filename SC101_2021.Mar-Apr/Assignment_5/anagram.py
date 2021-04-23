"""
File: anagram.py
Name: DiCheng
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dic_lst = []                  # Global dictionary list


def main():
    """
    finds all the anagram(s) for the word input by user.
    """
    global dic_lst
    read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    input_s = input("Find anagrams for: ")

    while EXIT != input_s:
        s = time.time()
        print("Searching...")
        anagram_lst = find_anagrams(input_s)
        print(f"{len(anagram_lst)} anagrams: {anagram_lst}")
        print(f"spent {time.time() - s} seconds.")
        input_s = input("Find anagrams for: ")


def read_dictionary():
    """
    read dictionary and stored at global as list.
    """
    global dic_lst
    with open(FILE, "r") as f:
        for line in f:
            dic_lst.append(line.strip("\n"))


def find_anagrams(s):
    """
    :param s: str, the word input by user.
    :return: list, the anagrams as list was found.
    """
    anagram_lst = []
    index_lst = []
    count_lst = [0]
    for i in range(len(s)):
        index_lst.append(i)
    helper(s, index_lst, [], "", anagram_lst, count_lst)
    print(f"search for {count_lst[0]} times.")

    return anagram_lst


def helper(s, index_lst, current_lst, find_s, anagram_lst, count_lst):
    """
    :param s: str, the word input by user.
    :param index_lst, list, the list of index indices for char of s.
    :param current_lst, list the list of current index in recursion.
    :param find_s, str, the str to look up in dict_lst that built char by char.
    :param anagram_lst, list, the list stored all the anagrams.
    """
    global dic_lst
    count_lst[0] += 1
    if has_prefix(find_s):
        if len(current_lst) == len(index_lst):
            if find_s in dic_lst and find_s not in anagram_lst:
                print("Found: " + find_s)
                anagram_lst.append(find_s)
                print("Searching...")
        else:
            for i in index_lst:
                if i not in current_lst:
                    # choose
                    current_lst.append(i)
                    find_s += s[i]
                    # explore
                    helper(s, index_lst, current_lst, find_s, anagram_lst, count_lst)
                    # un-choose
                    current_lst.pop()
                    find_s = find_s[:len(find_s) - 1]


def has_prefix(sub_s):
    """
    :param sub_s: str, the word substring from s.
    :return: boolean, is the any words in dic_lst has same prefix as sub_s or not.
    """
    global dic_lst
    for word in dic_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
