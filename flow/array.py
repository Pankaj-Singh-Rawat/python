'''
Are you dealing with an ARRAY problem?
│
├── YES ──> Is the array SORTED?
│           │
│           ├── YES ──> Are you searching for a specific element/boundary?
│           │           ├── YES ──> BINARY SEARCH
│           │           └── NO ───> Do you need to find pairs/triplets that match a target sum?
│           │                       └── YES ──> TWO POINTERS (Left & Right meeting in the middle)
│           │
│           └── NO ───> Are you looking for a SUBARRAY (contiguous elements)?
│                       │
│                       ├── YES ──> Does the problem involve a sum, length, or distinct characters?
│                       │           ├── YES ──> SLIDING WINDOW 
│                       │           │           ├── Fixed Size (e.g., "Max sum of K elements")
│                       │           │           └── Variable Size (e.g., "Longest subarray with sum <= K")
│                       │           └── NO ───> Do you need cumulative sums frequently?
│                       │                       └── YES ──> PREFIX SUM Array
│                       │
│                       └── NO ───> Are you looking for a SUBSEQUENCE/SUBSET (non-contiguous)?
│                                   │
│                                   ├── YES ──> Are you asked to find the max/min of something, or "total ways"?
│                                   │           ├── YES ──> DYNAMIC PROGRAMMING (0/1 Knapsack type or LIS)
│                                   │           └── NO ───> Do you need to generate all possible combinations?
│                                   │                       └── YES ──> BACKTRACKING
│                                   │
│                                   └── NO ───> Do you need to find the "Next Greater" or "Previous Smaller" element?
│                                               └── YES ──> MONOTONIC STACK
'''