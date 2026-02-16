import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import time

class Visualizer:
    def __init__(self, grid):
        self.grid = grid
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.cmap = mcolors.ListedColormap(['white', 'black', 'green', 'red', 'blue', 'yellow', 'purple'])
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
        # Reset transient states (frontier, explored) but keep walls, start, target is handled by logic order
        # Actually easier to just update specific cells based on the sets passed in
        
        # We need to be careful not to overwrite Start (2) and Target (3) visually if we want them distinct
        # But 'Explored' usually covers start. Let's keep Start/Target visible if possible or just let them be covered.
        # Requirement: "Visually distinguish nodes currently in the queue... Explored nodes... Final Path"
        
        # Copy base grid to avoid flickering or persistent state issues if we were redrawing from scratch
        # but for performance, we just update the specific cells in grid_data
        
        for r in range(self.grid.height):
            for c in range(self.grid.width):
                # efficient update? No, just iterate all for correctness first. 
                # Optimization: only update validation logic if needed. 
                # Actually, let's just stick to the sets provided.
                
                val = 0 # Default empty
                if (r, c) in self.grid.walls:
                    val = 1
                elif (r, c) == self.grid.start_pos:
                    val = 2
                elif (r, c) == self.grid.target_pos:
                    val = 3
                
                # Overwrite with algorithm state
                if (r, c) in explored:
                    val = 5
                elif (r, c) in frontier:
                    val = 4
                
                # Path overwrites all
                if path and (r, c) in path:
                    val = 6
                    
                # Keep Start/Target visible on top of explored if we want? 
                # Usually Start is explored. Target is found. 
                # Let's let them be colored by their state (Explored/Path) as that shows flow.
                # BUT, let's ensure Start/Target text or distinct color if they ARE the path.
                # The prompt asks to "Highlight the final successful route".
                
                # Let's enforce the color map logic:
                # If path is present, it draws over everything.
                # If explored, it draws over empty.
                
                self.grid_data[r][c] = val

        self.img.set_data(self.grid_data)
        self.fig.canvas.flush_events()
        # time.sleep(0.01) # Small delay for animation
