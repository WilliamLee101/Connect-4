#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()


def process_file(filename, algorithm, param):
    """ open the file with the specified filename for reading, and it should use a loop to process the file one line at a time
        report the number of moves in the solution, and the number of states tested during the search for a solution
        print strings that have the informations of the number of puzzles solved, the average number of moves in the solutions, and the average number of states tested
        
        input: a string filename specifying the name of a text file in which each line is a digit string for an eight puzzle. 
               a string algorithm that specifies which state-space search algorithm should be used to solve the puzzles ('random', 'BFS', 'DFS', 'Greedy', or 'A*')
               a third input param that allows you to specify a parameter for the searcher – either a depth limit (for the uninformed search algorithms) or a choice of heuristic function (for the informed search algorithms)
    """
    file = open(filename)
    loop = 0
    total_moves = 0
    total_states = 0
    for line in file:
        line = line[:-1]
        searcher = create_searcher(algorithm, param)
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        
        
        soln = None
        try:
            soln = searcher.find_solution(init_state)
            if soln == None:
                print(line + ':','no solution')
            else:
                print(line + ':', soln.num_moves, 'moves,', searcher.num_tested, 'states tested')
                loop += 1
                total_moves += soln.num_moves
                total_states += searcher.num_tested
        except KeyboardInterrupt:
            print(line + ': search terminated, ', end='')
            print('no solution')
          
    print()
    if loop != 0:
        print('solved '+ str(loop) + ' puzzles')
        print('averages: ' + str(total_moves/loop) + ' moves, ' + str(total_states/loop) + ' states tested')
    else:
        print('solved '+ str(loop) + ' puzzles')
        
    






















