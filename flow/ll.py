'''
Are you dealing with a LINKED LIST problem?
│
├── YES ──> Does the problem involve modifying the structure or order?
│           │
│           ├── YES ──> Are you asked to reverse, reorder, or manipulate nodes in blocks?
│           │           └── YES ──> IN-PLACE REVERSAL / "REVERSE IN K-GROUPS"
│           │                       (Use a 'prev' pointer and a temporary 'next' pointer)
│           │
│           └── NO ───> Are you Asked to merge lists, partition, or remove specific nodes?
│                       ├── YES ──> DUMMY NODE + ITERATION
│                       │           (Simplifies corner cases like an empty list or new head)
│                       └── NO ───> Are you merging multiple sorted lists?
│                                   └── YES ──> HEAP (PRIORITY QUEUE) OR DIVIDE AND CONQUER
│
└── NO ───> Does the problem involve checking properties or finding specific nodes?
            │
            ├── YES ──> Are you looking for the midpoint, a cycle, or the intersection?
            │           │
            │           ├── Cycle Detection? ──> FLOYD’S TORTOISE & HARE (Two Pointers: Slow/Fast)
            │           │
            │           ├── Find Midpoint? ───> FAST & SLOW POINTERS
            │           │                       (Fast moves 2x the speed of Slow)
            │           │
            │           └── Intersection Point? ─> TWO POINTERS / HASH SET
            │
            └── NO ───> Are you looking for the Nth node from the end?
                        └── YES ──> TWO POINTERS (With a gap of N nodes)
'''