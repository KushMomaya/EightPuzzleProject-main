import heapq as q
from node import Node

# General Search Template
def general_search(initial_state, goal_state, queueing_function):
    nodes = []
    initial_node = Node(state=initial_state)
    q.heappush(nodes, initial_node)

    seen = set()

    while nodes:
        if len(nodes) == 0:
            return "failure"
        
        node = q.heappop(nodes)

        if node.state == goal_state:
            return node
        operators = ["left", "right", "up", "down"]
        neighbors = expand(node, operators)
        nodes = queueing_function(nodes, neighbors)
                                  
# Expand function returns an array of valid neighbors for the node passed in
def expand(node, operators):

# Queueing logic for uniform cost search
def uniform_cost(nodes, neighbors):

# Queueing logic for A* with the manhattan distance heuristic
def astar_manhattan(nodes, neighbors):

# Queueing logic for A* with the misplaced tile heuristic
def astar_misplaced(nodes, neighbors):

# Check the current amount of tiles in the wrong position    
def tile_check(state):
    count = 0
    goal_state = [
        [1,2,3],
        [4,5,6],
        [7,8,0]
    ]
    for i in range(3):
        for j in range(3):
            if state[i,j] != goal_state[i][j]:
                count = count + 1
    
    return count

# Check the total distance of each tile from its current state
def distance_check(state):
