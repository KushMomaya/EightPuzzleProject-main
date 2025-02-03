import heapq as q
from node import Node


def general_search(initial_state, queueing_function):
    nodes = []
    initial_node = Node(state=initial_state)
    q.heappush(nodes, initial_node)

    while nodes:
        if len(nodes) == 0:
            return "failure"
        
        node = q.heappop(nodes)

        #if check goal state
            #then return node
        neighbors = #expand(node, operators)
        nodes = queueing_function(nodes, #neighbors)
                                  

def expand(node, operators):

def uniform_cost(nodes, neighbors):

def astar_manhattan(nodes, neighbors):

def astar_misplaced(nodes, neighbors):

def tile_check(state):

def distance_check(state):
