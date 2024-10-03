#################################################################
# FILE : math_print.py
# WRITER : Asmaa Ghrayeb
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A simple program that calculate different values
# NOTES: (nothing)
#################################################################

import math


def golden_ratio():
    """These next lines print the golden ratio"""
    print((1 + math.sqrt(5))/2)


def six_squared():
    """These next lines print six squared"""
    print(math.pow(6, 2))


def hypotenuse():
    """These next lines print the hypotenuse of some triangle"""
    print(math.sqrt(5**2 + 12**2))


def pi():
    """These next lines print the value of pi"""
    print(math.pi)


def e():
    """These next lines print the value of e"""
    print(math.e)


def squares_area():
    """These next lines print the squares area from 1 to 10"""
    print(1*1, 2*2, 3*3, 4*4, 5*5, 6*6, 7*7, 8*8, 9*9, 10*10)


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
