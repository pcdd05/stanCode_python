"""
File: hangman_ext.py
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


# This constant which minimum as 3 controls the number of guess the player has, and the height of claw as well.
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
    hint = ">>Game Start"
    draw_hangman(hint, current_guess, life_point)
    while life_point != 0:
        input_guess = check_format(input("Enter your guess: "), current_guess, life_point)
        current_guess = match_ans(input_guess, current_guess, ans)
        life_point = check_guess(life_point, input_guess, current_guess)
        if current_guess.find("-") == -1:
            hint = "Awesome!**"
            break
        if life_point == 0:
            hint = "GAME OVER<<"
    current_guess = ans
    draw_hangman(hint, current_guess, life_point)


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


def check_format(input_guess, current_guess, life_point):
    """
    Check the format in new guess input and return in upper case, while drawing latest guess status.
    :param input_guess: str, the given alphabet of new guess.
    :param current_guess: str, str, the hint of current guess.
    :param life_point: int, the current number of guess left.
    :return: str, the guess in legal format and upper case.
    """
    while True:
        if input_guess.isalpha() and len(input_guess) == 1:
            input_guess = input_guess.upper()
            return input_guess
        hint = "Illegal format!"
        draw_hangman(hint, current_guess, life_point)
        input_guess = input("Enter Your guess again: ")


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
    Checking the new guess alphabet can be found in latest guess or not, and reduce 1 point if its not,
    while drawing latest guess status.
    :param life_point: int, the current number of guess left.
    :param input_guess: str, the new guess alphabet input.
    :param current_guess: str, the replaced hint of latest guess.
    :return: the latest number of guess left.
    """
    if current_guess.find(input_guess) != -1:
        hint = "You are correct!"
        if "-" in current_guess:
            draw_hangman(hint, current_guess, life_point)
        return life_point
    hint = "There is no \"" + input_guess + "\""
    life_point -= 1
    if life_point > 0:
        draw_hangman(hint, current_guess, life_point)
    return life_point


def draw_hangman(hint, current_guess, life_point):
    """
    Just drawing something funny.
    :param hint: str, the status description will show on the first line of hint board.
    :param current_guess: str, the latest hint of guess will show on the second line of hint board.
    :param life_point: int, the number of guess left will show on the third line of hint board.
    :return: nothing really return in code, just a hilarious paint to console.
    """
    # define variable
    line1 = " " + hint
    if hint.find("<") != -1:
        line2 = " Answer is: " + current_guess
    else:
        line2 = " Guess hint: " + current_guess + "   "
    line3 = " Your life point: " + str(life_point) + "   "
    if hint.find(">") != -1:
        greeting = random_greeting(0)
    elif hint.find("*") != -1:
        greeting = random_greeting(4)
    elif life_point == 2:
        greeting = random_greeting(1)
    elif life_point == 1:
        greeting = random_greeting(2)
    elif life_point == 0:
        greeting = random_greeting(3)
    else:
        greeting = random_greeting(999)
    # draw empty 2 rows
    for k in range(2):
        print("")
    # draw claw and man
    draw_claw_and_man(current_guess, life_point, greeting)
    # draw hint board
    draw_hint_board(current_guess, line1, line2, line3)


