#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    
    
    def __init__(self, depth_limit):
        """ an attribute states for the Searcher‘s list of untested states; it should be initialized to an empty list
            an attribute num_tested that will keep track of how many states the Searcher tests; it should be initialized to 0
            an attribute depth_limit that specifies how deep in the state-space search tree the Searcher will go, -1 indicates that the Searcher does not use a depth limit
            input: depth_limit is an integer
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def add_state(self, new_state):
        """ add a single State object to the Searcher‘s list of untested states
            input: new_statea is a single State object  
        """
        self.states += [new_state]
        
    def should_add(self, state):
        """ returns True if the called Searcher should add state to its list of untested states, and False otherwise.
            the Searcher has a depth limit (i.e., its depth limit is not -1) and state is beyond the depth limit (i.e., the number of moves used to get to state is greater than the depth limit)
            state creates a cycle in the search
            input: state is a state object
        """
        if self.depth_limit!=-1 and state.num_moves>self.depth_limit:
            return False
        elif state.creates_cycle()==True:
            return False
        else:
            return True
            
    def add_states(self, new_states):
        """ If a given state s should be added to the Searcher‘s list of untested states (because s would not cause a cycle and is not beyond the Searcher‘s depth limit), add s to the list of untested states.
            If a given state s should not be added to the Searcher object’s list of states, the method should ignore the state.
            input: new_states is a list of State object
        """
        for s in new_states:
            if self.should_add(s)==True:
                self.add_state(s)
            else:
                None
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        """ performs a full state-space search that begins at the specified initial state init_state and ends when the goal state is found or when the Searcher runs out of untested states
            input: init_state is a beginning state
        """
        self.add_state(init_state)
        while self.states != []:
            
            s = self.next_state()
            self.num_tested+=1
            if s.is_goal():
                return s
            else: 
                self.add_states(s.generate_successors())
                
        return None

### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    """ choosing one the untested states that has the smallest depth
    """
    

        
    def next_state(self):
        """ overrides the next_state method that is inherited from Searcher
            follow FIFO (first-in first-out) ordering – choosing the state that has been in the list the longest
            remove the chosen state from the list of untested states before returning it
            input: no inputs
        """
        longest = self.states[0]
        self.states.remove(longest)
        return longest
    
class DFSearcher(Searcher):
    """ choosing one the untested states that has the largest depth
    """

        
    def next_state(self):
        """ overrides the next_state method that is inherited from Searcher
            follow LIFO (last-in first-out) ordering – choosing the state that was most recently added to the list.
            remove the chosen state from the list of untested states before returning it
            input: no inputs
        """
        newest = self.states[-1]
        self.states.remove(newest)
        return newest
        



def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    """ returns an estimate of how many additional moves are needed to get from state to the goal state
        input: state is a state object
    """
    return state.board.num_misplaced()

def h2(state):
    """ return the index difference (both col and row) between the goal state and the current state
        input: state is a state object
    """
    return state.board.row_col_difference()
    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        the moves that need to be taken to reach the goal state
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        """ attributes inherited from Searcher
            self.heuristic is used to store a reference to the heuristic function used by the searcher
            input: heuristic is whatever value is passed in for the heuristic parameter
        """
        super().__init__(self)
        self.depth_limit = -1
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        """ overrides the add_state method that is inherited from Searcher
            the method should add a sublist that is a [priority, state] pair to the untested states, where priority is the priority of state that is determined by calling the priority method
            input: state is a state object
        """
        self.states+=[[self.priority(state), state]]
        
    def next_state(self):
        """ overrides the next_state method that is inherited from Searcher
            choose one of the states with the highest priority
            input: no inputs
        """
        highest = max(self.states)
        self.states.remove(highest)
        return highest[-1]
        


    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """ inherited from the GreedySearch class
        include the prior num_moves and the moves that need to be taken to reach the goal state
    """
        
    def priority(self, state):
        """ similar to GreedySearch's priority, but it takes into account the cost that has already been expended to get to that state 
            input: state is a state object
        """
        return -1 * (self.heuristic(state) + state.num_moves)
        
    





























