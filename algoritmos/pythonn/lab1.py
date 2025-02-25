#------------------------------------------------------------------------------------------------------------------
#  Laberinto
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
#   Auxiliar functions
#------------------------------------------------------------------------------------------------------------------

def printea(board, action, goal):
    """
    printea el tablero
    """

    for i, row in enumerate(board):
        if(i==action[0]):
            row[action[1]]= 'O'
        if(i==goal[0]):
            row[goal[1]]= 'X'
        for j in row:
            print(j, end='')
        print()


#------------------------------------------------------------------------------------------------------------------
#   Problem definition
#------------------------------------------------------------------------------------------------------------------

tablero = [['+','+','+','+','+','+','+','+','+','+',' ',' ',' ',' ',' ',' ','+','+','+','+','+','+'],
                        ['+',' ',' ',' ','+',' ',' ',' ','+','+',' ','+','+',' ',' ',' ',' ',' ',' ',' ',' ','+'],
                        ['+',' ',' ',' ',' ',' ','+',' ',' ',' ',' ',' ','+','+','+','+','+',' ','+',' ','+','+'],
                        [' ',' ',' ',' ',' ',' ',' ','+','+',' ',' ','+','+','+','+',' ','+','+','+',' ',' ','+'],
                        ['+',' ',' ',' ',' ',' ','+',' ','+',' ','+','+',' ',' ','+',' ',' ','+','+','+',' ','+'],
                        ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+','+',' ','+','+','+',' ',' ','+',' ','+'],
                        ['+','+','+','+','+',' ','+',' ','+',' ',' ',' ',' ',' ','+','+','+',' ',' ','+',' ','+'],
                        ['+','+','+','+','+',' ','+','+','+',' ',' ','+','+','+','+','+','+','+',' ',' ',' ','+'],
                        ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+',' ','+','+',' ','+',' ','+',' ',' ','+'],
                        ['+','+',' ',' ',' ',' ',' ',' ',' ','+',' ','+',' ','+','+',' ',' ',' ',' ',' ',' ','+'],
                        ['+','+','+','+','+','+','+',' ',' ',' ',' ',' ',' ','+','+','+','+','+','+','+','+','+']]

class laberinto(SearchProblem):
    
    def __init__(self, initial_state, goal):
        """ 
       Se definen estados iniciales y finales
        """
        
        # Call base class constructor (the initial state is specified here).
        SearchProblem.__init__(self, initial_state)
        # Define goal state.
        self.goal = tuple(goal)     
        # 11 por 22
        self.size = [11,22]
        self.tablero = [['+','+','+','+','+','+','+','+','+','+',' ',' ',' ',' ',' ',' ','+','+','+','+','+','+'],
                        ['+',' ',' ',' ','+',' ',' ',' ','+','+',' ','+','+',' ',' ',' ',' ',' ',' ',' ',' ','+'],
                        ['+',' ',' ',' ',' ',' ','+',' ',' ',' ',' ',' ','+','+','+','+','+',' ','+',' ','+','+'],
                        [' ',' ',' ',' ',' ',' ',' ','+','+',' ',' ','+','+','+','+',' ','+','+','+',' ',' ','+'],
                        ['+',' ',' ',' ',' ',' ','+',' ','+',' ','+','+',' ',' ','+',' ',' ','+','+','+',' ','+'],
                        ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+','+',' ','+','+','+',' ',' ','+',' ','+'],
                        ['+','+','+','+','+',' ','+',' ','+',' ',' ',' ',' ',' ','+','+','+',' ',' ','+',' ','+'],
                        ['+','+','+','+','+',' ','+','+','+',' ',' ','+','+','+','+','+','+','+',' ',' ',' ','+'],
                        ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','+',' ','+','+',' ','+',' ','+',' ',' ','+'],
                        ['+','+',' ',' ',' ',' ',' ',' ',' ','+',' ','+',' ','+','+',' ',' ',' ',' ',' ',' ','+'],
                        ['+','+','+','+','+','+','+',' ',' ',' ',' ',' ',' ','+','+','+','+','+','+','+','+','+']]

    def actions(self, state):
        """ 
        Devuelve la lista de posiciones a las que podemos llegar
        """

        [i,j] = list(state)
        actions = []
        if i > 0 and self.tablero[i-1][j]==' ':
            actions.append([i - 1, j])
        if i < 10 and self.tablero[i+1][j]==' ':
            actions.append([i + 1, j])
        if j > 0 and self.tablero[i][j-1]==' ':
            actions.append([i, j - 1])
        if j < 21 and self.tablero[i][j + 1]==' ':
            actions.append([i, j + 1])
        return actions
        
    def result(self, state, action):
        """ 
        Se actualiza el estado actual
        """

        return tuple(action)
        
    def is_goal(self, state):
        """ 
        Se comprueba si se llegó a la meta
        """
        return state == self.goal

    def cost(self, state, action, state2):
        """ 
        Costo por transición
        """
        return 1

    def heuristic(self, state):
        """ 
        Distancia euclidiana del estado actual al objetivo al cuadrado
        """
        ac = list(state)
        distance = (self.goal[0]-ac[0])**2 + (self.goal[1]-ac[1])**2
        return distance

#------------------------------------------------------------------------------------------------------------------
#   Program
#------------------------------------------------------------------------------------------------------------------

# Initialize board
initial_pos = (1,2)
goal = (9,19)

# Solve problem
result = astar(laberinto(initial_pos, goal), graph_search=True)

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
    printea(tablero, list(state), list(goal))

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
