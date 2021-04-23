"""
File: boggle.py
Name: DiCheng
----------------------------------------
This program recursively finds all the combination from 4x4 letters input by user
and find matched with dictionary.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
dic = {}                      # Global dictionary


def main():
	"""
	find all the words from 4x4 letters input by user.
	"""
	row_num = 0
	input_dic = {}
	read_dictionary()
	while row_num < 4:
		input_s = input(f"{row_num + 1} row of letters: ").lower()
		if not check_input_format(input_s):
			print("Illegal input")
			break
		build_input_dic(row_num, input_s, input_dic)
		row_num += 1
	if row_num == 4:
		s = time.time()
		boggle_lst = find_boggle_word(input_dic)
		print(f"There are {len(boggle_lst)} words in total.")
		print(f"spent {time.time() - s} seconds.")

def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and get words in each line into a Python dict.
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


def check_input_format(input_s):
	"""
	:param input_s: str, input string by user.
	:return: bool, check if the input string is in legal format or not.
	"""
	if len(input_s) < 7 or len(input_s) > 8:
		return False
	for i in range(len(input_s)):
		if i % 2 == 0:
			if not input_s[i].isalpha():
				return False
		else:
			if not input_s[i].isspace():
				return False
	return True


def build_input_dic(row_num, input_s, input_dic):
	"""
	:param row_num: str, indices which row of user input, will be stored as (x, y) in y-coordinate.
	:param input_s: str, input string by user.
	:param input_dic: dict, build a dictionary that contain all the 4x4 letters,form in {key=(x,y): value=letter}
						eg. {(0,0): "f", (1,0): "y", (2.0): "c", (3.0): "l"}
	"""
	input_s = input_s.replace(" ", "")
	for i in range(len(input_s)):
		input_dic[(i, row_num)] = input_s[i]


def find_boggle_word(input_dic):
	"""
	:param input_dic: dict, all 4x4 letters input by user stored as dict.
	"""
	global dic
	boggle_lst = []
	for y in range(4):
		for x in range(4):
			helper(input_dic, boggle_lst, "", dic, [], x, y, True)
	return boggle_lst


def helper(input_dic, boggle_lst, find_s, search_dic, pass_by_lst, x, y, has_next):
	"""
	:param input_dic: dict, all 4x4 letters input by user stored as dict.
	:param boggle_lst, list, the list stored all the words matched with search_dic.
	:param find_s, str, the str to look up in search_dic that built char by char.
	:param search_dic, dict., the dict. that search for find_s.
	:param pass_by_lst, list, the list stored all the (x, y) coordinate to record which letter has been used.
	:param x, int, x-coordinate in input_dic[key].
	:param y, int, y-coordinate in input_dic[key].
	:param has_next, bool, indicate is there has neighbor letters need to be search or not(the recursion should ended).
	"""
	# check new words first
	if len(find_s) >= 4 and find_s not in boggle_lst and find_s in search_dic:
		print(f"Found \"{find_s}\"")
		boggle_lst.append(find_s)
	# base case
	if not has_next:
		return
	# recursive case
	else:
		for i in range(3):
			for j in range(3):
				if 0 <= x + (j-1) < 4 and 0 <= y + (i-1) < 4 and (x, y) not in pass_by_lst:
					# choose
					find_s += input_dic[(x, y)]
					pass_by_lst.append((x, y))
					if i == 3 and j == 3:
						has_next = False
					if find_s in search_dic:
						# explore
						current_dic = search_dic[find_s]
						helper(input_dic, boggle_lst, find_s, current_dic, pass_by_lst, x + (j-1), y + (i-1), has_next)
					# un-choose
					pass_by_lst.pop()
					find_s = find_s[:len(find_s) - 1]
					current_dic = search_dic


if __name__ == '__main__':
	main()
