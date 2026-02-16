import sys
import time
from node import Grid
from visualizer import Visualizer
from search_algorithms import SearchAlgorithms

def main():
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

    while True:
        grid = Grid(WIDTH, HEIGHT, walls, START, TARGET)

        print("\nAI Pathfinder - Blind Search Visualization")
        print("------------------------------------------")
        print("1. Breadth-First Search (BFS)")
        print("2. Depth-First Search (DFS)")
        print("3. Uniform Cost Search (UCS)")
        print("4. Depth-Limited Search (DLS)")
        print("5. Iterative Deepening DFS (IDDFS)")
        print("6. Bidirectional Search")
        print("0. Exit")
        
        choice = input("Select Algorithm (1-6, 0 to Exit): ")
        
        if choice == '0':
            print("Exiting...")
            break

        # 2. Show Static Grid & Menu (Re-init for fresh state)
        # We process choice first so we don't open a window if user wants to exit
        # Also, we need to create the visualizer *after* choice to know we are running, 
        # BUT user wanted to see grid static? 
        # Actually user said: "when python main.py runs it should show grid (but static) and when options selected it starts traversing"
        # If we are looping, we probably want to open the window, show static, wait for input... 
        # But input() blocks the main thread, so the window might freeze if not handled carefully.
        # Matplotlib 'plt.pause' handles the GUI event loop.
        # A simple input() call will freeze the GUI.
        
        # To strictly satisfy "show grid static -> select option":
        # We can open the window in non-blocking mode, but input() is blocking terminal.
        # The window will be unresponsive during input(). This is acceptable for a simple script.
        
        vis = Visualizer(grid)
        import matplotlib.pyplot as plt
        plt.pause(0.1) # Render static grid

        algo = SearchAlgorithms(grid)
        search_generator = None
        title = ""
        
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
            plt.close()
            continue

        # 3. Run Visualization
        vis.ax.set_title(f"AI Pathfinder - {title}")
        
        found = False
        step_count = 0
        start_time = time.time()
        
        try:
            for frontier, explored, path in search_generator:
                step_count += 1
                # Update every step or skip for speed
                vis.update(frontier, explored, path)
                plt.pause(0.001) 
                
                if path:
                    vis.update(frontier, explored, path)
                    found = True
                    print(f"Goal Reached! Path length: {len(path)}")
                    break
        except KeyboardInterrupt:
            print("\nSearch Interrupted")
        
        print(f"Search Finished in {time.time() - start_time:.4f}s")
        
        input("Press Enter to return to menu...")
        plt.close('all') # Clean up window before next iteration

if __name__ == "__main__":
    import matplotlib.pyplot as plt # lazy import for main check
    main()
