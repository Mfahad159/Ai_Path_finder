# AI Pathfinder – Blind Search Visualization

This project provides a **visual demonstration of classical blind (uninformed) search algorithms** used in Artificial Intelligence.  
It shows how different algorithms explore a grid-based environment to find a path from a **Start node (S)** to a **Target node (T)** while avoiding static obstacles (walls).

The goal is to help learners **intuitively understand search behavior, exploration patterns, and performance differences** among blind search strategies.

---

## 🔍 Implemented Algorithms

The following six fundamental blind search algorithms are implemented and visualized:

1. **Breadth-First Search (BFS)**  
2. **Depth-First Search (DFS)**  
3. **Depth-Limited Search (DLS)**  
4. **Iterative Deepening Depth-First Search (IDDFS)**  
5. **Uniform Cost Search (UCS)**  
6. **Bidirectional Search**

Each algorithm explores the same grid environment using a consistent movement policy to ensure fair comparison.

---

## 🧭 Strict Movement Order

All algorithms expand neighboring nodes using a **fixed clockwise order** (including only the main diagonal directions):

1. **Up**  
2. **Right**  
3. **Down**  
4. **Down-Right (Diagonal)**  
5. **Left**  
6. **Up-Left (Diagonal)**  

> **Note:**  
> The **Top-Right** and **Bottom-Left** diagonal moves are intentionally excluded to maintain deterministic and controlled behavior across all searches.

---

## ⚙️ Setup & Execution

### 1️⃣ Install Required Dependency
```bash
pip install matplotlib
```

### 2️⃣ Run the Application
```bash
python main.py
```
You will be prompted to select a scenario and a search algorithm.  
The visualization will then animate how the chosen algorithm explores the grid.

---

## 🖼️ Project Gallery
Below are sample visualizations showing the search algorithms in action.

### 🎨 Color Legend
*   🔵 **Blue** — Start Node
*   🟢 **Green** — Target Node
*   🟡 **Yellow** — Explored Nodes
*   🔴 **Red** — Frontier (Open List)
*   🟣 **Purple** — Final Path

### 📌 Visualization Examples

![Figure 1: Search algorithm execution](images/Figure_1.png)
*Figure 1: Search algorithm execution*

![Figure 2: Search algorithm execution](images/Figure_2.png)
*Figure 2: Search algorithm execution*

![Figure 3: Search algorithm execution](images/Figure_3.png)
*Figure 3: Search algorithm execution*

![Figure 4: Search algorithm execution](images/Figure_4.png)
*Figure 4: Search algorithm execution*

![Figure 5: Search algorithm execution](images/Figure_5.png)
*Figure 5: Search algorithm execution*

![Figure 6: Search algorithm execution](images/Figure_6.png)
*Figure 6: Search algorithm execution*

![Figure 7: Search algorithm execution](images/Figure_7.png)
*Figure 7: Search algorithm execution*

![Figure 8: Search algorithm execution](images/Figure_8.png)
*Figure 8: Search algorithm execution*

![Figure 9: Search algorithm execution](images/Figure_9.png)
*Figure 9: Search algorithm execution*

![Figure 10: Search algorithm execution](images/Figure_10.png)
*Figure 10: Search algorithm execution*
