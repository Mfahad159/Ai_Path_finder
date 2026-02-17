import sys
import time
from node import Grid
from visualizer import Visualizer
from search_algorithms import SearchAlgorithms

def main():
    while True:
        print("\nAI Pathfinder - Select Scenario")
        print("1. Standard Map (Assignment Default)")
        print("2. Best Case (Open Space, Close Target)")
        print("3. Worst Case (Target Trapped behind Wall)")
        print("0. Exit")
        
        scen_choice = input("Select Scenario (1-3, 0 to Exit): ")
        
        if scen_choice == '0':
            break
            
        WIDTH, HEIGHT = 15, 15
        START = (2, 2)
        walls = []
        
        if scen_choice == '2': # Best Case
            TARGET = (5, 5) # Close
            # No walls
        elif scen_choice == '3': # Worst Case
            TARGET = (12, 12)
            # Create a C-shape trap around the start or a maze
            # Let's block the direct diagonal path
            for r in range(0, 10):
                walls.append((r, 8)) # Vertical wall blocking right
            for c in range(0, 8):
                walls.append((10, c)) # Horizontal wall blocking bottom
            # Force it to go ALL the way around
        else: # Standard
            TARGET = (13, 13)
            for r in range(5, 14):
                walls.append((r, 10))
            for c in range(2, 8):
                walls.append((12, c))
            for c in range(11, 15): 
                walls.append((5, c))

        grid = Grid(WIDTH, HEIGHT, walls, START, TARGET)

        # 2. Show Static Grid & Menu
        vis = Visualizer(grid)
        import matplotlib.pyplot as plt
        plt.pause(0.1) 
        
        # Inner loop for algorithm selection on this map
        algo = SearchAlgorithms(grid)
        while True:
            # Re-drawing the clean grid if we re-run logic would be nice, 
            # but visualizer.reset() handles that.
            
            print("\nSelect Algorithm for this Map:")
            print("1. Breadth-First Search (BFS)")
            print("2. Depth-First Search (DFS)")
            print("3. Uniform Cost Search (UCS)")
            print("4. Depth-Limited Search (DLS)")
            print("5. Iterative Deepening DFS (IDDFS)")
            print("6. Bidirectional Search")
            print("9. Change Map / Back")
            
            choice = input("Select Algorithm (1-6, 9 to Back): ")
            
            if choice == '9':
                plt.close('all')
                break
            
            # ... rest of algo logic ...
        
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
                try:
                    limit = int(input("Enter Depth Limit: "))
                    search_generator = algo.dls(limit)
                    title = f"DLS (Limit {limit})"
                except ValueError:
                    print("Invalid limit")
                    continue
            elif choice == '5':
                search_generator = algo.iddfs()
                title = "IDDFS"
            elif choice == '6':
                search_generator = algo.bidirectional()
                title = "Bidirectional Search"
            else:
                print("Invalid choice")
                continue

            # 3. Run Visualization
            vis.ax.set_title(f"AI Pathfinder - {title}")
            
            found = False
            step_count = 0
            start_time = time.time()
            
            try:
                for frontier, explored, path in search_generator:
                    step_count += 1
                    # Update every step
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
            
            print("Press Enter to continue...")
            input()
            vis.reset() # Reset for next algo on same map
        
    plt.close('all')

if __name__ == "__main__":
    import matplotlib.pyplot as plt # lazy import for main check
    main()
