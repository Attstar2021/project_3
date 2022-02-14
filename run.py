from random import randint

scores = {"computer": 0, "player": 0}


class Board:
    """
    Main board class. which contain and sets board size the number of ships
     the players name and board type(player board or computer)
     Has methods for adding ships and gueses and printing the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))


    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "^"
            return "Hit"
        else:
            return "Miss"


    def add_ship():


    def random_point():

    
    def valid_corordinates():


    def populate_board():


    def make_guess():


    def play_game():


    def new_game():
        """
        This is to start a new game, to sets the board size and number of ships,
        resets the scores and initialises the boards
        """
        size = 5
        num_ships = 3
        scores["computer"] = 0
        scores["player"] = 0



    new_game()



    


    



