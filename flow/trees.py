'''
Are you dealing with a TREE problem?
│
├── YES ──> Are you allowed to alter the tree, or are you looking for a specific value/property?
│           │
│           ├── YES ──> Does the problem involve structural relationships (Height, Diameter, LCA, Paths)?
│           │           │
│           │           ├── Process level-by-level (e.g., "Right side view", "Level average")?
│           │           │   └── YES ──> BREADTH-FIRST SEARCH (BFS / Level-Order with a Queue)
│           │           │
│           │           └── Bottom-up calculation (e.g., Max Depth, Check Balanced, Diameter)?
│           │               └── YES ──> POST-ORDER DFS (Recursion)
│           │                           (Gather left and right child details before processing parent)
│           │
│           └── NO ───> Does the problem ask you to construct, copy, or flatten a tree?
│                       ├── Construct from Pre/In/Post-order arrays? ──> PRE-ORDER DFS (Root -> Left -> Right)
│                       └── Flatten tree / Serialize & Deserialize? ────> DFS with a global/state tracking variable
│
└── NO ───> Is the tree specifically a BINARY SEARCH TREE (BST)?
            │
            ├── YES ──> Do you need to find an element, validate the tree, or process elements in order?
            │           ├── Process sorted values / Find K-th smallest? ──> IN-ORDER DFS (Left -> Root -> Right)
            │           └── Search, Insert, or Delete a node? ──────────> BINARY SEARCH PROPERTY
            │                                                             (If target < root, go left; else go right)
            │
            └── NO ───> Does the problem involve evaluating paths that sum up to a target?
                        ├── Path starts at root and ends at leaf? ─────> TOP-DOWN DFS (Pass running sum down)
                        └── Path can start and end anywhere? ──────────> POST-ORDER DFS + PREFIX SUM HASH MAP
'''