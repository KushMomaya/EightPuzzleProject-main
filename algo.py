import heapq as q
from node import Node
import time

# General Search Template
def general_search(initial_state, goal_state, queueing_function):
    start = time.time() # Keep track of time

    #Initial Queue Setup
    nodes = []
    initial_node = Node(state=initial_state)
    q.heappush(nodes, initial_node)

    #Informational Variables
    expanded_nodes = 0
    max_q_size = 0
    frontier = 1

    seen = set() # Keep track of repeated states

    while nodes:
        if len(nodes) == 0:
            return "failure"

        #Update Information
        max_q_size = max(max_q_size, len(nodes))
        node = q.heappop(nodes)
        frontier = len(nodes)

        if node.state == goal_state:
            end = time.time()
            #print("Nodes Expanded: " + str(expanded_nodes))
            #print("Maximum Queue Size: " + str(max_q_size))
            #print("Frontier: " + str(frontier))
            #print("Depth: " + str(node.cost))
            #print("Time Taken: " + str(end - start))
            #print(node.state) check correct answer output
            return node, expanded_nodes, max_q_size, node.cost, end - start
            
        # Needs to be immutable to be added to the set
        state = tuple(tuple(row) for row in node.state)

        operators = ["left", "right", "up", "down"]

        if state not in seen:
            seen.add(state)
            expanded_nodes += 1
            neighbors = expand(node, operators)
            for neighbor in neighbors:
                neighbor_check = tuple(tuple(row) for row in neighbor.state)
                if neighbor_check not in seen:
                    queueing_function(nodes, neighbor)
                    #debug code for tracing
                    #print("curr: ", len(nodes))
                    #print("currnode: ", neighbor.state, neighbor.cost)
                                  
# Expand function returns an array of valid neighbors for the node passed in
def expand(node, operators):
    neighbors = []
    r, c = -1, -1
    for i in range(3):
        for j in range(3):
            if node.state[i][j] == 0:
                r = i # Row coordinate for blank
                c = j # Column coordinate for blank
    
    #find neighbors from r,c position and remeber to store the states of the new ones
    for k in operators:
        new_r, new_c = r, c
        if k == "left" and c > 0:
            new_c = c - 1
        elif k == "right" and c < 2:
            new_c = c + 1
        elif k == "up" and r > 0:
            new_r = r - 1
        elif k == "down" and r < 2:
            new_r = r + 1
        else:
            continue
        new_state = [row[:] for row in node.state]
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
            if state[i][j] != goal_state[i][j]:
                count = count + 1
    
    return count

# Check the total distance of each tile from its current state
def distance_check(state):
    static = {
        1: (0,0), 2: (0,1), 3: (0,2),
        4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 0: (2,2)
    }
    distance = 0
    for i in range(3):
        for j in range(3):
            curr = state[i][j]
            if curr != 0:
                goalx, goaly = static[curr]
                distance += abs(goalx - i) + abs(goaly - j)
    return distance