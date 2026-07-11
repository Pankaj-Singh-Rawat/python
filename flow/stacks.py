'''
Are you dealing with a STACK problem?
│
├── YES ──> Does the problem involve nested structures, brackets, or string decoding?
│           │
│           ├── YES ──> Are you verifying matching pairs or expanding inner layers?
│           │           ├── Valid Parentheses? ─────> CHAR-BY-CHAR STACK MATCHING
│           │           └── Nested Strings/Decodes? ──> TWO STACKS (One for counts, one for prefixes)
│           │
│           └── NO ───> Are you evaluating an algebraic or string path expression?
│                       ├── Calculator / Postfix? ──> EVALUATION STACK (Push operands, pop on operator)
│                       └── Directory Paths (../)? ──> SYSTEM / DIRECTORY STACK (Pop on "..", push on folder)
│
└── NO ───> Does the problem ask you to find the "Next Greater" or "Previous Smaller" element?
            │
            ├── YES ──> Are you looking for the closest element that meets a size condition?
            │           └── YES ──> MONOTONIC STACK 
            │                       ├── Monotonic Increasing (Maintains elements in rising order)
            │                       └── Monotonic Decreasing (Maintains elements in falling order)
            │
            └── NO ───> Do you need to track the history of an operation (Undo/Redo or Browser Back)?
                        └── YES ──> TWO STACKS (Main history stack + temporary auxiliary stack)
'''