from algo import *
from node import Node
import matplotlib.pyplot as plt

goal_state = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

puzzles = [
    [
        [1,2,3],
        [4,5,6],
        [7,8,0]
    ],

    [
        [1,2,3],
        [4,5,6],
        [7,0,8]
    ],

    [
        [1,2,3],
        [4,5,6],
        [0,7,8]
    ],

    [
        [1,2,3],
        [0,5,6],
        [4,7,8]
    ],

    [
        [1,2,3],
        [5,0,6],
        [4,7,8]
    ],

    [
        [1,0,3],
        [5,2,6],
        [4,7,8]
    ],

    [
        [0,1,3],
        [5,2,6],
        [4,7,8]
    ],

    [
        [1,3,6],
        [5,2,0],
        [4,7,8]
    ],

    [
        [1,3,6],
        [5,0,2],
        [4,7,8]
    ],

    [
        [1,3,6],
        [5,0,7],
        [4,8,2]
    ],

    [
        [1,6,7],
        [5,0,3],
        [4,8,2]
    ],

    [
        [7,1,2],
        [4,8,5],
        [6,3,0]
    ],

    [
        [0,7,2],
        [4,6,1],
        [3,5,8]
    ],

    [
        [8, 6, 7],
        [2, 5, 4],
        [3, 0, 1]
    ]
]

depths = [] #Store depths
uc_exp, mt_exp, md_exp = [], [], [] #Store amount of nodes expanded for 3 algos
uc_max, mt_max, md_max = [], [], [] #Store max q size expanded for 3 algos
uc_rt, mt_rt, md_rt = [], [], [] #Store runtime expanded for 3 algos


for puzzle in puzzles:
    ucnode, ucexpanded_nodes, ucmax_q_size, ucdepth, ucruntime = general_search(puzzle, goal_state, uniform_cost)
    mtnode, mtexpanded_nodes, mtmax_q_size, mtdepth, mtruntime = general_search(puzzle, goal_state, astar_misplaced)
    mdnode, mdexpanded_nodes, mdmax_q_size, mddepth, mdruntime = general_search(puzzle, goal_state, astar_manhattan)

    depths.append(ucdepth)
    
    uc_exp.append(ucexpanded_nodes)
    mt_exp.append(mtexpanded_nodes)
    md_exp.append(mdexpanded_nodes)

    uc_max.append(ucmax_q_size)
    mt_max.append(mtmax_q_size)
    md_max.append(mdmax_q_size)

    uc_rt.append(ucruntime)
    mt_rt.append(mtruntime)
    md_rt.append(mdruntime)



#Plotting Nodes Expanded vs Depth
plt.figure(figsize=(8,6))
plt.plot(depths, uc_exp, label="Uniform Cost")
plt.plot(depths, mt_exp, label="A* Misplaced Tile")
plt.plot(depths, md_exp, label="A* Manhattan Distance")
plt.xlabel("Depth")
plt.ylabel("Nodes Expanded")
plt.title("Expanded Nodes vs Depth")
plt.legend()
plt.show()

#Plotting Max Q Size vs Depth
plt.figure(figsize=(8,6))
plt.plot(depths, uc_max, label="Uniform Cost")
plt.plot(depths, mt_max, label="A* Misplaced Tile")
plt.plot(depths, md_max, label="A* Manhattan Distance")
plt.xlabel("Depth")
plt.ylabel("Maximum Queue Size")
plt.title("Maximum Queue Size vs Depth")
plt.legend()
plt.show()

#Plotting Runtime vs Depth
plt.figure(figsize=(8,6))
plt.plot(depths, uc_rt, label="Uniform Cost")
plt.plot(depths, mt_rt, label="A* Misplaced Tile")
plt.plot(depths, md_rt, label="A* Manhattan Distance")
plt.xlabel("Depth")
plt.ylabel("Runtime(seconds)")
plt.title("Runtime vs Depth")
plt.legend()
plt.show()