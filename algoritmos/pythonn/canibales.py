#------------------------------------------------------------------------------------------------------------------
#   8-puzzle solver using the A* algorithm
#
#   This code is an adaptation of the 8-puzzle solver described in:
#   Artificial intelligence with Python. Alberto Artasanchez and Prateek Joshi. 2nd edition, 2020, 
#   editorial Pack. Chapter 10.
#
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------
import sys
sys.stdin = open('file.in', 'r')
sys.stdout = open('file.out', 'w')
from simpleai.search import astar, SearchProblem, breadth_first
import random

#------------------------------------------------------------------------------------------------------------------
#   Problem definition
#------------------------------------------------------------------------------------------------------------------

class canibal(SearchProblem):
    """ Class that is used to define 8-puzzle problem. 
        The states are represented by 2D touples ((a,b,c),(d,e,f),(g,h,i)), where each element is one
        number from 0 to 8. The number 0 indicates the possition of the empty tile.
    """
    
    def __init__(self, initial_state):
        """ 
            This constructor initializes the 8-puzzle problem. 
        
            initial_state: The initial state of the board.
        """
        
        # Call base class constructor (the initial state is specified here).
        SearchProblem.__init__(self, initial_state)

        # Define goal state.
        self.goal = ((3,3,0))        

    def actions(self, state):
        """ 
            This method returns a list with the possible actions that can be performed according to
            the specified state.

            state: The state to be evaluated.
        """
        if state == tuple([3,3,1]):
            actions = [[1,1,0],[0,2,0],[0,1,0]]
        if state == tuple([3,2,1]):
            actions = [[0,2,0],[0,3,0],[1,1,0]]
        if state == tuple([3,1,1]):
            actions = [[2,2,0],[0,3,0]]
        if state == tuple([0,3,1]):
            actions = [[3,1,0],[3,2,0]]
        if state == tuple([0,2,1]):
            actions = [[3,2,0],[3,3,0]]
        if state == tuple([0,1,1]):
            actions = [[3,3,0]]
        if state == tuple([1,1,1]):
            actions = [[3,3,0],[3,2,0]]
        if state == tuple([2,2,1]):
            actions = [[2,2,0],[3,1,0]]
        

        if state == tuple([3,3,0]):
            actions = [[1,1,1],[0,2,1],[0,1,1]]
        if state == tuple([3,2,0]):
            actions = [[0,2,1],[0,3,1],[1,1,1]]
        if state == tuple([3,1,0]):
            actions = [[2,2,1],[0,3,1]]
        if state == tuple([0,3,0]):
            actions = [[3,1,1],[3,2,1]]
        if state == tuple([0,2,0]):
            actions = [[3,2,1],[3,3,1]]
        if state == tuple([0,1,0]):
            actions = [[3,3,1]]
        if state == tuple([1,1,0]):
            actions = [[3,3,1],[3,2,1]]
        if state == tuple([2,2,0]):
            actions = [[2,2,1],[3,1,1]]
        

        return actions
        
    def result(self, state, action):
        """ 
            This method returns the new state obtained after performing the specified action.

            state: The state to be modified.
            action: The action be perform on the specified state.
        """
        # Swap values
        return tuple(action)
        
    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state: The state to be tested.
        """
        return state == self.goal

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------

# Initialize board
initial_board = tuple([3,3,1])

# Solve problem
result = breadth_first(canibal(initial_board), graph_search=False)

# Print results
for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('After moving', action, 'Goal achieved!')
    else:
        print('After moving', action)

    print(state)

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
