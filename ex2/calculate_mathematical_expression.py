#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Asmaa Ghrayeb , asmaa.ghrayeb , 212017719
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that calculates mathematical expressions.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED:None
# NOTES: Nothing
#################################################################

def calculate_mathematical_expression(num1, num2, math_symbol):
    """
    This function gets two numbers and arithmetic symbol.
    The function calculates and returns the arithmetic operation of the
    numbers using the symbol.
    """
    if math_symbol == "+":
        return num1 + num2
    elif math_symbol == "-":
        return num1 - num2
    elif math_symbol == "*":
        return num1 * num2
    elif num2 == 0 or math_symbol != ":":
        return None
    return num1/num2


def calculate_from_string(arith_operation):
    """
    This function gets a string of an arithmetic operation and calculates it
    using the former function.
    """
    number1, s, number2 = arith_operation.split()
    return calculate_mathematical_expression(float(number1), float(number2), s)
