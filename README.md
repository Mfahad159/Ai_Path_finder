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

## Project Gallery

Here are visualizations of the search algorithms exploring the grid.
*(Blue = Start, Green = Target, Yellow = Explored, Red = Frontier, Purple = Path)*

### 1. Visualization Examples
![Search Vis 1](images/Figure_1.png)
*Figure 1: Algorithm execution*

![Search Vis 2](images/Figure_2.png)
*Figure 2: Algorithm execution*

![Search Vis 3](images/Figure_3.png)
*Figure 3: Algorithm execution*

![Search Vis 4](images/Figure_4.png)
*Figure 4: Algorithm execution*

![Search Vis 5](images/Figure_5.png)
*Figure 5: Algorithm execution*

![Search Vis 6](images/Figure_6.png)
*Figure 6: Algorithm execution*

![Search Vis 7](images/Figure_7.png)
*Figure 7: Algorithm execution*

![Search Vis 8](images/Figure_8.png)
*Figure 8: Algorithm execution*

![Search Vis 9](images/Figure_9.png)
*Figure 9: Algorithm execution*

![Search Vis 10](images/Figure_10.png)
*Figure 10: Algorithm execution*
