


class Array2d:
    # Attributes
    x = 0
    y = 0
    array = []

    # Constructors
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.array = [0 for _ in range(x * y)]

        
    # Methods
    """
    Methods to implement:

    - get:            \PARAMS: x value, y value; \RETURNS: value at that position
    - change:         \PARAMS: x value, y value, new value; \RETURNS: nothing
    - print:          \PARAMS: none; \RETURNS: none; prints a formatted, rectangular representation 
                      of the 2D array
    - check_indices:  \PARAMS: x value, y value; \RETURNS: boolean or 0/1's; helper function to 
                      make sure user is inputting valid indices

    Other challenges:
    - Make another constructor: Takes in an extra param which is a value to place at every space in 2D array
    - Add linear algebra functions
        - add: param: another array2d to add together and returns a new array
        - subtract
        - multiply: more difficult
    - Allow for negative values to be inputted into list (ie. -1 for x would lead to last
      array in array2d 
    """

    def get(self, x:int, y:int) -> int:
        '''
        Returns value located at array2d[x][y]
        '''
        if (self.check_indices(x, y)):
            raise ValueError(f"array2d[{x}][{y}] is invalid: indices out of bounds")

        

    def check_indices(self, x, y):
        '''
        Checks to see if indices are valid
        '''
        if (x >= self.x): return 1
        if (y >= self.y): return 1
        if (x < 0): return 1
        if (y < 0): return 1
        return 0
        

