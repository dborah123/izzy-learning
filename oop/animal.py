class Animal:
    # Attributes
    num_legs = 0
    is_mammal = False

    # Constructors
    def __init__(self, num_legs:int) -> None:
        self.num_legs = num_legs

    # Methods
    def get_num_legs(self) -> int:
        return self.num_legs



class Dog(Animal):
    # Attributes
    breed = ""

    # Contructors
    def __init__(self, num_legs:int, breed:str) -> None:
        super().__init__(num_legs)
        self.breed = breed

    # Methods
    def get_breed(self):
        return self.breed
