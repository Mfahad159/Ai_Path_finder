from collections import deque
import heapq
from node import Node

def get_path(node):
    path = []
    curr = node
    while curr:
        path.append((curr.r, curr.c))
        curr = curr.parent
    return path[::-1]

class SearchAlgorithms:
    def __init__(self, grid):
        self.grid = grid

    def bfs(self):
        start_node = Node(*self.grid.start_pos)
        if start_node.r == self.grid.target_pos[0] and start_node.c == self.grid.target_pos[1]:
            return [], [], [(start_node.r, start_node.c)]

        frontier = deque([start_node])
        explored = set()
        frontier_set = { (start_node.r, start_node.c) } # For fast lookup

        while frontier:
            node = frontier.popleft()
            frontier_set.remove((node.r, node.c))
            explored.add((node.r, node.c))

            if (node.r, node.c) == self.grid.target_pos:
                yield frontier_set, explored, get_path(node)
                return

            for neighbor in self.grid.get_neighbors(node):
                if (neighbor.r, neighbor.c) not in explored and (neighbor.r, neighbor.c) not in frontier_set:
                    frontier.append(neighbor)
                    frontier_set.add((neighbor.r, neighbor.c))
            
            yield frontier_set, explored, []

    def dfs(self):
        start_node = Node(*self.grid.start_pos)
        frontier = [start_node] # Stack
        explored = set()
        frontier_set = { (start_node.r, start_node.c) }

        while frontier:
            node = frontier.pop()
            frontier_set.remove((node.r, node.c))
            
            if (node.r, node.c) == self.grid.target_pos:
                yield frontier_set, explored, get_path(node)
                return

            if (node.r, node.c) not in explored:
                explored.add((node.r, node.c))
                yield frontier_set, explored, []

                # If we want to *visit* Up first, in DFS, we push neighbors in REVERSE order.
                for neighbor in reversed(self.grid.get_neighbors(node)):
                     if (neighbor.r, neighbor.c) not in explored: # Optimization check
                        frontier.append(neighbor)
                        frontier_set.add((neighbor.r, neighbor.c))


    def ucs(self):
        start_node = Node(*self.grid.start_pos)
        frontier = []
        heapq.heappush(frontier, start_node)
        explored = set()
        frontier_set = { (start_node.r, start_node.c) }
        cost_so_far = { (start_node.r, start_node.c): 0 }

        while frontier:
            node = heapq.heappop(frontier)
            frontier_set.discard((node.r, node.c)) # Might be in there multiple times with diff costs

            if (node.r, node.c) == self.grid.target_pos:
                yield frontier_set, explored, get_path(node)
                return

            if (node.r, node.c) not in explored: # Lazy deletion
                explored.add((node.r, node.c))
                yield frontier_set, explored, []

                for neighbor in self.grid.get_neighbors(node):
                    new_cost = cost_so_far[(node.r, node.c)] + 1 # Uniform cost 1
                    if (neighbor.r, neighbor.c) not in cost_so_far or new_cost < cost_so_far[(neighbor.r, neighbor.c)]:
                        cost_so_far[(neighbor.r, neighbor.c)] = new_cost
                        neighbor.cost = new_cost
                        heapq.heappush(frontier, neighbor)
                        frontier_set.add((neighbor.r, neighbor.c))

    def dls(self, limit):
        start_node = Node(*self.grid.start_pos)
        path_stack = [start_node] # Stack storing nodes
        explored_depths = {} # (r,c) -> min_depth visited

        # We can't use a simple valid 'explored' set because we might revisit at shallower depth.
        
        while path_stack:
            node = path_stack.pop()
            
            if (node.r, node.c) == self.grid.target_pos:
                yield set(), explored_depths.keys(), get_path(node)
                return True

            if (node.r, node.c) not in explored_depths or node.depth < explored_depths[(node.r, node.c)]:
                explored_depths[(node.r, node.c)] = node.depth
                yield set(n.r for n in path_stack), explored_depths.keys(), [] # Approximate frontier viz

                if node.depth < limit:
                    # Reverse for DFS order
                    for neighbor in reversed(self.grid.get_neighbors(node)):
                        path_stack.append(neighbor)
        
        return False

    def iddfs(self):
        depth = 0
        while True:
            # But the 'explored' set in visualizer persists? 
            # The visualizer.update method REPLACES the grid colors based on inputs.
            # So if DLS yields empty sets at start, it clears.
            
            # However, DLS generator above yields explored_depths.keys().
            # So it will show the fresh search.
            found = yield from self.dls(depth)
            if found:
                return
            depth += 1
            if depth > self.grid.width * self.grid.height: # Sad safety break
                return 

    def bidirectional(self):
        start_node = Node(*self.grid.start_pos)
        target_node = Node(*self.grid.target_pos)

        f_src = deque([start_node])
        f_tgt = deque([target_node])
        
        explored_src = { (start_node.r, start_node.c): start_node }
        explored_tgt = { (target_node.r, target_node.c): target_node }

        while f_src and f_tgt:
            # Expand Source
            if f_src:
                curr = f_src.popleft()
                if (curr.r, curr.c) in explored_tgt:
                    # Meet point!
                    path_a = get_path(curr)
                    # Reconstruct path B from target backwards
                    meet_node_b = explored_tgt[(curr.r, curr.c)]
                    path_b = get_path(meet_node_b) # This goes T -> ... -> Meet
                    # Join them. path_b needs to be reversed to go Meet -> ... -> T? 
                    # get_path returns S -> ... -> Node.
                    # So path_b is T -> ... -> Meet.
                    # We want S -> ... -> Meet -> ... -> T.
                    path_b.pop() # Remove duplicate meet point
                    final_path = path_a + path_b[::-1] # Reverse path_b to get Meet -> ... -> T
                    
                    yield set(), set(explored_src.keys()) | set(explored_tgt.keys()), final_path
                    return

                for neighbor in self.grid.get_neighbors(curr):
                    if (neighbor.r, neighbor.c) not in explored_src:
                        explored_src[(neighbor.r, neighbor.c)] = neighbor
                        f_src.append(neighbor)

            # Expand Target
            if f_tgt:
                curr = f_tgt.popleft()
                if (curr.r, curr.c) in explored_src:
                     # Meet point!
                    path_b = get_path(curr) # T -> Meet
                    meet_node_a = explored_src[(curr.r, curr.c)]
                    path_a = get_path(meet_node_a) # S -> Meet
                    
                    path_b.pop()
                    final_path = path_a + path_b[::-1]
                    
                    yield set(), set(explored_src.keys()) | set(explored_tgt.keys()), final_path
                    return

                for neighbor in self.grid.get_neighbors(curr):
                    if (neighbor.r, neighbor.c) not in explored_tgt:
                        explored_tgt[(neighbor.r, neighbor.c)] = neighbor
                        f_tgt.append(neighbor)
            
            # Visualization yield
            frontier_viz = set((n.r, n.c) for n in f_src) | set((n.r, n.c) for n in f_tgt)
            explored_viz = set(explored_src.keys()) | set(explored_tgt.keys())
            yield frontier_viz, explored_viz, []
