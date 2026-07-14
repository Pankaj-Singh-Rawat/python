'''
Are you dealing with a QUEUE problem?
│
├── YES ──> Does the problem involve traversing a structural space (Grid, Tree, or Graph)?
│           │
│           ├── YES ──> Are you looking for the SHORTEST path, level-by-level processing, or minimum steps?
│           │           └── YES ──> BREADTH-FIRST SEARCH (BFS)
│           │                       (Process elements level-by-level using a standard Queue)
│           │
│           └── NO ───> Are there multiple starting points expanding simultaneously (e.g., spreading fire/rot)?
│                       └── YES ──> MULTI-SOURCE BFS
│                                   (Initialize Queue with all starting points at Step 0)
│
└── NO ───> Does the problem involve a sliding window or maintaining max/min elements?
            │
            ├── YES ──> Do you need to find the maximum or minimum value in a sliding window of size K?
            │           └── YES ──> MONOTONIC DEQUE (Double-Ended Queue)
            │                       (Store indices; pop from back to keep elements ordered, pop from front if out of window)
            │
            └── NO ───> Are you designing a system that processes data in order, or limits traffic?
                        ├── First In, First Out (FIFO)? ──> CIRCULAR QUEUE (Using a fixed-size array)
                        └── Rate Limiter / Stream? ────────> DEQUE (Discard timestamps older than current window)
'''