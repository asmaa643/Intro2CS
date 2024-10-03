#################################################################
# FILE : quadratic_equation.py
# WRITER : Asmaa Ghrayeb , asmaa.ghrayeb , 212017719
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that solves a quadratic equation.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED:None
# NOTES: Nothing
#################################################################
def quadratic_equation(a, b, c):
    """
    This function gets three parameters that represent the coefficients of
    quadratic equation and calculates and returns the equation's solutions.
    """
    delta = b**2 - 4*a*c
    if delta > 0:
        return (-b + delta**0.5)/(2*a), (-b - delta**0.5)/(2*a)
    elif delta == 0:
        return -b / (2*a), None
    return None, None


def quadratic_equation_user_input():
    """
    This function solves an equation that user inputs.
    It prints if the quadratic equation has solutions or not and prints them.
    """
    three_num = input("Insert coefficients a, b, and c: ")
    a, b, c = three_num.split()
    if float(a) == 0:
        print("The parameter 'a' may not equal 0")
        return
    x, y = quadratic_equation(float(a), float(b), float(c))
    if x is None and y is None:
        print("The equation has no solutions")
    elif y is None:
        print("The equation has 1 solution: " + str(x))
    else:
        print("The equation has 2 solutions: " + str(x) + " and " + str(y))
