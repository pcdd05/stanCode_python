"""
File: class_reviews.py
Name: DiCheng
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""

# the exit code to exit input data
EXIT_CODE = "-1"
# the class name of SC001
SC001 = "SC001"
# the class name of SC101
SC101 = "SC101"


def main():
    """
    enter class name and input score data continuously,
    once enter exit code, print max, min, avg scores of both classes.
    """
    max_001 = 0
    min_001 = 0
    sum_001 = 0
    score_count_001 = 0
    max_101 = 0
    min_101 = 0
    sum_101 = 0
    score_count_101 = 0

    class_name = check_input_format(input("Which class? "), "name")
    while EXIT_CODE != class_name:
        input_score = int(check_input_format(input("Score: "), "score"))
        if SC001 == class_name:
            max_001 = get_max(max_001, input_score)
            min_001 = get_min(min_001, input_score)
            sum_001 += input_score
            score_count_001 += 1
        else:
            max_101 = get_max(max_101, input_score)
            min_101 = get_min(min_101, input_score)
            sum_101 += input_score
            score_count_101 += 1
        class_name = check_input_format(input("Which class? "), "name")
    if score_count_001 == 0 and score_count_101 == 0:
        print("No class scores were entered")
    else:
        print_outcome(SC001, max_001, min_001, sum_001, score_count_001)
        print_outcome(SC101, max_101, min_101, sum_101, score_count_101)


def check_input_format(input_data, data_type):
    """
    check the format of input data, given data type whether is class name or score,
    if format is illegal, hint to ask enter again.
    if format is legal, return input data with upper case.
    :param input_data: str, the data entered by user.
    :param data_type: str, the type of data.
    :return: str, data with upper case.
    """
    if "score" == data_type:
        while not input_data.isdigit() or int(input_data) < 0:
            input_data = input("Score illegal format, please enter number >=0: ")
    else:
        while EXIT_CODE != input_data:
            if SC001 == input_data.upper() or SC101 == input_data.upper():
                break
            input_data = input("Class name illegal format, please enter either SC001 or SC101: ")
    return input_data.upper()


def get_max(current_max, input_score):
    """
    compare two input numbers, and return bigger one.
    :param current_max: int, the current max score.
    :param input_score: int, the score just input.
    :return: int, compare two numbers and return bigger one.
    """
    if current_max != 0 and current_max > input_score:
        return current_max
    return input_score


def get_min(current_min, input_score):
    """
    compare two input numbers, and return smaller one.
    :param current_min: int, the current min score.
    :param input_score: int, the score just input.
    :return: int, compare two numbers and return smaller one.
    """
    if current_min != 0 and current_min < input_score:
        return current_min
    return input_score


def print_outcome(class_name, max_score, min_score, sum_score, score_count):
    """
    print the outcome to show max, min, avg scores of given class name.
    :param class_name: str, the class name to print.
    :param max_score: str, the max score of all input to print.
    :param min_score: str, the min score of all input to print.
    :param sum_score: str, the sum of scores for calculating average score.
    :param score_count: str, the number of score input counting.
    """
    if score_count > 0:
        print("=============" + class_name + "=============")
        print("Max (" + class_name[2:len(class_name)] + "): " + str(max_score))
        print("Min (" + class_name[2:len(class_name)] + "): " + str(min_score))
        print("Avg (" + class_name[2:len(class_name)] + "): " + str(sum_score/score_count))
    else:
        print("=============" + class_name + "=============")
        print("No score for " + class_name)


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
