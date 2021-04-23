"""
File: rocket.py
Name: DiCheng
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	build a rocket with head, belt, upper and lower part, belt and head as tail.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	drawing head.
	"""
	# half_col = ROW + 1
	for i in range(SIZE):
		for k in range(SIZE-i):
			print(" ", end="")
		for j in range(i+1):
			print("/", end="")
		for j in range(i+1):
			print("\\", end="")
		for k in range(SIZE-i):
			print(" ", end="")
		print("")


def belt():
	"""
	drawing belt.
	"""
	col = 2*(SIZE+1)
	for i in range(1):
		print("+", end="")
	for j in range(col-2):
		print("=", end="")
	for i in range(1):
		print("+", end="")
	print("")


def upper():
	"""
	drawing upper part.
	"""
	for i in range(SIZE):
		for j in range(1):
			print("|", end="")
		for k in range(SIZE-i-1):
			print(".", end="")
		for m in range(i+1):
			print("/", end="")
			print("\\", end="")
		for k in range(SIZE-i-1):
			print(".", end="")
		for j in range(1):
			print("|", end="")
		print("")


def lower():
	"""
	drawing lower part.
	"""
	for i in range(SIZE):
		for j in range(1):
			print("|", end="")
		for k in range(i):
			print(".", end="")
		for m in range(SIZE-i):
			print("\\", end="")
			print("/", end="")
		for k in range(i):
			print(".", end="")
		for j in range(1):
			print("|", end="")
		print("")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()