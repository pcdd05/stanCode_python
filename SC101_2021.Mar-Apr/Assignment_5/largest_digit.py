"""
File: largest_digit.py
Name: DiCheng
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number to find largest digit.
	:return: int, largest digit was found.
	"""
	return helper(n, 0)


def helper(n, current_max):
	"""
	:param n: int, the number to find largest digit.
	:param current_max: int, current max digit was found.
	:return: int, largest digit was found.
	"""
	# get positive int
	if n < 0:
		n *= -1
	# get last digit num
	digit_num = n - (n // 10) * 10
	if 0 < digit_num <= 9 and digit_num > current_max:
		current_max = digit_num
	# base case
	if n // 10 == 0:
		return current_max
	# recursive case
	else:
		return helper(n // 10, current_max)


if __name__ == '__main__':
	main()