def draw_claw_and_man(current_guess, life_point, greeting):
    """
    These code smells bad... :'(
    :param current_guess: str, the latest hint of guess show on hint board, to decide the hint board width.
    :param life_point: int, the latest number of guess left to decide the position of claw and man's life.
    :param greeting: str, some gibberish talking from man.
    :return: nothing really return in code, just a hilarious paint to console.
    """
    for i in range(N_TURNS + 5):  # claw height
        for j in range(15 + len(current_guess)):  # board width
            if i == 0:  # claw top
                if j < (15 + len(current_guess))//2:
                    print("_", end="")
            if i == 1:  # first section of rope
                if j == 0:
                    print("|", end="")
                elif j == (15 + len(current_guess))//2 - 1:
                    print("|", end="")
                else:
                    print(" ", end="")
            if i == 2:  # claw init position
                if j == 0:
                    print("|", end="")
                elif life_point == N_TURNS:
                    if j == (15 + len(current_guess)) // 2 - 1 - 1:
                        print("{", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        print("}", end="")
                    else:
                        print(" ", end="")
                else:
                    if j == (15 + len(current_guess)) // 2 - 1:
                        print("|", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 5 and N_TURNS == 3 and life_point == 0:
                        print(greeting, end="")
                    else:
                        print(" ", end="")
            # middle section of rope
            if i > 2 and (N_TURNS + 5) - i > 5:
                if j == 0:
                    print("|", end="")
                elif life_point + i == N_TURNS + 2:  # claw position
                    if j == (15 + len(current_guess)) // 2 - 1 - 1:
                        print("{", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        print("}", end="")
                    else:
                        print(" ", end="")
                elif life_point + i < N_TURNS + 2:
                    if j == (15 + len(current_guess)) // 2 - 1:
                        print("|", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
            if N_TURNS > 3 and life_point == 0 and (N_TURNS + 5) - i == 6:
                if j == (15 + len(current_guess)) // 2 - 1 + 5:
                    print(greeting, end="")
            # bottom 5 rows: man position
            if (N_TURNS + 5) - i == 5:
                if j == 0:
                    print("|", end="")
                elif life_point > 2:
                    if j == (15 + len(current_guess)) // 2 - 1 + 5:
                        print(greeting, end="")
                    else:
                        print(" ", end="")
                elif life_point == 2:
                    if j == (15 + len(current_guess)) // 2 - 1 - 2:
                        print("{", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 2:
                        print("}", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 5:
                        print(greeting, end="")
                    else:
                        print(" ", end="")
                elif life_point == 1:
                    if j == (15 + len(current_guess)) // 2 - 1:
                        print("|", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 5:
                        print(greeting, end="")
                    else:
                        print(" ", end="")
                else:
                    if j == (15 + len(current_guess)) // 2 - 1 - 2:
                        print("{", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 - 1:
                        print("X", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1:
                        print("'", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        print("(", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 2:
                        print("}", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 5:
                        print("/", end="")
                    else:
                        print(" ", end="")
            if (N_TURNS + 5) - i == 4:
                if j == 0:
                    print("|", end="")
                elif life_point > 2:
                    if j == (15 + len(current_guess)) // 2 - 1 - 1:
                        print(":", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        print(")", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 5:
                        print("/", end="")
                    else:
                        print(" ", end="")
                elif life_point == 2:
                    if j == (15 + len(current_guess)) // 2 - 1 - 1:
                        print(":", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        if greeting.find("yay") != -1:
                            print(")", end="")
                        else: print("|", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 5:
                        print("/", end="")
                    else:
                        print(" ", end="")
                elif life_point == 1:
                    if j == (15 + len(current_guess)) // 2 - 1 - 2:
                        print("{", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 - 1:
                        print(":", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1:
                        if greeting.find("yay") != -1:
                            print(" ", end="")
                        else:
                            print("'", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        if greeting.find("yay") != -1:
                            print(")", end="")
                        else:
                            print("(", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 2:
                        print("}", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 5:
                        print("/", end="")
                    else:
                        print(" ", end="")
                else:
                    if j == (15 + len(current_guess)) // 2 - 1 - 1:
                        print("/", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1:
                        print("|", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        print("\\", end="")
                    else:
                        print(" ", end="")
            if (N_TURNS + 5) - i == 3:
                if j == 0:
                    print("|", end="")
                elif life_point != 0:
                    if j == (15 + len(current_guess)) // 2 - 1 - 1:
                        print("\\", end="")
                    elif j == (15 + len(current_guess))//2 - 1:
                        print("|", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        print("/", end="")
                    else:
                        print(" ", end="")
                else:
                    if j == (15 + len(current_guess))//2 - 1:
                        print("|", end="")
                    else:
                        print(" ", end="")
            if (N_TURNS + 5) - i == 2:
                if j == 0:
                    print("|", end="")
                elif life_point != 0:
                    if j == (15 + len(current_guess))//2 - 1:
                        print("|", end="")
                    else:
                        print(" ", end="")
                else:
                    if j == (15 + len(current_guess))//2 - 1 - 1:
                        print("|", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        print("|", end="")
                    else:
                        print(" ", end="")
            if (N_TURNS + 5) - i == 1:  # last row
                if j == 0:
                    print("|", end="")
                elif life_point != 0:
                    if j == (15 + len(current_guess))//2 - 1 - 1:
                        print("/", end="")
                    elif j == (15 + len(current_guess)) // 2 - 1 + 1:
                        print("\\", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
        print("")


def draw_hint_board(current_guess, line1, line2, line3):
    """
    Is it hint board or a bloody execution stand?
    :param current_guess: str, the latest hint of guess show on hint board, to decide the hint board width.
    :param line1: str, the first line of hint board, which is status description.
    :param line2: str, the second line of hint board, which is latest guess.
    :param line3: str, the third line of hint board, which is latest guess left.
    :return: nothing really return in code, just a hilarious paint to console.
    """
    for m in range(5):  # hint board height
        for n in range(15 + len(current_guess)):  # hint board width
            if m == 0 or m == 4:
                print("-", end="")
            elif m == 1:
                if n == 0 or n == 13 + len(current_guess):
                    print("|", end="")
                if n < len(line1):
                    print(line1[n], end="")
                else:
                    print(" ", end="")
            elif m == 2:
                if n == 0 or n == 13 + len(current_guess):
                    print("|", end=" ")
                else:
                    if n < len(line2):
                        print(line2[n], end="")
                    else:
                        print(" ", end="")
            elif m == 3:
                if n == 0 or n == 13 + len(current_guess):
                    print("|", end="")
                if n < len(line3):
                    print(line3[n], end="")
                else:
                    print(" ", end="")
        print("")


def random_greeting(i):
    """
    some gibberish might help to find missing Karel.
    :param i: int, a param to specify the man's greeting.
    :return: str, something for the man to jabber.
    """
    if i == 0:
        return "I wanna play a game~"
    elif i == 1:
        return "WHAT IS THAT on the top of my head??"
    elif i == 2:
        return "oh no, help meeeeee!!"
    elif i == 3:
        return ".......buh bye, my dear Karel."
    elif i == 4:
        return "yay! you save me, who's next to play with me?"
    else:
        num = random.choice(range(9))
        if num == 0:
            return "how are you today?"
        elif num == 1:
            return "Have you seen Karel?"
        elif num == 2:
            return "hmmm, I can't find Karel."
        elif num == 3:
            return "I like to play with Karel, but where is he?"
        elif num == 4:
            return "I think Karel was hung last night."
        elif num == 5:
            return "I'm starving."
        elif num == 6:
            return "Could you please call foodpanda or UberEat for me?"
        elif num == 7:
            return "hey, who's the guy behind you?"
        elif num == 8:
            return "don't look back, I heard something strange."


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


#
# post-credits scene: the script of man.
#
#
#    : )
#    \|/
#     |
#    / \
#
#
# _______
# |     |
# |    { }
# |
# |    : )
# |    \|/
# |     |
# |    / \
#
#
# _______
# |     |
# |     |
# |   {   }
# |    : |
# |    \|/
# |     |
# |    / \
#
#  _______
# |     |
# |     |
# |     |
# |   {:'(}
# |    \|/
# |     |
# |    / \
#
# _______
# |     |
# |     |
# |   {X'(}
# |    /|\
# |     |
# |    / \
# |


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
