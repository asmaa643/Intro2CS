import board
import sys
import helper
import car


class Game:
    """
    A class that run a rush hour game with some board.
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        pass

    def __check_inputs(self, user_input):
        """
        This is a helper function that checks the validity of the user input.
        :param user_input: An input from the user.
        :return: True if is is valid, False else.
        """
        if len(user_input) != 3:
            return False
        if user_input[1] != ",":
            return False
        user_input = user_input.split(",")
        name, movekey = user_input
        if name not in "YBOGWR" or movekey not in "durl":
            return False
        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        win = self.__board.cell_content(self.__board.target_location())
        print(self.__board)
        while win is None:
            choice = input("Choose in the following format: "
                           "name(capital letter),direction(one of: d, u, r, l)"
                           "or '!' if you want to quit the game.")
            if choice == "!":
                break
            if self.__check_inputs(choice):
                name = choice[0]
                movekey = choice[2]
                move_try = self.__board.move_car(name, movekey)
                win = self.__board.cell_content(
                    self.__board.target_location())
                if move_try:
                    print("The car moves successfully.")
                    print(self.__board)
                else:
                    print("Can't move the car. Try again!")
            else:
                print("Please enter an input like the format above.")
        if win is not None:
            print("You win the game!")


if __name__ == "__main__":
    board_of_game = board.Board()
    json_file = sys.argv[1]
    json_data = helper.load_json(json_file)
    for key, value in json_data.items():
        if value[0] not in [2, 3, 4]:
            continue
        if tuple(value[1]) not in board_of_game.cell_list():
            continue
        if value[2] not in [0, 1]:
            continue
        if key not in "YBOGWR":
            continue
        board_of_game.add_car(
            car.Car(key, value[0], tuple(value[1]), value[2]))
    game = Game(board_of_game)
    game.play()
