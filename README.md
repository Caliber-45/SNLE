# Smart Network Logistics Engine (SNLE)

## Student Information

* Name: \[Gurpinder Singh]
* Student ID: \[300219228]

## How to Run

From the project root folder, run:

```bash
python src/main.py
```

## Modules

* **src/main.py**: Runs the command-line menu and connects all data structures.
* **src/graph.py**: Stores the weighted directed graph as an adjacency list. Includes BFS, DFS, Dijkstra, cycle detection with DFS coloring, and connected component counting.
* **src/heap.py**: Contains a custom MinHeap for Dijkstra and a custom MaxHeap for the dispatch queue.
* **src/hashmap.py**: Contains a custom hash map using chaining. Supports insert, search, delete, and resize when load factor grows.
* **src/trie.py**: Stores depot and zone names for prefix-based autocomplete.
* **src/utils.py**: Loads data from `network.txt`, formats output, and prints the menu.

## Data Structures and Algorithms Used

* **Adjacency List Graph**: Good for sparse graphs and stores only existing edges.
* **BFS / DFS**: Standard graph traversals from the course.
* **Dijkstra's Algorithm**: Finds the lowest-cost path in a weighted graph using a MinHeap.
* **DFS Coloring**: Uses WHITE, GRAY, and BLACK states to detect cycles.
* **MaxHeap Priority Queue**: Dispatches the highest-priority package first.
* **Hash Map**: Gives fast average lookup for depot information.
* **Trie**: Supports prefix search for depot names.

## Complexity Analysis

* **Adjacency list space**: `O(V + E)`
* **BFS**: `O(V + E)`
* **DFS**: `O(V + E)`
* **Dijkstra with MinHeap**: `O((V + E) log V)`
* **Heap insert / extract**: `O(log N)`
* **Hash map search / insert (average)**: `O(1)`
* **Trie insert / search / prefix walk**: `O(L)` where `L` is the length of the word or prefix

## Sample Features

1. Display network summary
2. Find shortest path
3. Detect cycles
4. Dispatch highest-priority package
5. Search depot by name
6. Autocomplete depot name

## Sample output

C:\\Users\\caliber\\Downloads\\snle\_slides\_fixed\\snle>python src/main.py



===== Smart Network Logistics Engine =====

1\. Display Network Summary

2\. Find Shortest Path

3\. Detect Cycles

4\. Dispatch Highest-Priority Package

5\. Search Depot by Name

6\. Autocomplete Depot Name

7\. Exit

==========================================

Select an option:



## 

