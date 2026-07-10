'''
Are you dealing with a STRING problem?
│
├── YES ──> Are you comparing characters or tracking frequencies/counts?
│           │
│           ├── YES ──> Do you need to track characters within a continuous segment?
│           │           └── YES ──> SLIDING WINDOW + HASH MAP / FREQUENCY ARRAY (size 26)
│           │
│           └── NO ───> Do you need to check for duplicates, anagrams, or palindromes?
│                       ├── Anagrams/Frequency ───> HASH MAP or FIXED ARRAY [26]
│                       └── Palindromes ──────────> TWO POINTERS (expanding from center or meeting at center)
│
└── NO ───> Does the problem involve matching prefixes or dictionary words?
            │
            ├── YES ──> Are you searching a massive dictionary of words for prefixes?
            │           └── YES ──> TRIE (Prefix Tree)
            │
            └── NO ───> Are you searching for a specific substring pattern inside a larger string?
                        └── YES ──> KMP ALGORITHM or Z-ALGORITHM
'''