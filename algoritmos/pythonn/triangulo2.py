#------------------------------------------------------------------------------------------------------------------
#   Triángulo mágico
#------------------------------------------------------------------------------------------------------------------

from simpleai.search import SearchProblem, breadth_first, depth_first
import sys
sys.stdin = open('file.in', 'r')
sys.stdout = open('file.out', 'w')
#------------------------------------------------------------------------------------------------------------------
#   Auxiliar functions
#------------------------------------------------------------------------------------------------------------------

def find_empty_space(state):
    """
       encuentra el primer 0     
    """
    for i, item in enumerate(state):
        if item == 0:
            return i
    return -1

def printea(state):
    estado = list(state)
    print("   ", estado[0],"   ")
    print(" ", estado[1]," ",estado[2]," ")
    print(estado[3]," ",estado[4]," ", estado[5])


#------------------------------------------------------------------------------------------------------------------
#   Problem definition
#------------------------------------------------------------------------------------------------------------------

class triangulo(SearchProblem):
    """ Class that is used to define the missionaries and cannibals problem. 
        The states are represented by tuples (a, b, c, d, e), where a is the number of missionaries 
        on the left side, b is the number of cannibals on the left side, c is the number of 
        missionaries on the right side, d is the number of cannibals on the right side, 
        and e is the position of the raft (L or R).
    """

    def __init__(self):
        """ Class constructor. It initializes the problem with 3 missionaries and 3 cannibals
            at one side of the river. 
        """
        
        # Call base class constructor (the initial state is specified here).
        SearchProblem.__init__(self, (0,0,0,0,0,0))

    def actions(self, state):
        """ 
            This method returns a list with the possible actions that can be performed according to
            the specified state.

            state: The state to be evaluated.
        """
        act = []
        pos = find_empty_space(state)
        if pos == -1:
            return act

        for i in range(6):
            if list(state).count(i+1)==0:
                temp = list(state)
                temp[pos] = i+1
                act.append(temp)
        return act

    def result(self, state, action):
        """ 
            This method returns the new state obtained after performing the specified action.

            state: The state to be modified.
            action: The action be perform on the specified state.
        """
        
        return tuple(action)

    def is_goal(self, state):
        """ 
            This method evaluates whether the specified state is the goal state.

            state: The state to be tested.
        """
        estado = list(state)
        sum_1 = estado[0] + estado[1] + estado[3]
        sum_2 = estado[0] + estado[2] + estado[5]
        sum_3 = estado[3] + estado[4] + estado[5]
        nums = estado.count(0)
        return (nums==0) and sum_1 == 10 and sum_2 == 10 and sum_3 == 10

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------

# Solve problem
result = depth_first(triangulo(), graph_search=False)
#help(breadth_first)

# Print results

for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('After moving', action, 'Goal achieved!')
    else:
        print('After moving', action)

    printea(state)

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------