"""
File: quadratic_solver.py
Name: DiCheng
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	pre-cond: User will need to enter 3 random integers, then stanCode Quadratic Solver will give you real roots.
	post-cond: If discriminant > 0, get 2 real roots; if discriminant = 0, get 1 real root; otherwise no real root.
	"""
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))
	discriminant = b**2 - 4*a*c
	# 2 real roots
	if discriminant > 0:
		r1 = (-b + math.sqrt(discriminant)) / 2 * a
		r2 = (-b - math.sqrt(discriminant)) / 2 * a
		print("Two roots: " + str(r1) + " , " + str(r2))
	# 1 real root
	elif discriminant == 0:
		r = (-b + math.sqrt(discriminant)) / 2 * a
		print("One root: " + str(r))
	# no real roots (discriminant < 0)
	else:
		print("No real roots")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
