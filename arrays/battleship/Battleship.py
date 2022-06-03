from random import randint

class Battleship:
    # Attributes
    player_board = [[]]
    actual_board = [[]]
    board_size = 0
    ships = 5

    # Contructor
    def __init__(self, board_size) -> None:
        self.board_size = board_size
        self.player_board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.actual_board = [[0 for _ in range(board_size)] for _ in range(board_size)]
        self.initialize_gameboard()

    # Methods
    def record_shot(self, x_coord, y_coord):
        '''
        Records shop at specific coordinate point. Will check if shot was a hit or not

        Returns: 1 if hit. 2 if not a hit
        '''
        

    # Initialization Methods >>> IGNORE
    def initialize_gameboard(self):
        '''
        Adds five ships of sizes 2,3,4,5,6
        '''
        ships_to_add = [2,3,4,5,6]

        for ship in ships_to_add:
            while 1:
                x_coord = randint(0, self.board_size)
                y_coord = randint(0, self.board_size)
                
                if (not self.check_coords(x_coord, y_coord, ship)): continue

                # Check to see if valid in x direction
                if (ship % 2):
                    if (self.check_x_placement(x_coord, y_coord, ship)):
                        self.hide_ship(x_coord, y_coord, 0, ship)
                        break
                
                self.check_y_placement(x_coord, y_coord, ship)
                self.hide_ship(x_coord, y_coord, 1, ship)
                break
                
                           

    def check_coords(self, x_coord:int, y_coord:int, ship:int) -> int:
        '''
        Checks if coordinates are out of bounds for the ship they are trying to place
        
        Returns 1 on success. 0 on failure
        '''
        if (x_coord + ship >= self.board_size 
            or y_coord + ship >= self.board_size): return 0
        return 1

    def check_x_placement(self, x_coord:int, y_coord, ship:int) -> int:
        '''
        Checks if ship placement at specific board point is valid for x 
        oriented placement

        Returns: 1 on success. 0 if placement is invalid
        '''
        for space in range(ship):
            actual_x_coord = x_coord + space
            if (self.actual_board[actual_x_coord][y_coord]): return 0
        return 1

    def check_y_placement(self, x_coord:int, y_coord, ship:int) -> int:
        '''
        Checks if ship placement at specific board point is valid for y 
        oriented placement

        Returns: 1 on success. 0 if placement is invalid
        '''
        for space in range(ship):
            actual_y_coord = y_coord + space
            if (self.actual_board[x_coord][actual_y_coord]): return 0
        return 1


    def hide_ship(self, x_coord:int, y_coord:int, orientation:int, ship:int):
        '''
        Hides ship on gameboard
        '''
        for space in range(ship):
            if (orientation):
                actual_y_coord = y_coord + space
                self.actual_board[x_coord][actual_y_coord] = 1
            else:
                actual_x_coord = x_coord + space
                self.actual_board[actual_x_coord][y_coord] = 1
            
