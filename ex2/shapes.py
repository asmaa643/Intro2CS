#################################################################
# FILE : shapes.py
# WRITER : Asmaa Ghrayeb , asmaa.ghrayeb , 212017719
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that calculates the area of 3 shapes.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED:None
# NOTES: Nothing
#################################################################
import math


def circle_area(radius):
    """ This function gets a radius and returns its circle area """
    return math.pi * radius * radius


def rectangle_area(side_1, side_2):
    """ This function gets 2 sides and returns the rectangle area """
    return side_1 * side_2


def triangle_area(side):
    """ This function gets a triangle side and returns the area of it """
    return (math.sqrt(3) / 4) * side * side


def shape_area():
    """
    This function calculates and returns the area of shape that user
    chooses from three: circle, rectangle and triangle.
    """
    choice = input("Choose shape (1=circle, 2=rectangle, 3=triangle): ")
    if choice == "1":
        radius = float(input())
        return circle_area(radius)
    elif choice == "2":
        side1 = float(input())
        side2 = float(input())
        return rectangle_area(side1, side2)
    elif choice == "3":
        side = float(input())
        return triangle_area(side)
    return None
