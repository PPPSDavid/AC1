# A Go Board implemented using matrix
class Go:
    def __init__(self, dimension):
        a = [[0] for i in range(dimension)]
        self.dimension = [a for i in range(dimension)]
        print(self.dimension)

# Called after each move is made, to make all necessary changes after a legal move
    def clean_up (self):
        pass

# Called before each move is made to see whether certain place is legal to be played
    def check_legal (self, coordinate):
        pass

# The main method used to place stones. Uses check_legal and clean_up to ensure legality
    def move (self, coordinate, color):
        if self.dimension[coordinate[0]][coordinate[1]] != 0:
            raise Exception('Place already taken')
        if color:
            self.dimension[coordinate[0]][coordinate[1]] = 1
        else:
            self.dimension[coordinate[0]][coordinate[1]] = -1
