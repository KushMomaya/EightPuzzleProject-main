class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.cost = cost # Cost of a node in uniform cost search
        self.heuristic = heuristic # Heuristic: distance of the current node to the goal state
        self.f = cost + heuristic # g(n) + h(n), comparing the cost of the node with the distance to reach the goal state to decide where to expand


    # Override the less than operator (<) so I can directly compare the f value of nodes when deciding where to go
    def __lt__(self, other):
        return self.f < other.f