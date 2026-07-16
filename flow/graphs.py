'''
Are you dealing with a GRAPH problem?
│
├── YES ──> Is the graph UNWEIGHTED (all connections have equal cost/distance)?
│           │
│           ├── YES ──> Are you looking for the shortest path or minimum steps?
│           │           ├── YES ──> BREADTH-FIRST SEARCH (BFS)
│           │           │           (Guarantees shortest path in O(V + E) time)
│           │           └── NO ───> Are you looking for connectivity, paths, or cycle detection?
│           │                       └── YES ──> DEPTH-FIRST SEARCH (DFS) or UNION-FIND
│           │
│           └── NO ───> Is the graph WEIGHTED (edges have different costs/lengths)?
│                       │
│                       ├── YES ──> Are you looking for the SHORTEST PATH from a source node?
│                       │           ├── Are all weights non-negative (>= 0)?
│                       │           │   └── YES ──> DIJKSTRA'S ALGORITHM (O(E log V))
│                       │           └── Are there negative weights?
│                       │               └── YES ──> BELLMAN-FORD ALGORITHM (O(V * E))
│                       │
│                       └── NO ───> Do you need the shortest path between ALL pairs of nodes?
│                                   └── YES ──> FLOYD-WARSHALL ALGORITHM (O(V^3))
│
└── NO ───> Does the problem involve building connections or tracking groups/orders?
            │
            ├── YES ──> Are you determining dependencies or a valid sequencing order?
            │           └── YES ──> TOPOLOGICAL SORT (Kahn's Algorithm or DFS with recursion)
            │                       (Only works on Directed Acyclic Graphs - DAGs)
            │
            └── NO ───> Are you connecting all nodes with the minimum possible total weight?
                        ├── YES ──> MINIMUM SPANNING TREE (MST)
                        │           ├── Kruskal's Algorithm (Sort edges + Union-Find / DSU)
                        │           └── Prim's Algorithm (Min-Heap / Priority Queue)
                        └── NO ───> Are you merging dynamic groups or checking if they share a set?
                                    └── YES ──> DISJOINT SET UNION (DSU / Union-Find)
'''