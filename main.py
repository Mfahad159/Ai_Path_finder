import sys
import time
from node import Grid
from visualizer import Visualizer
from search_algorithms import SearchAlgorithms

def main():
    # 1. Setup Grid
    # 1. Setup Grid
    WIDTH, HEIGHT = 15, 15
    START = (2, 2)
    TARGET = (13, 13)
    
    # Create some walls
    walls = []
    # Vertical wall
    for r in range(5, 14): # Adjusted for height 15
        walls.append((r, 10))
    # Horizontal walls
    for c in range(2, 8):
        walls.append((12, c))
    for c in range(11, 15): # Adjusted (max 14)
        walls.append((5, c))

    grid = Grid(WIDTH, HEIGHT, walls, START, TARGET)

    # 2. Show Static Grid & Menu
    vis = Visualizer(grid)
    import matplotlib.pyplot as plt # Ensure plt is available
    plt.pause(0.1) # Essential to render the window before input blocks

    print("AI Pathfinder - Blind Search Visualization")
    print("------------------------------------------")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. Uniform Cost Search (UCS)")
    print("4. Depth-Limited Search (DLS)")
    print("5. Iterative Deepening DFS (IDDFS)")
    print("6. Bidirectional Search")
    
    choice = input("Select Algorithm (1-6): ")
    
    algo = SearchAlgorithms(grid)
    search_generator = None
    
    if choice == '1':
        search_generator = algo.bfs()
        title = "BFS"
    elif choice == '2':
        search_generator = algo.dfs()
        title = "DFS"
    elif choice == '3':
        search_generator = algo.ucs()
        title = "UCS"
    elif choice == '4':
        limit = int(input("Enter Depth Limit: "))
        search_generator = algo.dls(limit)
        title = f"DLS (Limit {limit})"
    elif choice == '5':
        search_generator = algo.iddfs()
        title = "IDDFS"
    elif choice == '6':
        search_generator = algo.bidirectional()
        title = "Bidirectional Search"
    else:
        print("Invalid choice")
        return

    # 3. Run Visualization
    vis.ax.set_title(f"AI Pathfinder - {title}")
    
    found = False
    step_count = 0
    start_time = time.time()
    
    try:
        for frontier, explored, path in search_generator:
            step_count += 1
            if step_count % 2 == 0: # Speed up by skipping frames if needed, or remove for full detail
                 vis.update(frontier, explored, path)
                 plt.pause(0.001) # Small pause for animation logic to handle events
            
            if path:
                vis.update(frontier, explored, path)
                found = True
                print(f"Goal Reached! Path length: {len(path)}")
                break
    except KeyboardInterrupt:
        print("\nSearch Interrupted")

    print(f"Search Finished in {time.time() - start_time:.4f}s")
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    import matplotlib.pyplot as plt # lazy import for main check
    main()
