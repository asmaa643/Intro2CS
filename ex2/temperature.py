#################################################################
# FILE : temperature.py
# WRITER : Asmaa Ghrayeb , asmaa.ghrayeb , 212017719
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that checks if it is summer yet.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED:None
# NOTES: Nothing
#################################################################

def is_it_summer_yet(t_limit, t_day1, t_day2, t_day3):
    """
    This function gets a number that represents a temperature and 3 other ones.
    It returns if at least 2 of these 3 temperature are bigger than the first.
    """
    if t_day1 > t_limit:
        if t_day2 > t_limit or t_day3 > t_limit:
            return True
    elif t_day2 > t_limit:
        if t_day3 > t_limit:
            return True
    return False
