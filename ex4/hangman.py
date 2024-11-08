#################################################################
# FILE : hangman.py
# WRITER : Asmaa Ghrayeb
# EXERCISE : intro2cse ex4 2021
# DESCRIPTION: A simple program that simulates the hangman game.
# NOTES: In run_single_game I separated and used calling functions as possible
#################################################################

from hangman_helper import*


def update_word_pattern(word, pattern, letter):
    """
    This function gets a pattern with a letter, updates the pattern with
    the letter and returns it
    """
    update_p = ""
    for i in range(len(word)):
        if letter == word[i]:
            update_p += letter
        else:
            update_p += pattern[i]
    return update_p


def how_many_times(word, letter):
    """
    This function gets a word with some letter and returns how many times
    the letter repeats in the word
    """
    times = 0
    for i in word:
        if i == letter:
            times += 1
    return times


def not_valid_guess(a):
    """ This function checks the validity of the input letter """
    return a.isupper() or len(a) > 1 or not a.isalpha() or not a


def do_if_letter(letter, word, wrong, guesses, pattern, points):
    """ This function checks the input letter and updates the display """
    if not_valid_guess(letter):
        msg = "Your input is not valid"
    elif letter in guesses:
        msg = "You chose this letter before. Choose another one!"
    else:
        points -= 1
        guesses.append(letter)
        if letter in word:
            pattern = update_word_pattern(word, pattern, letter)
            n = how_many_times(word, letter)
            points += n * (n + 1) // 2
            msg = "You guessed right, continue!"
        else:
            wrong.append(letter)
            msg = "Unfortunately, you guessed a wrong letter"
    return wrong, guesses, pattern, points, msg


def do_if_hint(words_list, pattern, wrong):
    """ This function show the filtered suggestions """
    filters = filter_words_list(words_list, pattern, wrong)
    if len(filters) > HINT_LENGTH:
        filters = filter_the_filtered(filters)
    show_suggestions(filters)


def calculate_word_score(word, pattern, score):
    """ This function calculates the score after guessing a right word """
    pattern = pattern.replace("_", "")
    n = len(word) - len(pattern)
    score += n * (n + 1) // 2
    return score


def run_single_game(words_list, score):
    """
    This function runs a single game
    :param words_list: A list of words
    :param score: The current points of the players
    :return: The final score after this game overs
    """
    current = get_random_word(words_list)
    message = "Let's start the game"
    pattern = "_" * len(current)
    wrong = list()  # List for the wrong guesses
    guesses = list()  # List for all the right and wrong guesses
    while score > 0 and pattern != current:
        display_state(pattern, wrong, score, message)
        num_of_choice, guess = get_input()
        if num_of_choice == LETTER:
            out = do_if_letter(guess, current, wrong, guesses, pattern, score)
            wrong, guesses, pattern, score, message = out
        elif num_of_choice == WORD:
            score -= 1
            if guess == current:
                score = calculate_word_score(current, pattern, score)
                pattern = current
            else:
                message = "This is not the right word!"
        elif num_of_choice == HINT:
            score -= 1
            do_if_hint(words_list, pattern, wrong)
            message = "Try to guess NOW!"
    message = end_of_single_game(current, pattern)
    display_state(pattern, wrong, score, message)
    return score


def end_of_single_game(word, pattern):
    if word == pattern:
        msg = "You got the word right, the words is: " + word
    else:
        msg = "You lost the game, the word is: " + word
    return msg


def filter_the_filtered(filter_lst):
    """
    This function gets a words list and returns a HINT LENGTH filtered one
    """
    filtered = list()
    step = 1
    for i in range(HINT_LENGTH):
        filtered.append(filter_lst[(step-1)*len(filter_lst)//HINT_LENGTH])
        step += 1
    return filtered


def main():
    """
    This function loads the words list, runs the hangman game as many times
    as the player wants
    """
    games = 0
    lst_of_words = load_words()
    ini_points = POINTS_INITIAL
    answer = True
    while answer:
        points = run_single_game(lst_of_words, ini_points)
        games += 1
        msg = "You played " + str(games) + " game/s & got " + str(points) + \
              " points. Do you want to play again?"
        answer = play_again(msg)
        if points > 0:
            ini_points = points
        else:
            games = 0
            ini_points = POINTS_INITIAL


def same_guessed_letters(word, pattern):
    """
    This function gets a word and a pattern and returns if the word has
    the same revealed letters in the pattern
    """
    for i in range(len(word)):
        if pattern[i] != "_":
            if word[i] != pattern[i]:
                return False
            count_1 = how_many_times(word, word[i])
            count_2 = how_many_times(pattern, word[i])
            if count_1 != count_2:
                return False
    return True


def is_there_wrong(word, lst):
    """
    This function gets a word with a list of letters and returns if the word
    has some letter from the list
    """
    for letter in lst:
        if letter in word:
            return True
    return False


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    This function gets a words list and returns a filtered one using the
    revealed letters in the pattern and the wrong guesses
    """
    filter_lst = list()
    for i in range(len(words)):
        if len(words[i]) != len(pattern):
            continue
        if not same_guessed_letters(words[i], pattern):
            continue
        if is_there_wrong(words[i], wrong_guess_lst):
            continue
        filter_lst.append(words[i])
    return filter_lst


if __name__ == "__main__":
    main()
