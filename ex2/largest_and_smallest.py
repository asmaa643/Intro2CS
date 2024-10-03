#################################################################
# FILE : largest_and_smallest.py
# WRITER : Asmaa Ghrayeb
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that finds the largest and the smallest
# from three numbers.
# NOTES: I chose (2, 2, 2) because the function works with some or all equal
# numbers and (2.1, 2.7, 2.5) to show that it works also with float numbers
# with small difference.
#################################################################

def largest_and_smallest(x, y, z):
    """
    This function gets three numbers and returns the largest number and the
    smallest one separated.
    """
    if x >= y and x >= z:
        max_n = x
        min_n = y
        if y >= z:
            min_n = z
    elif y > x and z > x:
        min_n = x
        max_n = z
        if y >= z:
            max_n = y
    elif y > x:
        max_n = y
        min_n = z
    else:
        max_n = z
        min_n = y
    return max_n, min_n


def check_largest_and_smallest():
    """ This function checks the correctness of the former function """
    if largest_and_smallest(17, 1, 6) != (17, 1):
        return False
    if largest_and_smallest(1, 17, 6) != (17, 1):
        return False
    if largest_and_smallest(1, 1, 2) != (2, 1):
        return False
    if largest_and_smallest(2, 2, 2) != (2, 2):
        return False
    if largest_and_smallest(2.1, 2.7, 2.5) != (2.7, 2.1):
        return False
    return True
