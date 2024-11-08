class Board:
    """
    A class that simulates a rush hour game board.
    The class builds a board 7x7, add cars to it and move cars in it.
    """

    def __init__(self):
        self.__target_cell = 3, 7
        self.__cars = list()
        self.__size = 7
        self.__board = list()
        for i in range(self.__size):
            row = []
            for _ in range(self.__size):
                row.append("_")
            self.__board.append(row)
            if i != 3:
                self.__board[i].append("*")
            else:
                self.__board[i].append("_")  # _ is the target location.

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        lst = []
        for row in self.__board:
            lst.append(' '.join([ch for ch in row]))  # Split the cells.
        # Split lines.
        return '\n'.join(lst)

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        lst = []
        for i in range(self.__size):
            for j in range(self.__size):
                lst.append((i, j))
        lst.append(self.target_location())
        return lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        lst = []
        for car in self.__cars:  # For every car check possible moves.
            possible_moves = car.possible_moves().items()
            for k, v in possible_moves:
                new_tup = (car.get_name(), k, v)
                free_places = car.movement_requirements(new_tup[1])
                if free_places:
                    flag = True
                    for tup in free_places:
                        # Check if the required coordinates for a car are empty
                        if tup not in self.cell_list() or \
                                self.cell_content(tup):
                            flag = False
                    if flag:  # It is a possible move, add it.
                        lst.append(new_tup)
        return lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return self.__target_cell

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        row, col = coordinate

        if self.__board[row][col] != "_":
            return self.__board[row][col]
        # If a cell isn't empty, it means that it contains part of a car.
        else:
            return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for park_car in self.__cars:  # Check if the car wasn't added before.
            if car.get_name() == park_car.get_name():
                return False
        for cord in car.car_coordinates():
            # Check if the car's coordinates are in the board and empty.
            if cord not in self.cell_list() or self.cell_content(cord):
                return False
        for cord in car.car_coordinates():
            x, y = cord  # It is possible to add the car to the board.
            self.__board[x][y] = car.get_name()
        self.__cars.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for move in self.possible_moves():  # Check which move from the
            # possible ones name & movekey are, if not found return False.
            move_name = move[0]
            key = move[1]
            if move_name == name and key == movekey:
                for c in self.__cars:  # Check which car is the one to move.
                    if c.get_name() == name:
                        cur_place = c.car_coordinates()  # Get its coordinates.
                        c.move(movekey)  # Update the coordinates.
                        new_place = c.car_coordinates()
                        # Check if new cells are in range.
                        for cord in new_place:
                            if cord not in self.cell_list():
                                return False
                        # Update the car location in the board.
                        for coordinate in cur_place:
                            x, y = coordinate
                            self.__board[x][y] = "_"
                        for coordinate in new_place:
                            x, y = coordinate
                            self.__board[x][y] = name
                        # The location was updated, this is success.
                        return True
        return False
