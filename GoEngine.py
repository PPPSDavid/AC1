# A Go Board implemented using matrix
class Go:

    # Initialize a Go game on a square board with size D
    def __init__(self, dimension):
        a = [[0] for i in range(dimension)]
        self.board = [a for i in range(dimension)]
        # print(self.board)

    # Get the adjacent blocks (up down left right) coordinate within a legal board
    def get_neighbor (self,coordinate):
        lst = []
        x = coordinate[0]
        y = coordinate[1]
        if x != 0 :
            lst.append([x-1,y])
        if x != len(self.board) :
            lst.append([x + 1, y])
        if y != 0:
                lst.append([x, y-1])
        if y != len(self.board):
                lst.append([x, y+1])
        return lst

    # Get the stone on a certain coordinate
    def get_stone (self, coordinate):
        poi = self.board[coordinate[0]][coordinate[1]]
        return poi

    # Get the dimension of this current Go game
    def get_dimension (self):
        return len(self.board)

    class Cluster:
        def __init__(self):
            self.unfinished = set()
            self.member = set()
            self.air_block = set()
            self.color = 0

        def rec_construct (self):
            if len(self.unfinished) == 0 :
                return
            else :
                poi = self.unfinished[0]
                color = self.color
                for new_pos in Go.get_neighbor(poi):
                    new_stone = Go.get_stone(new_pos)
                    if new_stone == 0:
                        self.air_block.add(new_stone)
                    elif new_stone == color:
                        self.unfinished.add(new_stone)
                    else:
                        pass
                self.unfinished.remove(poi)
                self.member.add(poi)

        def start_cluster(self, coordinate):
            self.unfinished.add(coordinate)
            self.color = Go.get_stone(coordinate)
            self.rec_construct()

        def get_cluster_air(self):
            len(self.air_block)

        def get_cluster_size(self):
            len(self.member)

# Called after each move is made, to make all necessary changes after a legal move
    def clean_up (self):
        pass

# Called before each move is made to see whether certain place is legal to be played
    def check_legal (self, coordinate):
        x = coordinate[0]
        y = coordinate[1]
        
        if self.dimension[x][y] != 0:
            return False
        
        elif x == 0 or y == 0 or x == len(self.dimension[0]) or y == len(self.dimension[0]):
            pass
        elif  x < 0 or y < 0 or x > len(self.dimension[0]) or y > len(self.dimension[0]):
            pass
        else:
            pass

# The main method used to place stones. Uses check_legal and clean_up to ensure legality
    def move (self, coordinate, color):
        if self.board[coordinate[0]][coordinate[1]] != 0:
            raise Exception('Place already taken')
        if color:
            self.board[coordinate[0]][coordinate[1]] = 1
        else:
            self.board[coordinate[0]][coordinate[1]] = -1
