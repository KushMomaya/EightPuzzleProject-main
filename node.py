class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action # Which way to move
        self.cost = cost # Cost of a node in uniform cost search
        self.heuristic = heuristic # Heuristic: distance of the current node to the goal state
        self.f = cost + heuristic # g(n) + h(n), comparing the cost of the node with the distance to reach the goal state to decide where to expand

    