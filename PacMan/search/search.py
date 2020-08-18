# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def graphSearch(problem, fringe):
    
    startState = problem.getStartState()
    fringe.push([(startState, 'Start', 0)]) #getSuccessors returns a list in format ( nextState, action, cost), so we create that for start and push it to fringe

    try:
        startState._hash_()
        visited = set()
    except:
        visited = list()

    while not fringe.isEmpty():
        nodes = fringe.pop()
        currentNode = nodes[-1][0] #fringe will be filled with (successor, action, stepCost) values by getSuccesors(), successor being a node
        #have -1 because in python the negative means start from end so -1 would grab last thing
        
        if problem.isGoalState(currentNode): #want to see if we reached goal before we check an available paths             
            return [x[1] for x in nodes][1:] # want to skip start nodes since we are at it, want directions
            # in teachers version above returns node.path
        
        if currentNode not in visited: 
            visited.append(currentNode)
            
            for childNode in problem.getSuccessors(currentNode):
                if childNode[0] not in visited: # don't want to add nodes to fringe that we already visited.  MAY NEED TO REMOVE NOT SURE YET
                    holder = nodes[:] #want to store information of node we are currently at before moving onto it's child
                    holder.append(childNode)
                    fringe.push(holder)
                   
    
    return False #is run if we can not reach goal from current start point


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """
    stack = util.Stack()   
    return graphSearch(problem, stack) 

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()
    return graphSearch(problem, queue)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    actionsCost = lambda nodes: problem.getCostOfActions( [x[1] for x in nodes][1:])
    #stores an anonymous function in actionsCost which get the total cost of going from start node to current node we are looking at.
    
    priorityQueue = util.PriorityQueueWithFunction(actionsCost)#since we need a function, we call this method which will used a util.PriorityQueue
    return graphSearch(problem, priorityQueue)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    # uniform search calculate cost of path so far while greedy cares about the sort of now
    actionsCost = lambda nodes: problem.getCostOfActions( [x[1] for x in nodes][1:]) + heuristic(nodes[-1][0], problem)
    #stores an anonymous function in actionsCost which get the total cost of going from start node to current node we are looking at along with actual cost of node.
    
    priorityQueue = util.PriorityQueueWithFunction(actionsCost)
    return graphSearch(problem, priorityQueue)
   


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
