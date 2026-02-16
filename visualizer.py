import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import time

class Visualizer:
    def __init__(self, grid):
        self.grid = grid
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        # Updated Color Map: 
        # 0:White, 1:Black, 2:Blue(Start), 3:Green(Target), 4:Red(Frontier), 5:Yellow(Explored), 6:Purple(Path)
        self.cmap = mcolors.ListedColormap(['white', 'black', 'blue', 'green', 'red', 'yellow', 'purple'])
        self.bounds = [0, 1, 2, 3, 4, 5, 6, 7]
        self.norm = mcolors.BoundaryNorm(self.bounds, self.cmap.N)
        
        # 0: Empty, 1: Wall, 2: Start, 3: Target, 4: Frontier, 5: Explored, 6: Path
        self.grid_data = [[0 for _ in range(grid.width)] for _ in range(grid.height)]
        
        # Initialize grid data
        for r, c in grid.walls:
            self.grid_data[r][c] = 1
        
        sr, sc = grid.start_pos
        tr, tc = grid.target_pos
        self.grid_data[sr][sc] = 2
        self.grid_data[tr][tc] = 3

        self.img = self.ax.imshow(self.grid_data, cmap=self.cmap, norm=self.norm)
        
        # Grid lines
        self.ax.set_xticks([x - 0.5 for x in range(1, grid.width)], minor=True)
        self.ax.set_yticks([y - 0.5 for y in range(1, grid.height)], minor=True)
        self.ax.grid(which="minor", color="gray", linestyle='-', linewidth=1)
        self.ax.tick_params(which="minor", size=0)
        self.ax.set_xticks([])
        self.ax.set_yticks([]) # Hide ticks

        plt.title("AI Pathfinder - Blind Search Visualization")
        plt.ion() # Interactive mode
        plt.show()

    def update(self, frontier, explored, path=None):
        for r in range(self.grid.height):
            for c in range(self.grid.width):
                val = 0 # Default empty
                
                # 1. Static features
                if (r, c) in self.grid.walls:
                    val = 1
                
                # 2. Dynamic Algorithm State (Overwrites Empty/Wall if valid)
                if (r, c) in explored:
                    val = 5 # Yellow
                elif (r, c) in frontier:
                    val = 4 # Red
                
                # 3. Path (Overwrites Explored/Frontier)
                if path and (r, c) in path:
                    val = 6 # Purple

                # 4. Start/Target (HIGHEST PRIORITY to keep them distinct)
                if (r, c) == self.grid.start_pos:
                    val = 2 # Blue
                elif (r, c) == self.grid.target_pos:
                    val = 3 # Green
                
                self.grid_data[r][c] = val

        self.img.set_data(self.grid_data)
        self.fig.canvas.flush_events()

