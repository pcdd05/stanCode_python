"""
File: hangman.py
Name: DiCheng
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    With given number of guess left and hint of guessing, checking answer with new input alphabet every time to see
    if its good guess or not. Try avoid losing all your life point before finding what's the hidden word, otherwise
    you'll be hung.
    """
    life_point = N_TURNS
    ans = random_word()
    current_guess = default_current_guess(len(ans))
    while life_point != 0:
        input_guess = get_input_guess(current_guess, life_point)
        current_guess = match_ans(input_guess, current_guess, ans)
        life_point = check_guess(life_point, input_guess, current_guess)
        if current_guess.find("-") == -1:
            print("You win!!")
            break
        if life_point == 0:
            print("You are completely hung : (")
    print("The word was: " + ans)


def default_current_guess(length):
    """
    Get the default guess hint by the length of answer.
    :param length: the length of random answer.
    :return: str, the default guess hint, which is all blind by "-".
    """
    current_guess = ""
    for i in range(length):
        current_guess += "-"
    return current_guess


def get_input_guess(current_guess, life_point):
    """
    Show the hint of guess and the number of guess left first, then get the new guess input.
    :param current_guess: str, the hint of current guess.
    :param life_point: int, the number of guess left.
    :return: str, the user guess alphabet in legal format.
    """
    print("The word looks like: " + current_guess)
    print("You have " + str(life_point) + " guesses left.")
    return check_format(input("Your guess: "))


def check_format(input_guess):
    """
    check the format in new guess input and return in upper case.
    :param input_guess: str, the given alphabet of new guess.
    :return: str, the guess in legal format and upper case.
    """
    while True:
        if input_guess.isalpha() and len(input_guess) == 1:
            input_guess = input_guess.upper()
            return input_guess
        input_guess = input("illegal format.\nYour guess: ")


def match_ans(input_guess, current_guess, ans):
    """
    Matching new guess alphabet to each answer char if equals, and return the replaced hint of latest guess.
    :param input_guess: str, the new guess alphabet.
    :param current_guess: str, the hint of current guess.
    :param ans: str, the hidden random word.
    :return: str, after matching, return the replaced hint of latest guess.
    """
    result = ""
    for i in range(len(ans)):
        if input_guess == ans[i]:
            result += ans[i]
        else:
            result += current_guess[i]
    return result


def check_guess(life_point, input_guess, current_guess):
    """
    Checking the new guess alphabet can be found in latest guess or not, and reduce 1 point if its not.
    :param life_point: int, the current number of guess left.
    :param input_guess: str, the new guess alphabet input.
    :param current_guess: str, the replaced hint of latest guess.
    :return: the latest number of guess left.
    """
    if current_guess.find(input_guess) != -1:
        print("You are correct!")
        return life_point
    print("There is no " + input_guess + "'s in the word.")
    return life_point - 1


def random_word():
    """
    get random word as hidden answer.
    :return: str, random word
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
