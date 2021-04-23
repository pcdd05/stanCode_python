"""
File: hailstone.py
Name: DiCheng
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    pre-cond: User will enter a random integer.
    post-cond: The program will calculate in Hailstone sequence way, and the number will end up with 1.
    """
    print("This program computes Hailstone sequences.")
    the_number = int(input("\nEnter a number: "))
    steps_count = 0
    while the_number != 1:
        steps_count += 1
        # when the number is odd
        if the_number % 2 != 0:
            print(str(the_number) + " is odd, so I make 3n+1: " + str(the_number * 3 + 1))
            the_number = the_number*3 + 1
        # when the number is even
        else:
            print(str(the_number) + " is even, so I take have: " + str(the_number // 2))
            the_number //= 2
    print("It took " + str(steps_count) + " steps to reach 1.")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
