from multiprocessing.sharedctypes import Value
from Battleship import Battleship
import string

class BattleshipGame:
    # Attributes
    _board_size = 0

    # Constructor
    def __init__(self, board_size:int) -> None:
        if (board_size < 8):
            raise ValueError("Board cannot be less than 8x8")
        self._board_size = board_size
        self.battleship = Battleship(self._board_size)

    # Methods
    def play_game(self):
        '''
        Begins game of 1 person battleship
        '''
        while (1):
            # self.display_board()
            print("here")
            print(self.get_players_shot())
            
            break
            
    def display_board(self):
        self.battleship.print_board()

    def get_players_shot(self):
        '''
        Records the shot of a player
        
        Returns coordinates translated into number coordinates in a tuple
        '''
        res = input("Enter shot coordinates: ")

        # Error checking
        if (len(res) != 2):
            raise ValueError("Coordinates must be of length 2")

        letter_char = res[0].upper()
        number_letter = string.ascii_uppercase.find(letter_char)
        if (number_letter > self._board_size):
            raise ValueError(f"{letter_char} is not a valid input")

        number_char = res[1]
        if (not number_char.isdigit() or int(number_char) > self._board_size):
            raise ValueError(f"{number_char} is not a valid integer")

        return (number_letter, int(number_char))