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
from simpleai.search import astar, SearchProblem
import random


#------------------------------------------------------------------------------------------------------------------
#   Problem definition
#------------------------------------------------------------------------------------------------------------------

class jarras(SearchProblem):
    """ Class that is used to define 8-puzzle problem. 
        The states are represented by 2D touples ((a,b,c),(d,e,f),(g,h,i)), where each element is one
        number from 0 to 8. The number 0 indicates the possition of the empty tile.
    """
    
    def __init__(self, initial_state, limits):
        """ 
            This constructor initializes the 8-puzzle problem. 
        
            initial_state: The initial state of the board.
        """
        
        # Call base class constructor (the initial state is specified here).
        SearchProblem.__init__(self, initial_state)

        result = list(initial_state)
        result[1] = result[0]/2
        result[0] = result[0] - result[1]
        # Define goal state.
        self.goal = tuple(result)    
        self.limit = limits   # lista 

    def actions(self, state):
        """ 
            This method returns a list with the possible actions that can be performed according to
            the specified state.

            state: The state to be evaluated.
        """

        ac = list(state)
        actions = []
        for i in range(3):
            for j in range(3):
                if i!=j and ac[i]>0 and ac[j]<self.limit[j]:
                    actions.append([i,j])
        return actions
        
    def result(self, state, action):
        """ 
            This method returns the new state obtained after performing the specified action.

            state: The state to be modified.
            action: The action be perform on the specified state.
        """
        [i,j] = action
        ac = list(state)
        aux_i = ac[i]
        aux_j = ac[j]
        ac[i] = max([0,aux_i+aux_j-self.limit[j]])
        ac[j] = min([self.limit[j],aux_i+aux_j])

        return tuple(ac)
        
    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state: The state to be tested.
        """
        return state == self.goal

    def cost(self, state, action, state2):
        """ 
            This method receives two states and an action, and returns
            the cost of applying the action from the first state to the
            second state.

            state: The initial state.
            action: The action used to generate state2.
            state2: The state obtained after applying the specfied action.
        """
        return 1

    def heuristic(self, state):
        """ 
            This method returns an estimate of the distance from the specified state to 
            the goal.

            state: The state to be evaluated.
        """

        ac = list(state)
        sum = ac[1]+ac[2]
        sum = sum - self.limit[0]/2
        sum = abs(sum)

        return sum

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------

# Initialize board
initial_board = (8,0,0)
limite = [8,5,3]

# Solve problem
result = astar(jarras(initial_board,limite), graph_search=True)

# Print results
for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('After moving', action, 'into the empty space. Goal achieved!')
    else:
        print('After moving', action, 'into the empty space')

    print(state)

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
