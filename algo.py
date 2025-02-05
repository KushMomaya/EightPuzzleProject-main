import heapq as q
from node import Node

# General Search Template
def general_search(initial_state, goal_state, queueing_function):
    nodes = []
    initial_node = Node(state=initial_state)
    q.heappush(nodes, initial_node)
    expanded_nodes = 0
    max_q_size = 0
    seen = set()

    while nodes:
        if len(nodes) == 0:
            return "failure"

        max_q_size = max(max_q_size, len(nodes))
        node = q.heappop(nodes)
        expanded_nodes += 1

        if node.state == goal_state:
            return node

        seen.add()
        operators = ["left", "right", "up", "down"]
        neighbors = expand(node, operators)
        for neighbor in neighbors:
            if not in seen:
                nodes = queueing_function(nodes, neighbor)
                                  
# Expand function returns an array of valid neighbors for the node passed in
def expand(node, operators):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if node.state[i][j] == 0:
                r = i # Row coordinate for blank
                c = j # Column coordinate for blank
    
    #find neighbors from r,c position and remeber to store the states of the new ones
    for k in operators:
        if k == "left":
            if 0 < c <= 2:
                new_r = r
                new_c = c - 1
        elif k == "right":
            if 0 <= c < 2:
                new_r = r
                new_c = c + 1
        elif k == "up":
            if 0 < r <= 2:
                new_r = r - 1
                new_c = c
        elif k == "down":
            if 0 <= c < 2:
                new_r = r + 1
                new_c = c
        
        new_state = node.state
        new_state[r][c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[r][c]
        neighbor = Node(state= new_state, cost= node.cost + 1)
        neighbors.append(neighbor)
    
    return neighbors

# Queueing logic for uniform cost search
def uniform_cost(nodes, node):
    node.heuristic = 0 # No heuristic for uc search
    node.f = node.cost
    q.heappush(nodes, node) # Pushing onto priority queue uses overrided less than operator for comparison
# Queueing logic for A* with the manhattan distance heuristic
def astar_manhattan(nodes, node):
    node.heuristic = distance_check(node.state)
    node.f = node.cost + node.heuristic
    q.heappush(nodes, node) # Pushing onto priority queue uses overrided less than operator for comparison
# Queueing logic for A* with the misplaced tile heuristic
def astar_misplaced(nodes, node):
    node.heuristic = tile_check(node.state)
    node.f = node.cost + node.heuristic
    q.heappush(nodes, node) # Pushing onto priority queue uses overrided less than operator for comparison
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
