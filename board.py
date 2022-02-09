#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Yin-Ching Lee
# email: leewill@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        
        for num_r in range(3):
            for num_c in range(3):
                self.tiles[num_r][num_c] = digitstr[3*num_r+num_c]
        
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[0])):
                if self.tiles[x][y]=='0':
                    self.blank_r = x
                    self.blank_c = y


    ### Add your other method definitions below. ###
    
    def __repr__(self):
        """ returns a string representation of a Board object
            input: no inputs
            change the 0 to a _
        """
        board = ''
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[0])):
                if y==2:
                    board += self.tiles[x][y] + ' ' + '\n'
                else:
                    board += self.tiles[x][y] + ' '
                    
        
        return board.replace('0','_')
    
    def move_blank(self, direction):
        """ return True or False to indicate whether the requested move was possible
            make changes to the board object according to the direction input
            input: direction can have one of the following four values (strings): 'up', 'down', 'left', 'right'
        """
        next_r = 0
        next_c = 0
        if direction == 'up':
            next_r = self.blank_r-1
            next_c = self.blank_c
        elif direction == 'down':
            next_r = self.blank_r+1
            next_c = self.blank_c
        elif direction == 'left':
            next_r = self.blank_r
            next_c = self.blank_c-1
        elif direction == 'right':
            next_r = self.blank_r
            next_c = self.blank_c+1
        
        if next_r in range(3) and next_c in range(3) and direction in ['up', 'down', 'left', 'right']:
            self.tiles[self.blank_r][self.blank_c]=self.tiles[next_r][next_c]
            self.tiles[next_r][next_c]='0'
            self.blank_r = next_r
            self.blank_c = next_c
            return True
        else:
            return False
        
    def digit_string(self):
        """ returns a string of digits that corresponds to the current contents of the called Board object’s tiles attribute
            input: no inputs
        """
        string = ''
        for x in range(3):
            for y in range(3):
                string+=self.tiles[x][y]
        return string
    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy of the called object
            input: no inputs
        """
        Copy_Board = Board(self.digit_string())
        return Copy_Board
        
    def num_misplaced(self):
        """ returns the number of tiles in the called Board object that are not where they should be in the goal state
            doesn't include the blank cell in this count even if it’s not where it should be in the goal state
            input: no inputs
        """
        value = 0
        correct = '012345678'
        for x in range(len(self.digit_string())):
            if self.digit_string()[x] != correct[x] and self.digit_string()[x]!= '0':
                value+=1
        return value
            
    
    def __eq__(self, other):
        """ return True if the called object (self) and the argument (other) have the same values for the tiles attribute, and False otherwise.
            input: other is another borad object
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False
        
    def row_col_difference(self):
        """ return the index difference (both col and row) between the goal state and the current state
            input: no inputs
        """
        diff = 0
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[0])):
                if self.tiles[x][y]=='1':
                    diff += abs(0-x)+abs(1-y)
                elif self.tiles[x][y]=='2':
                    diff += abs(0-x)+abs(2-y)
                elif self.tiles[x][y]=='3':
                    diff += abs(1-x)+abs(0-y)
                elif self.tiles[x][y]=='4':
                    diff += abs(1-x)+abs(1-y)
                elif self.tiles[x][y]=='5':
                    diff += abs(1-x)+abs(2-y)
                elif self.tiles[x][y]=='6':
                    diff += abs(2-x)+abs(0-y)
                elif self.tiles[x][y]=='7':
                    diff += abs(2-x)+abs(1-y)
                elif self.tiles[x][y]=='8':
                    diff += abs(2-x)+abs(2-y)
        return diff
                    
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        