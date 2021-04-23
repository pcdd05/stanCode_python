"""
File: coin_flip_runs.py
Name: DiCheng
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r

# the alphabet representing coin's heads or tails
HT = "HT"


def main():
	"""
	flip a coin to get random heads or tails continuously, stop flip when the given number of row runs achieved.
	"""
	print("Let's flip a coin!")
	num_run = int(check_input_format(input("Number of runs: ")))
	count_num_run = 0
	coin_outcome = ""
	is_in_a_row = False
	while not count_num_run == num_run:
		coin_outcome += HT[r.randint(0, 1)]
		if len(coin_outcome) > 1:
			if coin_outcome[len(coin_outcome) - 2] == coin_outcome[len(coin_outcome) - 1]:
				if not is_in_a_row:
					count_num_run += 1
					is_in_a_row = True
			else:
				is_in_a_row = False
	print(coin_outcome)


def check_input_format(input_data):
	"""
	check if the input data is numbers > 0.
	:param input_data: str, the input number of row runs to achieved.
	:return: str, the data in legal format.
	"""
	while not input_data.isdigit() or int(input_data) <= 0:
		input_data = input("Illegal format, please enter numbers > 0: ")
	return input_data


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
	main()
