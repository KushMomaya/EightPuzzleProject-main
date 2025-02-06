from algo import *

depth0 = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

depth2 = [
    [1,2,3],
    [4,5,6],
    [0,7,8]
]

depth4 = [
    [1,2,3],
    [5,0,6],
    [4,7,8]
]

depth8 = [
    [1,3,6],
    [5,0,2],
    [4,7,8]
]

depth12 = [
    [1,3,6],
    [5,0,7],
    [4,8,2]
]

depth16 = [
    [1,6,7],
    [5,0,3],
    [4,8,2]
]

depth20 = [
    [7,1,2],
    [4,8,5],
    [6,3,0]
]

depth24 = [
    [0,7,2],
    [4,6,1],
    [3,5,8]
]

def main():
    #choose which puzzle to solve
    print("Select which depth puzzle you want to solve -> [0,2,4,8,12,16,20,24] ")
    choice = input().strip()
    #store goal state
    goal_state = [
        [1,2,3],
        [4,5,6],
        [7,8,0]
    ]

    if choice == "0":
        initial_state = depth0
    elif choice == "2":
        initial_state = depth2
    elif choice == "4":
        initial_state = depth4
    elif choice == "8":
        initial_state = depth8
    elif choice == "12":
        initial_state = depth12
    elif choice == "16":
        initial_state = depth16
    elif choice == "20":
        initial_state = depth20
    elif choice == "24":
        initial_state = depth24
    #pick algorithm to use
    print("Select which algorithm to use: 1 = Uniform Cost, 2 = A* Misplaced Tile, 3 = A* Manhattan Distance")
    algo_choice = input().strip()
    #run algorithm with initial state
    if algo_choice == "1":
        general_search(initial_state, goal_state, uniform_cost)
    elif algo_choice == "2":
        general_search(initial_state, goal_state, astar_misplaced)
    elif algo_choice == "3":
        general_search(initial_state, goal_state, astar_manhattan)
    else:
        print("Invalid Input")
    #some display of solution

main()