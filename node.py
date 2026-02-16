class Node:
    def __init__(self, r, c, parent=None, cost=0, depth=0):
        self.r = r
        self.c = c
        self.parent = parent
        self.cost = cost
        self.depth = depth

    def __eq__(self, other):
        return self.r == other.r and self.c == other.c

    def __hash__(self):
        return hash((self.r, self.c))

    def __lt__(self, other):
        return self.cost < other.cost  # For priority queue

    def __repr__(self):
        return f"Node({self.r}, {self.c})"


class Grid:
    def __init__(self, width, height, walls, start_pos, target_pos):
        self.width = width
        self.height = height
        self.walls = set(walls)  # Set of (r, c) tuples
        self.start_pos = start_pos
        self.target_pos = target_pos

    def is_valid(self, r, c):
        # Check bounds
        if not (0 <= r < self.height and 0 <= c < self.width):
            return False
        # Check walls
        if (r, c) in self.walls:
            return False
        return True

    def get_neighbors(self, node):
        """
        Returns neighbors in the specific Strict Movement Order:
        1. Up
        2. Right
        3. Bottom
        4. Bottom-Right (Diagonal)
        5. Left
        6. Top-Left (Diagonal)
        """
        r, c = node.r, node.c
        moves = [
            (-1, 0),   # 1. Up
            (0, 1),    # 2. Right
            (1, 0),    # 3. Bottom
            (1, 1),    # 4. Bottom-Right
            (0, -1),   # 5. Left
            (-1, -1)   # 6. Top-Left
        ]

        neighbors = []
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if self.is_valid(nr, nc):
                cost = 1  # Uniform cost
                neighbors.append(Node(nr, nc, parent=node, cost=node.cost + cost, depth=node.depth + 1))
        
        return neighbors
