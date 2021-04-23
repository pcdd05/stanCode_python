"""
File: anagram_dic_ver.py
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
dic = {}                      # Global dictionary


def main():
    """
    finds all the anagram(s) for the word input by user.
    """
    global dic
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
    read dictionary and stored at global as dict.
    """
    global dic
    current_dic = {}
    with open(FILE, "r") as f:
        for line in f:
            word = line.strip("\n")
            build_word_dic(word, current_dic, 0)
    dic = current_dic


def build_word_dic(word, current_dic, index):
    """
    :param word: str, the word that read from file.
    :param current_dic: dict, the current dict. was built.
    :param index: int, the index for indices word char by char.
    """
    sub_word = word[:index + 1]
    if len(sub_word) == len(word):
        current_dic[sub_word] = {sub_word: word}
        return
    else:
        if sub_word not in current_dic:
            current_dic[sub_word] = {}
        sub_dic = current_dic[sub_word]
        build_word_dic(word, sub_dic, index + 1)


def find_anagrams(s):
    """
    :param s: str, the word input by user.
    :return: list, the anagrams as list was found.
    """
    global dic
    anagram_lst = []
    index_lst = []
    count_lst = [0]
    for i in range(len(s)):
        index_lst.append(i)
    helper(s, index_lst, [], "", anagram_lst, dic, count_lst)
    print(f"search for {count_lst[0]} times.")

    return anagram_lst


def helper(s, index_lst, current_lst, find_s, anagram_lst, search_dic, count_lst):
    """
    :param s: str, the word input by user.
    :param index_lst, list, the list of index indices for char of s.
    :param current_lst, list the list of current index in recursion.
    :param find_s, str, the str to look up in dict_lst that built char by char.
    :param anagram_lst, list, the list stored all the anagrams.
    :param search_dic, dict., the dict. that search for find_s.
    """
    count_lst[0] += 1
    if len(current_lst) == len(s) and find_s in search_dic:
        if find_s not in anagram_lst:
            print("Found: " + find_s)
            anagram_lst.append(find_s)
            print("Searching...")
            return
    else:
        for i in index_lst:
            if i not in current_lst:
                # choose
                current_lst.append(i)
                find_s += s[i]
                if find_s in search_dic:
                    current_dic = search_dic[find_s]
                    # explore
                    helper(s, index_lst, current_lst, find_s, anagram_lst, current_dic, count_lst)
                # un-choose
                current_lst.pop()
                find_s = find_s[:len(find_s) - 1]
                current_dic = search_dic


if __name__ == '__main__':
    main()
