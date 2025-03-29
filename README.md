# Eight Puzzle Project

## Introduction
The goal of this assignment is to demonstrate the performance of different search algorithms in solving eight puzzles. The eight puzzle is a sliding puzzle consisting of a 3x3 grid with numbered tiles and one blank space. The objective is to move the tiles to achieve a goal state where the numbers are in order, and the blank space is in the bottom right corner.

Search algorithms are effective solutions to this problem, as they explore different puzzle states to find an optimal solution. This project implements the following search algorithms:
- **Uniform Cost Search**
- **A* with the Misplaced Tile Heuristic**
- **A* with the Manhattan Distance Heuristic**

## Algorithm Overview
### Uniform Cost Search
Uniform Cost Search assumes each move has the same cost. The algorithm expands nodes based on their cumulative cost, working similarly to Breadth-First Search by expanding nodes at the lowest depth before deeper nodes.

### A* Misplaced Tile
A* search uses a cost function that combines path cost with a heuristic estimate. The **misplaced tile heuristic** counts the number of misplaced tiles compared to the goal state.

### A* Manhattan Distance
A* with the **Manhattan Distance heuristic** calculates the sum of the horizontal and vertical distances between each tile's current position and its goal position. This heuristic provides a more informed estimate of the remaining moves needed to solve the puzzle.

## Comparison of Algorithm Performance
### Nodes Expanded vs Depth
A key performance measure is the number of nodes expanded at various depths. The graph below compares each algorithm's performance:

![Nodes Expanded](#)

### Maximum Queue Size vs Depth
The maximum queue size indicates the space complexity of each algorithm:

![Maximum Queue Size](#)

### Runtime vs Depth
Execution time is critical in evaluating algorithm efficiency:

![Runtime](#)

## Conclusion
A* with the Manhattan Distance heuristic consistently outperforms the other algorithms in terms of runtime, expanded nodes, and queue size. While both A* algorithms are heuristic-based, their performance differences highlight the importance of heuristic selection.

## Traceback of Example 8-Puzzles
### Depth 4 with Uniform Cost Search
```plaintext
[1, 2, 3]    → [0, 5, 6]  → [4, 5, 6]  → [4, 5, 6]  → [4, 5, 6]
[5, 0, 6]    → [1, 2, 3]  → [1, 2, 3]  → [1, 2, 3]  → [1, 2, 3]
[4, 7, 8]    → [4, 7, 8]  → [0, 7, 8]  → [7, 0, 8]  → [7, 8, 0]
```
**Nodes Expanded:** 36  
**Maximum Queue Size:** 32  
**Depth:** 4  

### Depth 20 with A* Manhattan Distance
```plaintext
[7, 1, 2]    → [7, 1, 2]  → ... → [4, 5, 0]  → [4, 5, 6]
[4, 8, 5]    → [4, 8, 5]  → ... → [1, 2, 3]  → [1, 2, 3]
[6, 3, 0]    → [6, 0, 3]  → ... → [7, 8, 6]  → [7, 8, 0]
```
**Nodes Expanded:** 363  
**Maximum Queue Size:** 234  
**Depth:** 20  

## GitHub Repository
The complete project code is available at: [EightPuzzleProject Repository](https://github.com/KushMomaya/EightPuzzleProject-main)

### File Breakdown
#### **Main**
- Interface to select a predefined puzzle or enter a custom state
- Allows selection of search algorithms
- Displays key performance metrics

#### **Algo**
- Contains search algorithm implementations
- General search function that integrates specific algorithms
- Helper functions for heuristic calculations and node expansion

#### **Examples**
- Contains code for graphing algorithm performance
- Generates three key performance graphs

#### **Node**
- Defines node structure for storing puzzle states
- Implements custom comparison operator for queue ordering
