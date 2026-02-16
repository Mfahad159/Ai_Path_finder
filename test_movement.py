from node import Node, Grid

def test_strict_movement():
    print("Testing Strict Movement Order...")
    # Create a 3x3 grid with start at center (1,1)
    # Order should be: Up, Right, Bottom, Bottom-Right, Left, Top-Left
    # Coordinates: (-1,0), (0,1), (1,0), (1,1), (0,-1), (-1,-1) relative to center
    
    # 0,0  0,1  0,2
    # 1,0  1,1  1,2
    # 2,0  2,1  2,2
    
    # Neighbors of (1,1):
    # 1. Up: (0,1)
    # 2. Right: (1,2)
    # 3. Bottom: (2,1)
    # 4. Bottom-Right: (2,2)
    # 5. Left: (1,0)
    # 6. Top-Left: (0,0)
    
    grid = Grid(3, 3, [], (0,0), (2,2)) # Walls empty
    center_node = Node(1, 1)
    
    neighbors = grid.get_neighbors(center_node)
    
    expected = [
        (0, 1), # Up
        (1, 2), # Right
        (2, 1), # Bottom
        (2, 2), # Bottom-Right
        (1, 0), # Left
        (0, 0)  # Top-Left
    ]
    
    actual = [(n.r, n.c) for n in neighbors]
    
    print(f"Center Node: (1, 1)")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    
    assert actual == expected, "Strict movement order Failed!"
    print("✅ Strict movement order Verified!")

def test_walls():
    print("\nTesting Wall Collision...")
    # Wall at (0,1) - Up
    grid = Grid(3, 3, [(0,1)], (0,0), (2,2))
    center_node = Node(1, 1)
    neighbors = grid.get_neighbors(center_node)
    
    # Up (0,1) should be missing
    expected = [
        (1, 2), # Right
        (2, 1), # Bottom
        (2, 2), # Bottom-Right
        (1, 0), # Left
        (0, 0)  # Top-Left
    ]
    
    actual = [(n.r, n.c) for n in neighbors]
    
    assert actual == expected, "Wall collision logic Failed!"
    print("✅ Wall collision Verified!")

if __name__ == "__main__":
    test_strict_movement()
    test_walls()
