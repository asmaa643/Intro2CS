#################################################################
# FILE : car.py
# WRITER : Asmaa Ghrayeb , asmaa.ghrayeb, 212017719
# EXERCISE : intro2cse ex9 2021
# DESCRIPTION : A simple program that simulates the rush hour game.
#################################################################

class Car:
    """
    A class that simulates a car.
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col)
        location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates = []
        x, y = self.__location
        for i in range(self.__length):
            if self.__orientation == 1:
                coordinates.append((x, y + i))
            elif self.__orientation == 0:
                coordinates.append((x + i, y))
        return coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        if self.__orientation == 0:  # Here there are 'u' or 'd'.
            return {'u': "cause the car to move one step up",
                    'd': "cause the car to move one step down"}
        else:  # Here there are 'l' or 'r'.
            return {'l': "cause the car to move one step left",
                    'r': "cause the car to move one step right"}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """
        x, y = self.__location
        if self.__orientation == 0 and movekey == 'u':
            return [(x - 1, y)]
        elif self.__orientation == 0 and movekey == 'd':
            return [(x + self.__length, y)]
        elif self.__orientation == 1 and movekey == 'r':
            return [(x, y + self.__length)]
        elif self.__orientation == 1 and movekey == 'l':
            return [(x, y - 1)]
        else:  # There aren't cells that must be empty.
            return []

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        possible_moves = self.possible_moves()
        if movekey in possible_moves:  # A movekey must be in possible moves.
            new_location = self.car_coordinates()
            new_location.pop(0)  # Remove the first location cell.
            new_location += self.movement_requirements(movekey)
            self.__location = min(new_location)  # Update the current location.
            return True
        else:
            return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
