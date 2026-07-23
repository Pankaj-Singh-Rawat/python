'''
Are you dealing with a DYNAMIC PROGRAMMING problem?
│
├── YES ──> What is the shape or structure of the input data?
│           │
│           ├── SINGLE ARRAY or NUMBER?
│           │   │
│           │   ├── Choice at position i depends on a fixed history (e.g., House Robber, Climbing Stairs)?
│           │   │   └── YES ──> 1D DP ARRAY / STATE VARS
│           │   │               (dp[i] = max(dp[i-1], dp[i-2] + val))
│           │   │
│           │   └── Finding the longest subsegment following a rule (e.g., LIS)?
│           │       └── YES ──> LONGEST INCREASING SUBSEQUENCE (LIS) PATTERN
│           │                   (O(N^2) standard DP, or O(N log N) using Binary Search)
│           │
│           ├── TWO STRINGS or TWO ARRAYS?
│           │   │
│           │   ├── Comparing prefixes, alignments, or matching (e.g., LCS, Edit Distance)?
│           │   │   └── YES ──> 2D GRID DP
│           │   │               (dp[i][j] depends on dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
│           │   │
│           │   └── Matching a pattern with wildcards (e.g., Wildcard / Regex Matching)?
│           │       └── YES ──> 2D STRING MATCHING DP
│           │
│           ├── A SET OF ITEMS WITH COSTS / WEIGHTS & A CAPACITY LIMIT?
│           │   │
│           │   ├── Each item can only be used ONCE (e.g., Partition Equal Subset Sum)?
│           │   │   └── YES ──> 0/1 KNAPSACK PATTERN
│           │   │               (dp[i][w] = max(dp[i-1][w], val + dp[i-1][w - weight]))
│           │   │
│           │   └── Items can be reused UNLIMITED times (e.g., Coin Change)?
│           │       └── YES ──> UNBOUNDED KNAPSACK PATTERN
│           │
│           └── A 2D GRID / MATRIX?
│               └── Navigating from top-left to bottom-right with min/max cost or total paths?
│                   └── YES ──> MATRIX GRID DP
│                               (dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]))
│
└── NO ───> Does the problem involve ranges, splits, or tree structures?
            │
            ├── Splitting an array/string into continuous sub-ranges (e.g., MCM, Burst Balloons)?
            │   └── YES ──> INTERVAL / RANGE DP
            │               (dp[i][j] = opt over k from i to j of (dp[i][k] + dp[k+1][j]))
            │
            └── Making choices on a hierarchical Tree structure (e.g., House Robber III)?
                └── YES ──> TREE DP
                            (Post-Order DFS returning [include_node, exclude_node])
'''