# AI Pathfinder - Blind Search Visualization

This project allows you to visualize how different "blind" search algorithms explore a map. It implements six fundamental search strategies to navigate a grid from a Start Point (S) to a Target Point (T) while avoiding static walls.

## Algorithms
1.  Breadth-First Search (BFS)
2.  Depth-First Search (DFS)
3.  Depth-Limited Search (DLS)
4.  Iterative Deepening DFS (IDDFS)
5.  Uniform Cost Search (UCS)
6.  Bidirectional Search

## Strict Movement Order
The algorithms explore neighbors in this specific clockwise order (including main diagonal only):
1.  Up
2.  Right
3.  Bottom
4.  Bottom-Right
5.  Left
6.  Top-Left

## Setup & Run
1.  Install dependencies:
    ```bash
    pip install matplotlib
    ```
2.  Run the application:
    ```bash
    python main.py
    ```
